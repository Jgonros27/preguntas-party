import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";
export default defineConfig({
  base: "./",
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          const deck = id.match(/\/src\/data\/([^/]+)\.json$/);
          if (deck) return `cards-${deck[1]}`;
        },
      },
    },
  },
  plugins: [
    react(),
    VitePWA({
      registerType: "prompt",
      includeAssets: [
        "icon.svg",
        "apple-touch-icon.png",
        "quizify-license.txt",
        "content-notices.txt",
      ],
      manifest: {
        name: "Otra ronda · Tarjetas de fiesta",
        short_name: "Otra ronda",
        description: "Tarjetas para acompañar tu juego de mesa.",
        lang: "es",
        theme_color: "#171329",
        background_color: "#171329",
        display: "standalone",
        start_url: "./",
        scope: "./",
        icons: [
          { src: "icon-192.png", sizes: "192x192", type: "image/png" },
          { src: "icon-512.png", sizes: "512x512", type: "image/png" },
          {
            src: "icon-maskable.png",
            sizes: "512x512",
            type: "image/png",
            purpose: "maskable",
          },
        ],
      },
      workbox: {
        globPatterns: ["**/*.{js,css,html,png,svg,woff2}"],
        navigateFallback: "index.html",
        cleanupOutdatedCaches: true,
      },
    }),
  ],
});
