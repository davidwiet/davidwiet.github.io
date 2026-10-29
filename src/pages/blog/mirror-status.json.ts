import type { APIRoute } from 'astro';
import archive from '../../../content/blog/posts.json';

export const GET: APIRoute = () => new Response(JSON.stringify({
  schema_version: 1,
  processed_request: (archive as any).processed_request ?? null,
  posts: archive.posts.map((post) => ({
    id: post.id, source_url: post.source_url,
    mirror_url: `https://davidwiet.github.io/blog/${post.mirror_slug}/`,
    body_sha256: post.body_sha256,
  })),
}, null, 2), {headers: {'Content-Type': 'application/json'}});
