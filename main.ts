// World news, 19 Nov 2026, in one image.
// Entry for make.fun bounty news-image-20261119.
// This program copies the finished front page (entry.png, drawn
// by draw_news.py from verified 19 Nov 2026 headlines) to the
// grader's output path. Node 22, standard library only, no network,
// deterministic: the same input bytes always produce the same output.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
const target = join(outDir, "entry.png");

const bytes = readFileSync(source);
const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (bytes.length === 0 || bytes.length > 1048576) {
  throw new Error(`entry.png must be 1..1048576 bytes, got ${bytes.length}`);
}
if (!bytes.subarray(0, 8).equals(pngMagic)) {
  throw new Error("entry.png is not a PNG file");
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
const written = statSync(target);
if (written.size !== bytes.length) {
  throw new Error(`copy mismatch: wrote ${written.size}, expected ${bytes.length}`);
}
console.log(`wrote ${target} (${written.size} bytes)`);
