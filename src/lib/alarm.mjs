// Bucle de audio nativo: continúa aunque el navegador ralentice los temporizadores JS.
// Cuatro pulsos con tonos alternos y armónicos producen un timbre de alarma claro.
export function createAlarmSamples(sampleRate) {
  const samples = new Float32Array(Math.round(sampleRate * 1.35));
  const pulses = [
    [0, 0.23, 880],
    [0.3, 0.53, 1320],
    [0.6, 0.83, 880],
    [0.9, 1.13, 1320],
  ];
  for (const [start, end, frequency] of pulses) {
    for (
      let i = Math.ceil(start * sampleRate);
      i < Math.floor(end * sampleRate);
      i++
    ) {
      const time = i / sampleRate;
      const envelope = Math.min(
        1,
        (time - start) / 0.008,
        (end - time) / 0.015,
      );
      const phase = 2 * Math.PI * frequency * (time - start);
      samples[i] =
        (0.85 *
          envelope *
          (Math.sin(phase) +
            0.3 * Math.sin(3 * phase) +
            0.12 * Math.sin(5 * phase))) /
        1.42;
    }
  }
  return samples;
}

export function startAlarm(context) {
  const samples = createAlarmSamples(context.sampleRate);
  const buffer = context.createBuffer(1, samples.length, context.sampleRate);
  buffer.copyToChannel(samples, 0);
  const source = context.createBufferSource();
  source.buffer = buffer;
  source.loop = true;
  source.connect(context.destination);
  source.start();
  let stopped = false;
  return () => {
    if (stopped) return;
    stopped = true;
    source.stop();
    source.disconnect();
  };
}
