# Otra ronda ✦

Tarjetas digitales para acompañar Party & Co Original con el tablero físico. React + TypeScript + Vite, sin backend. Cinco categorías, 1.500 tarjetas por categoría y respuestas siempre visibles. Aplicación independiente, sin afiliación con Diset.

## Desarrollo

Requiere Node.js 20.19+ o 22.12+.

```sh
npm install
npm run dev
```

Abre la dirección que indica Vite. Para probar desde un móvil en la misma red, usa la dirección de red. La instalación y el service worker requieren HTTPS o localhost; una IP de red por HTTP no permite probar toda la PWA.

## Verificación y producción

```sh
npm test
npm run build
npm run preview
```

`npm test` comprueba las 7.500 tarjetas, formatos, rondas sin repeticiones, persistencia serializada, cambios de contenido y datos inválidos. `npm run build` comprueba TypeScript y genera `dist/`, el manifiesto y el service worker. Prueba el modo offline sobre producción, no sobre el servidor de desarrollo.

## Despliegue estático

Sube el contenido de `dist/` a un alojamiento estático con HTTPS (por ejemplo, GitHub Pages, Netlify o Cloudflare Pages). El proyecto utiliza rutas relativas y no necesita servidor de aplicaciones ni variables secretas. Publica todo `dist/` en cada versión; evita cachear indefinidamente `index.html` y `sw.js`. El bundle contiene los JSON y cambia de hash al modificar las tarjetas.

En GitHub Pages puedes compilar con `npm ci && npm run build` y publicar `dist/` mediante el flujo oficial de Pages. No se ha activado ni modificado ningún alojamiento desde este proyecto.

## Añadir tarjetas

Edita `src/data/telepatia.json`, `mimica.json`, `preguntas.json`, `dibujos.json` o `prohibido.json`. Conserva los identificadores de tarjetas existentes y utiliza uno nuevo para cada tarjeta añadida. La cantidad puede crecer sin cambiar la interfaz. Los campos opcionales `difficulty` (`easy`, `medium`, `hard`) y `topic` indican dificultad orientativa y ámbito. Los cinco mazos mezclan dificultades y temas: acciones, personajes, animales y otros ámbitos según la mecánica.

Formato básico:

```json
{
  "id": "mimica-011",
  "prompt": "Un fotógrafo intentando reunir a una familia para una foto"
}
```

Preguntas abiertas o verdadero/falso:

```json
{
  "id": "preguntas-011",
  "prompt": "¿Cuántos lados tiene un hexágono?",
  "answer": "Seis",
  "type": "open"
}
```

Usa `type: "boolean"` para verdadero/falso. Las preguntas de tres opciones usan `type: "choice"` y un array `options` de exactamente tres textos diferentes; `answer` debe coincidir con uno de ellos. No hay interacción para responder: el móvil lo manejan quienes dirigen la prueba.

Prohibido:

```json
{
  "id": "prohibido-011",
  "prompt": "Brújula",
  "forbidden": ["Norte", "Sur", "Aguja", "Orientación"]
}
```

Se validan los datos al iniciar la aplicación. Los errores muestran una pantalla explicativa. Tras ampliar el contenido, adapta el número esperado en el test de contenido inicial de `tests/deck.test.mjs` y ejecuta test/build.

## Barajas y temporizador

Fisher–Yates mezcla las tarjetas. Cada categoría conserva su cola, los identificadores usados y el último mostrado en `localStorage` (`otra-ronda-decks-v1`). No hay repetición hasta agotar el mazo ni entre rondas (salvo una categoría con una sola tarjeta). Añadir o quitar tarjetas reconcilia los identificadores sin borrar innecesariamente el progreso. Si el almacenamiento está bloqueado, funciona en memoria y muestra un aviso.

El temporizador de 30 segundos es opcional, usa una fecha de finalización para evitar deriva al cambiar de pestaña y se destruye al cambiar de carta o pantalla. El aviso sonoro se prepara únicamente tras pulsar Iniciar; si el navegador lo bloquea, permanece el aviso visual.

## Instalación y offline

