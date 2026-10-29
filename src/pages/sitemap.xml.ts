import type { APIRoute } from 'astro';
import { works } from '../data/works';

export const GET: APIRoute = ({site}) => {
  // Article copies identify Substack as canonical and are linked from /blog/.
  // Keep only this site's canonical pages in its sitemap.
  const paths = ['/', '/human-image/', '/blog/', ...works.map((work) => `/works/${work.slug}/`)];
  return new Response(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${paths.map((path) => `<url><loc>${new URL(path, site).href}</loc></url>`).join('')}</urlset>`, {headers: {'Content-Type': 'application/xml'}});
};
