import { useEffect, useRef, useState, type CSSProperties } from "react";
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
  const [phase, setPhase] = useState<"ready" | "leaving" | "hidden">("ready");
  const timers = useRef<number[]>([]);
  const switching = useRef(false);
  const heading = useRef<HTMLHeadingElement>(null);
  const stage = useRef<HTMLDivElement>(null);
  const [stageHeight, setStageHeight] = useState<number>();
  useEffect(() => () => timers.current.forEach(window.clearTimeout), []);
  useEffect(() => {
    heading.current?.focus({ preventScroll: true });
    window.scrollTo({ top: 0, behavior: "instant" });
  }, [sequence]);
  function replaceCard() {
    if (switching.current) return;
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
      onNext();
      return;
    }
    switching.current = true;
    setStageHeight(stage.current?.getBoundingClientRect().height);
    setPhase("leaving");
    timers.current = [
      window.setTimeout(() => {
        setPhase("hidden");
        timers.current.push(
          window.setTimeout(() => {
            onNext();
            setPhase("ready");
            switching.current = false;
          }, 70),
        );
      }, 160),
    ];
  }
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
      <div
        ref={stage}
        className="card-stage"
        aria-busy={phase !== "ready"}
        style={{ minHeight: phase === "ready" ? undefined : stageHeight }}
      >
        {phase !== "hidden" && (
          <article
            key={sequence}
            className={`playing-card ${phase === "leaving" ? "card-leaving" : ""}`}
          >
            <div className="card-top">
              <span className="card-category">
                <Icon size={22} />
                {category.name}
              </span>
              {card.difficulty && (
                <span className="difficulty-badge">
                  {
                    { easy: "Fácil", medium: "Media", hard: "Difícil" }[
                      card.difficulty
                    ]
                  }
                </span>
              )}
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
              <h1
                ref={heading}
                tabIndex={-1}
                className={card.prompt.length > 85 ? "long-prompt" : ""}
              >
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
        )}
      </div>
      <details className="rules">
        <summary>
          Cómo se juega <ChevronRight size={16} />
        </summary>
        <p>{category.rule}</p>
      </details>
      {phase === "ready" ? (
        <Countdown key={sequence} />
      ) : (
        <div className="timer-placeholder" aria-hidden="true" />
      )}
      <div className="card-actions">
        <button
          className="primary"
          onClick={replaceCard}
          disabled={phase !== "ready"}
        >
          <Shuffle size={20} /> Otra tarjeta <ArrowRight size={21} />
        </button>
        <button className="text-button" onClick={onCategories}>
          Cambiar categoría
        </button>
      </div>
    </main>
  );
}
