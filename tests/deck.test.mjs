import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { draw, validateCards } from "../src/lib/deck.mjs";
const categories = ["telepatia", "mimica", "preguntas", "dibujos", "prohibido"];
test("50 tarjetas válidas, diez por categoría y tres formatos de preguntas", () => {
  for (const category of categories) {
    const cards = JSON.parse(
      readFileSync(
        new URL(`../src/data/${category}.json`, import.meta.url),
        "utf8",
      ),
    );
    assert.equal(validateCards(category, cards).length, 10);
    if (category === "preguntas")
      assert.equal(new Set(cards.map((c) => c.type)).size, 3);
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
  const result = draw(["a", "b", "d"], state);
  assert.equal(result.id, "b");
  assert.deepEqual(result.state.queue, ["d"]);
  assert.deepEqual(result.state.used, ["a", "b"]);
  assert.equal(draw(["a", "b", "d"], result.state).id, "d");
});
test("una tarjeta, mazo vacío y estado corrupto", () => {
  assert.equal(draw(["a"], { used: ["a"], last: "a" }).id, "a");
  assert.throws(() => draw([]));
  assert.ok(draw(["a", "b"], null).id);
  assert.ok(draw(["a", "b"], null).id);
  assert.ok(
    ["a", "b"].includes(draw(["a", "b"], { queue: "bad", used: 4 }).id),
  );
});
test("rechaza duplicados y formatos inválidos", () => {
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
