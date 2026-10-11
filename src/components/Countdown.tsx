import { useEffect, useRef, useState } from "react";
import { Timer, RotateCcw } from "lucide-react";
import { startAlarm } from "../lib/alarm.mjs";
export default function Countdown() {
  const [remaining, setRemaining] = useState(30);
  const [running, setRunning] = useState(false);
  const deadline = useRef(0);
  const audio = useRef<AudioContext | null>(null);
  const alarm = useRef<(() => void) | null>(null);
  useEffect(() => {
    if (!running) return;
    const tick = () => {
      const next = Math.max(
        0,
        Math.ceil((deadline.current - Date.now()) / 1000),
      );
      setRemaining(next);
      if (next === 0) {
        setRunning(false);
      }
    };
    tick();
    const id = window.setInterval(tick, 100);
    return () => clearInterval(id);
  }, [running]);
  useEffect(() => {
    if (remaining !== 0) return;
    try {
      if (audio.current) alarm.current = startAlarm(audio.current);
    } catch {}
    return () => {
      alarm.current?.();
      alarm.current = null;
    };
  }, [remaining]);
  useEffect(
    () => () => {
      alarm.current?.();
      alarm.current = null;
      void audio.current?.close().catch(() => {});
    },
    [],
  );
  function start() {
    try {
      audio.current ??= new AudioContext();
      void audio.current.resume().catch(() => {});
    } catch {}
    deadline.current = Date.now() + remaining * 1000;
    setRunning(true);
  }
  function reset() {
    alarm.current?.();
    alarm.current = null;
    setRunning(false);
    setRemaining(30);
  }
  return (
    <section
      className={`timer-panel ${remaining === 0 ? "expired" : ""}`}
      aria-label="Temporizador opcional"
    >
      <div
        className="timer-dial"
        style={
          { "--progress": `${(remaining / 30) * 100}%` } as React.CSSProperties
        }
      >
        <span>
          {remaining}
          <small>s</small>
        </span>
      </div>
      <div className="timer-copy">
        <strong>
          {remaining === 0
            ? "¡Tiempo!"
            : running
              ? "¡Vamos, vamos!"
              : "A vuestro ritmo"}
        </strong>
        <span>
          {remaining === 0
            ? "Pulsa Reiniciar para detener la alarma"
            : running
              ? "El reloj está en marcha"
              : "30 segundos · temporizador opcional"}
        </span>
      </div>
      {!running && remaining > 0 ? (
        <button
          className="timer-start"
          onClick={start}
          aria-label="Iniciar temporizador"
        >
          <Timer size={18} /> Iniciar
        </button>
      ) : (
        <button
          className="timer-start"
          onClick={reset}
          aria-label="Reiniciar temporizador"
        >
          <RotateCcw size={19} />
          {remaining === 0 && "Reiniciar"}
        </button>
      )}
      {!running && remaining !== 30 && remaining > 0 && (
        <button
          className="icon-button"
          onClick={reset}
          aria-label="Reiniciar temporizador"
        >
          <RotateCcw size={17} />
        </button>
      )}
      <span className="sr-only" role="status">
        {remaining === 0 ? "Tiempo agotado" : ""}
      </span>
    </section>
  );
}