Android: el botón de instalación aparece cuando el navegador entrega `beforeinstallprompt`. iOS: muestra una guía para añadir a inicio; en otros navegadores indica usar Safari si no aparece la opción. Desaparece en modo standalone o tras `appinstalled`.

El service worker precachea la aplicación y sus tarjetas después de la primera carga de producción. Vuelve a abrirla sin Internet para comprobarlo. Una versión nueva muestra un aviso de actualización; se recarga cuando se pulsa Actualizar y conserva las barajas. Se comprueban actualizaciones al volver a la aplicación. El progreso depende del navegador y del origen: borrar sus datos o cambiar de dominio lo reinicia.

## Diseño y alcance

Diseño adaptable a móviles, tablets y pantallas grandes con áreas seguras, controles táctiles, movimiento reducido y contenido con desplazamiento vertical cuando hace falta. Reglas breves basadas en las dos páginas del manual facilitado. No incluye tablero, dados, turnos, puntuaciones ni pizarra digital. Las respuestas se muestran siempre siguiendo la aclaración del usuario.

## Ampliación editorial y procedencia

La versión actual contiene exactamente **7.500 tarjetas: 1.500 por categoría**. Los tests verifican cantidades, diversidad de ámbitos y dificultades en los cinco mazos, los ejemplos sencillos de Mímica, datos válidos y dos rondas completas de cada mazo con persistencia. También comprueban la alarma repetida y su parada. Las 50 cartas iniciales mantienen sus IDs y textos para conservar el progreso.

En Mímica hay más de 400 acciones cotidianas fáciles, además de animales, profesiones, películas, series, personajes, famosos y desafíos. Dibujos y Prohibido incluyen también acciones y escenas concretas. Telepatía combina temas abiertos de marcas, gastronomía, personajes, animales y planes. Las etiquetas de dificultad son orientativas y no cambian la aleatoriedad.

Las preguntas añadidas adaptan una selección de los bancos españoles de **[Quizify](https://github.com/mholzi/quizify)** (Markus Holzhäuser y colaboradores), bajo licencia MIT. Se conserva el snapshot `b0eac76d463940815ba01d32a805dca5f44f727c` y la referencia de archivo/ID en cada tarjeta adaptada. Se han excluido pruebas de imagen, estimaciones, respuestas dependientes de opciones y algunas referencias temporales; se han convertido registros a formatos abiertos y verdadero/falso. Se ha revisado la estructura y una muestra de contenido, no se afirma una comprobación documental individual de las 1.500 respuestas. Aviso y licencia: `public/content-notices.txt` y `public/quizify-license.txt`, incluidos en la distribución y en la caché offline.

Los bancos de conceptos y escenas se mantienen en `scripts/content/`. El generador opcional de mantenimiento requiere Python 3 y **no necesita Internet**:

```sh
python scripts/generate-content.py
```

Regenera todos los mazos desde esos bancos y `scripts/content/trivia-source.json`; si editas JSON a mano, guarda tus cambios antes de regenerar o introdúcelos primero en los bancos. `scripts/content/original.json` conserva las tarjetas iniciales. Los IDs añadidos se derivan del contenido normalizado; las tarjetas con el mismo texto mantienen la misma identidad al regenerar. El resumen de cantidades, temas, dificultades y formatos está en `scripts/content/report.json`.

La aplicación no ejecuta estos scripts ni consulta APIs durante una partida. Vite separa los cinco mazos en recursos estáticos que el service worker guarda junto con la interfaz. Así se evita concentrar todo el contenido en un único archivo grande.

Al pulsar **Otra tarjeta**, la carta sale, se retira del DOM y aparece la siguiente. El botón se bloquea durante esa transición y se cancela cualquier cambio pendiente si se abandona la pantalla. Con movimiento reducido, la sustitución es inmediata. El temporizador se detiene y se reinicia; se vuelve al comienzo de la carta para que el contenido nuevo quede visible.

Al llegar a cero, el temporizador reproduce una alarma fuerte de tonos alternos en bucle mediante Web Audio. Continúa hasta pulsar **Reiniciar** o cambiar de carta/salir de la prueba. No depende de repetir un intervalo de JavaScript para mantener el sonido. Su nivel final depende del volumen del dispositivo; el contexto de audio se activa al pulsar Iniciar.
