import type { APIRoute } from 'astro'
import { getAllAnswers } from '../lib/answers'

export const GET: APIRoute = () => {
  const base = 'https://spellingbeeanswers.xyz'
  const answers = getAllAnswers()

  const staticPages = ['', '/answers', '/hints', '/words', '/about']

  const datePages = answers.map(a => `/answers/${a.date}`)

  const wordPages = [...new Set(answers.flatMap(a => a.words.map(w => `/words/${w.word.toLowerCase()}`)))]

  const allUrls = [...staticPages, ...datePages, ...wordPages]

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allUrls.map(url => `  <url>
    <loc>${base}${url}</loc>
    <changefreq>${url === '' ? 'daily' : 'weekly'}</changefreq>
    <priority>${url === '' ? '1.0' : url.startsWith('/answers/202') ? '0.8' : '0.6'}</priority>
  </url>`).join('\n')}
</urlset>`

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml' }
  })
}
