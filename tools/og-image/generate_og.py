#!/usr/bin/env python3
"""
generate_og.py — generate a 1200x630 Open Graph share-card image for a blog post.

USAGE
    python generate_og.py <slug>
    e.g. python generate_og.py validating-lukra

WHAT IT DOES
    1. Reads content/blog/<slug>.md and pulls out the same fields head.html
       uses for the OG card (ogTitle -> title, eyebrow, ogDescription -> stand),
       so the generated image always matches what's actually live on the page.
    2. Fills in tools/og-image/template.html (kept as its own file so visual
       tweaks don't require touching this script) with that text and the
       logo SVG.
    3. Renders it in headless Chromium via Playwright and screenshots at 2x
       scale for crisp text, then downsamples to the exact 1200x630 OG spec
       size with Pillow.
    4. Writes the result to themes/lukra/static/images/og/<slug>.png —
       exactly where head.html's og:image tag already expects it.

PREREQUISITES (one-time setup on whatever machine runs this)
    pip install playwright pillow --break-system-packages
    playwright install chromium

NOTE ON FRONT MATTER PARSING
    This is a deliberately minimal parser for Hugo's flat key: value front
    matter — it does NOT handle multi-line values, nested YAML, or lists.
    All fields this script reads are single-line strings, so that's fine
    for now. If a future post needs something more complex, swap in
    PyYAML rather than extending this by hand.
"""

import sys
import html
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit(
        "Playwright not installed. Run:\n"
        "    pip install playwright pillow --break-system-packages\n"
        "    playwright install chromium"
    )
try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow not installed. Run: pip install pillow --break-system-packages")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
CONTENT_DIR = REPO_ROOT / "content" / "blog"
OUTPUT_DIR = REPO_ROOT / "themes" / "lukra" / "static" / "images" / "og"


def parse_front_matter(md_path: Path) -> dict:
    """Minimal flat key: value front matter parser — see module docstring
    for why this doesn't use a full YAML library."""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        sys.exit(f"{md_path} has no front matter block (expected leading ---)")
    _, fm_block, _ = text.split("---", 2)

    fields = {}
    for line in fm_block.strip().splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        # Strip one layer of wrapping quotes, e.g.  seoTitle: "..."
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        fields[key] = value
    return fields


def build_card_html(fields: dict) -> str:
    template = (SCRIPT_DIR / "template.html").read_text(encoding="utf-8")
    logo_svg = (SCRIPT_DIR / "logo.svg").read_text(encoding="utf-8")

    # Same fallback order as head.html: prefer the OG-specific field, fall
    # back to the on-page field, so the card always matches what the live
    # page would actually show for og:title / og:description.
    title = fields.get("ogTitle") or fields.get("title", "")
    eyebrow = fields.get("eyebrow", "")
    stand = fields.get("ogDescription") or fields.get("stand", "")

    out = template.replace("__LOGO_SVG__", logo_svg)
    out = out.replace("__EYEBROW__", html.escape(eyebrow))
    out = out.replace("__TITLE__", html.escape(title))
    out = out.replace("__STAND__", html.escape(stand))
    return out


def render_png(card_html: str, out_path: Path) -> None:
    # Render into the same directory as template.html so the relative
    # fonts/... @font-face paths resolve correctly under file://.
    tmp_html = SCRIPT_DIR / "_render_tmp.html"
    tmp_html.write_text(card_html, encoding="utf-8")

    raw_png = SCRIPT_DIR / "_render_tmp.png"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        page.goto(tmp_html.as_uri())
        page.wait_for_timeout(200)  # let local @font-face finish loading
        page.screenshot(path=str(raw_png))
        browser.close()

    # Downsample from the 2x capture to the exact 1200x630 OG spec size.
    im = Image.open(raw_png).convert("RGB")
    im = im.resize((1200, 630), Image.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.save(out_path, "PNG", optimize=True)

    tmp_html.unlink()
    raw_png.unlink()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python generate_og.py <slug>")
    slug = sys.argv[1]

    md_path = CONTENT_DIR / f"{slug}.md"
    if not md_path.exists():
        sys.exit(f"No such post: {md_path}")

    fields = parse_front_matter(md_path)
    card_html = build_card_html(fields)

    out_path = OUTPUT_DIR / f"{slug}.png"
    render_png(card_html, out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
