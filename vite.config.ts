import { defineConfig } from 'vite';
import MdItAdmon from 'markdown-it-admon';

export default defineConfig({
  server: {
    // make the dev server listen on all network interfaces
    host: true,              // or '0.0.0.0'
    // all hosts are allowed
    allowedHosts: true,
    fs: { strict: false },
    hmr: {
      overlay: false,
    },
    watch: {
      usePolling: false,
      interval: 1000,
      ignored: ['**/slides/tools/**', '**/slides/slidev-template/**'],
    },
  },
  build: {
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor';
          }
        }
      }
    }
  },
  optimizeDeps: {
    exclude: ['@slidev/cli'],
  },
  slidev: {
    vue: {
      /* vue options */
    },
    markdown: {
      /* markdown-it options */
      markdownItSetup(md) {
        /* custom markdown-it plugins */
        md.use(MdItAdmon);
      },
    },
  },
});
