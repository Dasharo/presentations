import { defineConfig } from 'vite';
import MdItAdmon from 'markdown-it-admon';

export default defineConfig({
  server: {
    // make the dev server listen on all network interfaces
    host: true,              // or '0.0.0.0'
    // all hosts are allowed
    allowedHosts: true,
    fs: { strict: false },
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

