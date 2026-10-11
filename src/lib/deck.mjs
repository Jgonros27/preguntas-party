export function shuffle(ids, random = Math.random) {
  const result = [...ids];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}
export function draw(ids, saved = {}, random = Math.random) {
  saved = saved && typeof saved === "object" ? saved : {};
  if (!ids.length) throw new Error("Esta categoría no tiene tarjetas.");
  const valid = new Set(ids);
  const used = new Set(
    Array.isArray(saved.used) ? saved.used.filter((id) => valid.has(id)) : [],
  );
  let queue = Array.isArray(saved.queue)
    ? [...new Set(saved.queue.filter((id) => valid.has(id) && !used.has(id)))]
    : [];
  const known = new Set(queue);
  queue.push(
    ...shuffle(
      ids.filter((id) => !used.has(id) && !known.has(id)),
      random,
    ),
  );
  if (!queue.length) {
    used.clear();
    queue = shuffle(ids, random);
  }
  if (queue.length > 1 && queue[0] === saved.last) {
    const swap = 1 + Math.floor(random() * (queue.length - 1));
    [queue[0], queue[swap]] = [queue[swap], queue[0]];
  }
  const id = queue.shift();
  used.add(id);
  return { id, state: { queue, used: [...used], last: id } };
}
export function validateCards(category, cards) {
  if (!Array.isArray(cards) || !cards.length)
    throw new Error(category + ": no hay tarjetas.");
  const seen = new Set();
  for (const card of cards) {
    if (typeof card.id !== "string" || !card.id.trim() || seen.has(card.id))
      throw new Error(category + ": identificador inválido o duplicado.");
    seen.add(card.id);
    if (typeof card.prompt !== "string" || !card.prompt.trim())
      throw new Error(category + ": falta el texto.");
    if (category === "preguntas") {
      if (
        typeof card.answer !== "string" ||
        !card.answer.trim() ||
        !["open", "boolean", "choice"].includes(card.type)
      )
        throw new Error("Pregunta inválida.");
      if (
        card.type === "choice" &&
        (!Array.isArray(card.options) ||
          card.options.length !== 3 ||
          card.options.some(
            (option) => typeof option !== "string" || !option.trim(),
          ) ||
          new Set(card.options).size !== 3 ||
          !card.options.includes(card.answer))
      )
        throw new Error("Opciones inválidas.");
    }
    if (
      category === "prohibido" &&
      (!Array.isArray(card.forbidden) ||
        card.forbidden.length !== 4 ||
        new Set(card.forbidden.map((w) => w.toLowerCase())).size !== 4 ||
        card.forbidden.some((w) => typeof w !== "string" || !w.trim()))
    )
      throw new Error("Se requieren cuatro palabras prohibidas diferentes.");
  }
  return cards;
}
