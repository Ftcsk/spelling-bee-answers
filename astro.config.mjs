import { defineConfig } from 'astro/config'
import tailwind from '@astrojs/tailwind'

export default defineConfig({
  site: 'https://spellingbeeanswers.xyz',
  integrations: [tailwind()],
  output: 'static',
})
