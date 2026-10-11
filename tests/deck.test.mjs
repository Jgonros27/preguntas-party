import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { draw, validateCards } from "../src/lib/deck.mjs";
const categories = ["telepatia", "mimica", "preguntas", "dibujos", "prohibido"];
const content = Object.fromEntries(
  categories.map((category) => [
    category,
    JSON.parse(
      readFileSync(
        new URL(`../src/data/${category}.json`, import.meta.url),
        "utf8",
      ),
    ),
  ]),
);

test("7.500 tarjetas válidas, 1.500 por categoría y tres formatos de preguntas", () => {
  for (const category of categories) {
    const cards = content[category];
    assert.equal(validateCards(category, cards).length, 1500);
    assert.equal(new Set(cards.map((c) => c.prompt.toLowerCase())).size, 1500);
    assert.ok(
      cards.every(
        (c) =>
          !/\b(?:lorem ipsum|pendiente|tarjeta \d+|prueba \d+)\b/i.test(
            c.prompt,
          ),
      ),
    );
    assert.equal(new Set(cards.map((c) => c.difficulty)).size, 3);
    assert.ok(new Set(cards.map((c) => c.topic)).size >= 8);
    if (category === "preguntas")
      assert.equal(new Set(cards.map((c) => c.type)).size, 3);
  }
});

test("las tres dificultades y los ámbitos están presentes en TODOS los mazos", () => {
  for (const category of categories) {
    const cards = content[category];
    for (const difficulty of ["easy", "medium", "hard"])
      assert.ok(
        cards.filter((c) => c.difficulty === difficulty).length >= 20,
        `${category}: ${difficulty}`,
      );
    const topics = cards.map((c) => c.topic.toLowerCase());
    if (category !== "preguntas") {
      for (const theme of ["animal", "personaje", "acci"])
        assert.ok(
          topics.some((topic) => topic.includes(theme)),
          `${category}: ${theme}`,
        );
    } else {
      for (const theme of [
        "ciencia",
        "historia",
        "geografía",
        "música",
        "deportes",
        "cine",
      ])
        assert.ok(
          topics.some((topic) => topic.includes(theme)),
          theme,
        );
    }
  }
});

test("mímica incluye los ejemplos reconocibles solicitados y muchas acciones fáciles", () => {
  const cards = content.mimica;
  for (const prompt of [
    "El rey león",
    "Tiburón",
    "Harry Potter",
    "Spider-Man",
    "Atracar un banco",
    "Hacer una tortilla de patatas",
    "Mascar un chicle",
    "Cirujano",
    "Albañil",
    "Electricista",
    "Canguro",
    "Pájaro carpintero",
    "Cangrejo",
    "Gorila",
    "Se me han olvidado las gafas",
    "Subirse a una montaña rusa",
    "Tener un déjà vu",
  ])
    assert.ok(
      cards.some((c) => c.prompt === prompt),
      prompt,
    );
  assert.ok(
    cards.filter(
      (c) => c.topic === "acciones cotidianas" && c.difficulty === "easy",
    ).length >= 400,
  );
});

test("mantiene las 50 identidades iniciales al ampliar los mazos", () => {
  const original = JSON.parse(
    readFileSync(
      new URL("../scripts/content/original.json", import.meta.url),
      "utf8",
    ),
  );
  for (const category of categories)
    for (const card of original[category]) {
      assert.equal(
        content[category].find((c) => c.id === card.id)?.prompt,
        card.prompt,
      );
    }
});

test("dos rondas completas de 1.500 cartas por categoría y recuperación tras recarga", () => {
  for (const category of categories) {
    const ids = content[category].map((c) => c.id);
    let state = {};
    let previous;
    for (let round = 0; round < 2; round++) {
      const seen = new Set();
      for (let i = 0; i < ids.length; i++) {
        const result = draw(ids, state);
        assert.notEqual(result.id, previous);
        assert.ok(!seen.has(result.id));
        seen.add(result.id);
        previous = result.id;
        state =
          i % 100 === 0
            ? JSON.parse(JSON.stringify(result.state))
            : result.state;
      }
      assert.equal(seen.size, 1500);
    }
  }
});
test("sin repeticiones dentro de 100 rondas ni en sus límites", () => {
  let state = {};
  let last;
  for (let round = 0; round < 100; round++) {
    const seen = new Set();
    for (let i = 0; i < 10; i++) {
      const result = draw(
        Array.from({ length: 10 }, (_, i) => String(i)),
        state,
      );
      assert.notEqual(result.id, last);
      assert.ok(!seen.has(result.id));
      seen.add(result.id);
      last = result.id;
      state = JSON.parse(JSON.stringify(result.state));
    }
    assert.equal(seen.size, 10);
  }
});
test("adapta altas y bajas conservando tarjetas usadas", () => {
  let state = { queue: ["b", "c"], used: ["a"], last: "a" };
  const result = draw(["a", "b", "d"], state, () => 0);
  assert.equal(result.id, "d");
  assert.deepEqual(result.state.queue, ["b"]);
  assert.deepEqual(result.state.used, ["a", "d"]);
  assert.equal(draw(["a", "b", "d"], result.state).id, "b");
});
test("una tarjeta, mazo vacío y estado corrupto", () => {
  assert.equal(draw(["a"], { used: ["a"], last: "a" }).id, "a");
  assert.throws(() => draw([]));
  assert.ok(draw(["a", "b"], null).id);
  assert.ok(
    ["a", "b"].includes(draw(["a", "b"], { queue: "bad", used: 4 }).id),
  );
});
test("rechaza duplicados y formatos inválidos", () => {
  assert.throws(() =>
    validateCards("mimica", [
      { id: "a", prompt: "Canguro" },
      { id: "b", prompt: "CÁNGURO!" },
    ]),
  );
  assert.throws(() =>
    validateCards("mimica", [
      { id: "a", prompt: "Canguro", difficulty: "unknown" },
    ]),
  );
  assert.throws(() =>
    validateCards("mimica", [
      { id: "x", prompt: "Uno" },
      { id: "x", prompt: "Dos" },
    ]),
  );
  assert.throws(() =>
    validateCards("prohibido", [
      { id: "x", prompt: "Uno", forbidden: ["a", "b", "c"] },
    ]),
  );
  assert.throws(() =>
    validateCards("preguntas", [
      {
        id: "x",
        prompt: "Uno",
        type: "choice",
        answer: "d",
        options: ["a", "b", "c"],
      },
    ]),
  );
});
