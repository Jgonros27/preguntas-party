import { useEffect, useRef, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  Download,
  Sparkles,
  X,
  Share,
} from "lucide-react";
import { registerSW } from "virtual:pwa-register";
import {
  categories,
  readDecks,
  saveDecks,
  validateCatalog,
  type Card,
  type Category,
} from "./lib/catalog";
import { draw } from "./lib/deck.mjs";
import CardView from "./components/CardView";
import "./style.css";

function Decoration() {
  return (
    <div className="decoration" aria-hidden="true">
      {categories.map((c, i) => (
        <span
          key={c.id}
          className={`float float-${i}`}
          style={{ color: c.color }}
        >
          <c.Icon strokeWidth={1.5} />
        </span>
      ))}
      <i className="confetti c1" />
      <i className="confetti c2" />
      <i className="confetti c3" />
      <i className="confetti c4" />
      <i className="confetti c5" />
    </div>
  );
}
function useInstall() {
  const [prompt, setPrompt] = useState<any>(null);
  const [installed, setInstalled] = useState(
    () =>
      matchMedia("(display-mode: standalone)").matches ||
      (navigator as any).standalone === true,
  );
  const ios =
    /iPad|iPhone|iPod/.test(navigator.userAgent) ||
    (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  useEffect(() => {
    const media = matchMedia("(display-mode: standalone)");
    const before = (event: Event) => {
      event.preventDefault();
      setPrompt(event);
    };
    const done = () => {
      setInstalled(true);
      setPrompt(null);
    };
    const change = () =>
      setInstalled(media.matches || (navigator as any).standalone === true);
    window.addEventListener("beforeinstallprompt", before);
    window.addEventListener("appinstalled", done);
    media.addEventListener("change", change);
    return () => {
      window.removeEventListener("beforeinstallprompt", before);
      window.removeEventListener("appinstalled", done);
      media.removeEventListener("change", change);
    };
  }, []);
  return {
    available: !installed && (ios || !!prompt),
    ios,
    install: async () => {
      if (prompt) {
        await prompt.prompt();
        await prompt.userChoice;
        setPrompt(null);
      }
    },
  };
}
export default function App() {
  const [screen, setScreen] = useState<"home" | "categories" | "card">("home");
  const [category, setCategory] = useState<Category>(categories[0]);
  const [card, setCard] = useState<Card | null>(null);
  const [sequence, setSequence] = useState(0);
  const [error, setError] = useState("");
  const [storageWarning, setStorageWarning] = useState(false);
  const [guide, setGuide] = useState(false);
  const [update, setUpdate] = useState(false);
  const updateSW = useRef<((reload?: boolean) => Promise<void>) | null>(null);
  const decks = useRef(readDecks());
  const install = useInstall();
  useEffect(() => {
    try {
      validateCatalog();
    } catch (err) {
      setError((err as Error).message);
    }
    updateSW.current = registerSW({
      onNeedRefresh() {
        setUpdate(true);
      },
      onRegisterError(err) {
        console.error("No se pudo activar el modo sin conexión", err);
      },
    });
    const check = () => {
      if (document.visibilityState === "visible")
        navigator.serviceWorker
          ?.getRegistration()
          .then((reg) => reg?.update())
          .catch(() => {});
    };
    document.addEventListener("visibilitychange", check);
    return () => document.removeEventListener("visibilitychange", check);
  }, []);
  useEffect(() => {
    window.scrollTo(0, 0);
    document.querySelector<HTMLElement>("main h1")?.focus();
  }, [screen]);
  useEffect(() => {
    const back = () => {
      setScreen((history.state?.screen as typeof screen) || "home");
    };
    history.replaceState({ screen: "home" }, "");
    window.addEventListener("popstate", back);
    return () => window.removeEventListener("popstate", back);
  }, []);
  function go(next: typeof screen) {
    history.pushState({ screen: next }, "");
    setScreen(next);
  }
  function next(c: Category) {
    try {
      const result = draw(
        c.cards.map((card) => card.id),
        decks.current[c.id],
      );
      decks.current[c.id] = result.state;
      setStorageWarning(!saveDecks(decks.current));
      setCategory(c);
      setCard(c.cards.find((card) => card.id === result.id)!);
      setSequence((s) => s + 1);
      if (screen !== "card") go("card");
    } catch (err) {
      setError((err as Error).message);
    }
  }
  return (
    <div className="app-shell">
      <Decoration />
      {error ? (
        <main className="screen error-screen">
          <h1>No hemos podido preparar las tarjetas</h1>
          <p>{error}</p>
          <button className="primary" onClick={() => location.reload()}>
            Volver a intentar
          </button>
        </main>
      ) : screen === "home" ? (
        <main className="screen home-screen">
          <div className="hero">
            <h1 tabIndex={-1}>
              otra
              <br />
              <span>
                ronda<span className="title-spark">✳</span>
              </span>
              <span className="title-dot">.</span>
            </h1>
            <p className="hero-subtitle">
              Las mejores partidas
              <br />
              <strong>nunca se repiten.</strong>
            </p>
            <div className="mini-deck" aria-hidden="true">
              {categories.map((c) => (
                <span
                  key={c.id}
                  style={{ "--tile": c.color } as React.CSSProperties}
                >
                  <c.Icon size={24} />
                </span>
              ))}
            </div>
          </div>
          <div className="home-actions">
            <button
              className="primary play-button"
              onClick={() => go("categories")}
            >
              ¡Jugar ahora! <ArrowRight size={23} />
            </button>
            {install.available && (
              <button
                className="install-button"
                onClick={() =>
                  install.ios
                    ? setGuide(true)
                    : void install
                        .install()
                        .catch(() =>
                          setError(
                            "No se pudo iniciar la instalación. Vuelve a intentarlo desde el menú del navegador.",
                          ),
                        )
                }
              >
                <Download size={17} /> Instalar aplicación
              </button>
            )}
            <p className="home-note">Un móvil. Tu gente. Mucho juego.</p>
          </div>
          <footer>
            <span>5 categorías</span>
            <i />
            <span>
              {categories
                .reduce((total, c) => total + c.cards.length, 0)
                .toLocaleString("es-ES")}{" "}
              retos
            </span>
            <i />
            <span>Cero complicaciones</span>
          </footer>
        </main>
      ) : screen === "categories" ? (
        <main className="screen category-screen">
          <header className="topbar">
            <button className="back-button" onClick={() => go("home")}>
              <ArrowLeft size={18} /> Inicio
            </button>
          </header>
          <div className="section-title">
            <h1 tabIndex={-1}>
              ¿Qué toca
              <br />
              <span>esta ronda?</span>
            </h1>
          </div>
          <div className="category-list">
            {categories.map((c, i) => (
              <button
                className="category-tile"
                key={c.id}
                style={
                  {
                    "--accent": c.color,
                    "--delay": `${i * 45}ms`,
                  } as React.CSSProperties
                }
                onClick={() => next(c)}
              >
                <span className="tile-icon">
                  <c.Icon size={30} strokeWidth={1.8} />
                </span>
                <span className="tile-copy">
                  <strong>{c.name}</strong>
                  <span>{c.tag}</span>
                </span>
                <ArrowRight size={22} />
                <span className="tile-ghost" aria-hidden="true">
                  <c.Icon size={93} />
                </span>
              </button>
            ))}
          </div>
        </main>
      ) : (
        card && (
          <CardView
            category={category}
            card={card}
            sequence={sequence}
            onNext={() => next(category)}
            onCategories={() => go("categories")}
            onHome={() => go("home")}
          />
        )
      )}{" "}
      {storageWarning && (
        <p className="storage-warning" role="status">
          El navegador no permite guardar el progreso. Las tarjetas no se
          repetirán durante esta sesión.
        </p>
      )}
      {update && (
        <div className="update-banner" role="status">
          <span>¡Hay una nueva ronda de novedades!</span>
          <button onClick={() => void updateSW.current?.(true)}>
            Actualizar
          </button>
          <button
            className="icon-button"
            onClick={() => setUpdate(false)}
            aria-label="Actualizar más tarde"
          >
            <X size={16} />
          </button>
        </div>
      )}
      {guide && (
        <div className="modal-backdrop" onClick={() => setGuide(false)}>
          <section
            className="install-guide"
            role="dialog"
            aria-modal="true"
            aria-labelledby="install-title"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              autoFocus
              className="icon-button close-guide"
              onClick={() => setGuide(false)}
              aria-label="Cerrar guía"
            >
              <X />
            </button>
            <span className="guide-icon">
              <Download size={30} />
            </span>
            <h2 id="install-title">La fiesta, a un toque.</h2>
            <p>Añade Otra ronda a tu pantalla de inicio.</p>
            <ol>
              <li>
                Abre el menú{" "}
                {/CriOS|FxiOS|EdgiOS/.test(navigator.userAgent)
                  ? "del navegador (⋯) y busca Compartir"
                  : "Compartir de Safari"}{" "}
                <Share size={17} />.
              </li>
              <li>
                Pulsa <strong>Añadir a pantalla de inicio</strong>. Si no
                aparece, abre esta página en Safari.
              </li>
              <li>
                Confirma con <strong>Añadir</strong> y abre el nuevo icono.
              </li>
            </ol>
            <p className="guide-note">
              Deja cargar la aplicación una vez con Internet para tener las
              tarjetas sin conexión.
            </p>
            <button className="primary" onClick={() => setGuide(false)}>
              ¡Entendido! <Check size={19} />
            </button>
          </section>
        </div>
      )}
    </div>
  );
}
