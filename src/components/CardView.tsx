import type { CSSProperties } from "react";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  ChevronRight,
  House,
  Shuffle,
  X,
} from "lucide-react";
import type { Card, Category } from "../lib/catalog";
import Countdown from "./Countdown";
export default function CardView({
  category,
  card,
  sequence,
  onNext,
  onCategories,
  onHome,
}: {
  category: Category;
  card: Card;
  sequence: number;
  onNext: () => void;
  onCategories: () => void;
  onHome: () => void;
}) {
  const Icon = category.Icon;
  return (
    <main
      className="screen card-screen"
      style={{ "--accent": category.color } as CSSProperties}
    >
      <header className="topbar">
        <button className="back-button" onClick={onCategories}>
          <ArrowLeft size={18} /> Categorías
        </button>
        <button
          className="icon-button"
          onClick={onHome}
          aria-label="Ir al inicio"
        >
          <House size={21} />
        </button>
      </header>
      <div className="card-heading">
        <span className="eyebrow">EL RETO ESTÁ SERVIDO</span>
        <span className="small-dot" /> <span>¡Que siga la ronda!</span>
      </div>
      <article key={sequence} className="playing-card">
        <div className="card-top">
          <span className="card-category">
            <Icon size={22} />
            {category.name}
          </span>
          <span className="card-number">
            OTRA
            <br />
            RONDA ✦
          </span>
        </div>
        <div className="card-body">
          <div className="card-emblem">
            <Icon size={43} strokeWidth={1.7} />
          </div>
          <p className="card-instruction">{category.instruction}</p>
          <h1 className={card.prompt.length > 85 ? "long-prompt" : ""}>
            {card.prompt}
          </h1>
          {card.options && (
            <ol className="options">
              {card.options.map((option, i) => (
                <li key={option}>
                  <span>{String.fromCharCode(65 + i)}</span>
                  {option}
                </li>
              ))}
            </ol>
          )}
          {card.type === "boolean" && (
            <div className="boolean-options">
              <span>Verdadero</span>
              <span>Falso</span>
            </div>
          )}
          {card.answer && (
            <div className="answer">
              <span>
                <Check size={15} /> RESPUESTA CORRECTA
              </span>
              <strong>{card.answer}</strong>
            </div>
          )}
          {card.forbidden && (
            <div className="forbidden">
              <p>
                <X size={15} /> NO PUEDES DECIR
              </p>
              <div>
                {card.forbidden.map((word) => (
                  <span key={word}>{word}</span>
                ))}
              </div>
            </div>
          )}
        </div>
        <div className="card-bottom">
          <span>✦</span>
          <p>
            {category.id === "telepatia"
              ? "Dos mentes. Una respuesta."
              : "La pantalla es para quien dirige la prueba."}
          </p>
          <span>✦</span>
        </div>
      </article>
      <details className="rules">
        <summary>
          Cómo se juega <ChevronRight size={16} />
        </summary>
        <p>{category.rule}</p>
      </details>
      <Countdown key={sequence} />
      <div className="card-actions">
        <button className="primary" onClick={onNext}>
          <Shuffle size={20} /> Otra tarjeta <ArrowRight size={21} />
        </button>
        <button className="text-button" onClick={onCategories}>
          Cambiar categoría
        </button>
      </div>
    </main>
  );
}
