import {
  Brain,
  Star,
  CircleHelp,
  Pencil,
  MessageCircleWarning,
} from "lucide-react";
import telepatia from "../data/telepatia.json";
import mimica from "../data/mimica.json";
import preguntas from "../data/preguntas.json";
import dibujos from "../data/dibujos.json";
import prohibido from "../data/prohibido.json";
import { validateCards } from "./deck.mjs";
export type Card = {
  id: string;
  prompt: string;
  answer?: string;
  type?: string;
  options?: string[];
  forbidden?: string[];
  difficulty?: "easy" | "medium" | "hard";
  topic?: string;
};
export const categories = [
  {
    id: "telepatia",
    name: "Telepatía",
    tag: "En la misma onda",
    color: "#b99aff",
    Icon: Brain,
    rule: "Dos jugadores, un tema. A la cuenta de tres, decid una respuesta a la vez. ¡Tenéis que coincidir! No valen marcas blancas.",
    instruction: "Coincidid en…",
    cards: telepatia as Card[],
  },
  {
    id: "mimica",
    name: "Mímica",
    tag: "Que hable tu cuerpo",
    color: "#ffc75a",
    Icon: Star,
    rule: "Representa la prueba para tu equipo. Puedes hacer sonidos y onomatopeyas relacionados, pero no decir la respuesta.",
    instruction: "Representa…",
    cards: mimica as Card[],
  },
  {
    id: "preguntas",
    name: "Preguntas",
    tag: "Dale al coco",
    color: "#77c8ff",
    Icon: CircleHelp,
    rule: "Lee la pregunta sin enseñar la pantalla a quien responde. El equipo puede consultar, pero debe dar una única respuesta.",
    instruction: "La pregunta es…",
    cards: preguntas as Card[],
  },
  {
    id: "dibujos",
    name: "Dibujos",
    tag: "Un trazo, mil palabras",
    color: "#b0e578",
    Icon: Pencil,
    rule: "Dibuja en papel para que tu equipo lo adivine. No puedes hablar, hacer sonidos, gesticular ni escribir letras o números.",
    instruction: "Dibuja…",
    cards: dibujos as Card[],
  },
  {
    id: "prohibido",
    name: "Prohibido",
    tag: "Dilo sin decirlo",
    color: "#ff8fa7",
    Icon: MessageCircleWarning,
    rule: "Explica el concepto sin decir las cuatro palabras prohibidas, sus derivados, iniciales ni abreviaturas. Tampoco digas el concepto.",
    instruction: "Haz que adivinen…",
    cards: prohibido as Card[],
  },
];
export function validateCatalog() {
  categories.forEach((c) => validateCards(c.id, c.cards));
}
export type Category = (typeof categories)[number];
const KEY = "otra-ronda-decks-v1";
export function readDecks(): Record<string, any> {
  try {
    const value = JSON.parse(localStorage.getItem(KEY) || "{}");
    return value && typeof value === "object" && !Array.isArray(value)
      ? value
      : {};
  } catch {
    return {};
  }
}
export function saveDecks(decks: Record<string, any>) {
  try {
    localStorage.setItem(KEY, JSON.stringify(decks));
    return true;
  } catch {
    return false;
  }
}
