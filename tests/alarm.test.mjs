import test from "node:test";
import assert from "node:assert/strict";
import { createAlarmSamples, startAlarm } from "../src/lib/alarm.mjs";

test("la alarma genera cuatro pulsos fuertes con dos tonos alternos", () => {
  const rate = 48000;
  const samples = createAlarmSamples(rate);
  assert.equal(samples.length, Math.round(rate * 1.35));
  for (const start of [0, 0.3, 0.6, 0.9]) {
    const pulse = samples.slice(
      Math.round((start + 0.02) * rate),
      Math.round((start + 0.2) * rate),
    );
    const rms = Math.sqrt(
      pulse.reduce((sum, value) => sum + value * value, 0) / pulse.length,
    );
    assert.ok(rms > 0.4, `pulso a ${start}s demasiado suave: ${rms}`);
  }
  assert.equal(samples[0], 0);
  assert.equal(samples.at(-1), 0);
  assert.ok(
    samples.every((value) => Math.abs(value) <= 1 && Number.isFinite(value)),
  );
});

test("se repite en el motor de audio sin detenerse por sí sola y se libera al reiniciar", () => {
  let starts = 0,
    stops = 0,
    disconnects = 0;
  let storedSamples;
  const source = {
    loop: false,
    connect(destination) {
      assert.equal(destination, "speaker");
    },
    start() {
      starts++;
    },
    stop() {
      stops++;
    },
    disconnect() {
      disconnects++;
    },
  };
  const context = {
    sampleRate: 44100,
    destination: "speaker",
    createBuffer(channels, frames, rate) {
      assert.equal(channels, 1);
      assert.equal(rate, 44100);
      return {
        copyToChannel(samples, channel) {
          assert.equal(channel, 0);
          assert.equal(samples.length, frames);
          storedSamples = samples;
        },
      };
    },
    createBufferSource() {
      return source;
    },
  };
  const stop = startAlarm(context);
  assert.equal(source.loop, true);
  assert.equal(starts, 1);
  assert.equal(stops, 0);
  assert.ok(storedSamples.length > context.sampleRate);
  stop();
  stop();
  assert.equal(stops, 1);
  assert.equal(disconnects, 1);
});
