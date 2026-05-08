#!/usr/bin/env python3
"""
build-html-docs.py — Convert every Markdown file in the sunscreen-filters
project to a static HTML file alongside it, using a consistent template
that matches the atlas styling (see /webapp/md.html).

Usage:
    python3 scripts/build-html-docs.py            # build all .md -> .html
    python3 scripts/build-html-docs.py --clean    # remove generated .html files

The script walks the project root (the parent of /scripts), renders each
.md to .html beside it, rewrites internal [text](foo.md) links so they
point at the corresponding .html, and wraps the output in an Atlas-style
template (Inter + JetBrains Mono, auto/light/dark theme toggle, AI GEN
pill, header with back-link to the atlas, footer with raw-source link).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import markdown  # type: ignore
    HAVE_MARKDOWN = True
except ImportError:
    HAVE_MARKDOWN = False


PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directories that should NOT be walked when collecting source markdown.
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


# ---------------------------------------------------------------------------
# CSS — copied verbatim from /webapp/md.html so the rendered docs match the
# live viewer (same fonts, color tokens, code blocks, tables, blockquotes,
# auto / light / dark theme support).
# ---------------------------------------------------------------------------
CSS = r"""
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg: #f8f6f1; --bg-2: #ffffff; --ink: #15121b; --ink-soft: #2d2735;
  --muted: #6b6473; --rule: #1a1620; --line: #d8d3cb; --line-soft: #e9e4dc;
  --accent: #6b1f6e; --accent-soft: #f4e8f4;
  --warn: #b94a3c; --warn-soft: #f7e7e3;
  --ok: #2d6b3f; --ok-soft: #e3efe6;
  --serif: 'Inter', -apple-system, system-ui, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg: #0f0d14; --bg-2: #16131b; --ink: #efeae0; --ink-soft: #d4cdbf;
    --muted: #948b9a; --rule: #efeae0; --line: #2d2737; --line-soft: #1f1b27;
    --accent: #d6a4d8; --accent-soft: #2c1d2e;
    --warn: #e8806f; --warn-soft: #36211d;
    --ok: #87c697; --ok-soft: #1d2c22;
  }
}
:root[data-theme="dark"]{
  --bg: #0f0d14; --bg-2:#16131b; --ink:#efeae0; --ink-soft:#d4cdbf;
  --muted:#948b9a; --rule:#efeae0; --line:#2d2737; --line-soft:#1f1b27;
  --accent:#d6a4d8; --accent-soft:#2c1d2e; --warn:#e8806f; --warn-soft:#36211d;
  --ok:#87c697; --ok-soft:#1d2c22;
}
html{ scroll-behavior:smooth }
body{
  font-family: var(--serif); background: var(--bg); color: var(--ink);
  line-height: 1.65; -webkit-font-smoothing: antialiased;
}
.container{ max-width: 880px; margin: 0 auto; padding: 0 32px }
.topbar{
  display:grid; grid-template-columns: 1fr auto 1fr;
  align-items:center; gap: 24px;
  padding: 20px 0; margin-top: 8px;
  border-bottom: 1.5px solid var(--rule);
  font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.6px;
  color: var(--muted);
}
.topbar-mid{ text-align:center; font-weight:500; color: var(--ink-soft) }
.topbar-right{ text-align:right; display:flex; gap:12px; justify-content:flex-end; align-items:center }
.back{ color: var(--accent); text-decoration:none }
.back:hover{ text-decoration:underline }
.theme-toggle{
  background:none; border:1px solid var(--line); color: var(--ink-soft);
  padding: 4px 10px; border-radius: 999px; cursor: pointer;
  font: inherit; font-size: 0.68rem; letter-spacing: 1.4px; text-transform: uppercase;
}
.raw-link{ color: var(--accent); text-decoration:none }
.raw-link:hover{ text-decoration:underline }

article#content{ padding: 50px 0 80px; max-width: 75ch }
article#content h1{
  font-size: clamp(1.9rem, 4vw, 2.6rem); font-weight: 800;
  line-height: 1.15; letter-spacing: -0.01em;
  margin-bottom: 24px;
}
article#content h2{
  font-size: 1.4rem; font-weight: 700; margin: 36px 0 12px;
  padding-bottom: 6px; border-bottom: 1px solid var(--line);
}
article#content h3{ font-size: 1.1rem; font-weight: 700; margin: 24px 0 8px }
article#content h4{ font: 700 0.78rem var(--mono); color: var(--muted); text-transform: uppercase; letter-spacing: 1.4px; margin: 18px 0 8px }
article#content p{ margin: 12px 0; color: var(--ink-soft); max-width: 75ch }
article#content strong{ color: var(--ink); font-weight: 600 }
article#content em{ color: var(--accent); font-style: italic }
article#content a{ color: var(--accent); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 2px }
article#content a:hover{ color: var(--ink) }
article#content ul, article#content ol{ margin: 12px 0; padding-left: 24px; color: var(--ink-soft) }
article#content li{ margin: 4px 0 }
article#content code{ font: 500 0.88em var(--mono); background: var(--bg-2); padding: 1px 6px; border-radius: 3px; color: var(--accent); border: 1px solid var(--line-soft) }
article#content pre{ background: var(--bg-2); border: 1px solid var(--line); border-radius: 4px; padding: 16px; overflow-x: auto; margin: 16px 0 }
article#content pre code{ background: none; border: none; padding: 0; color: var(--ink-soft); font-size: 0.85rem }
article#content blockquote{
  border-left: 3px solid var(--accent); padding: 4px 16px;
  margin: 16px 0; color: var(--muted); font-style: italic;
}
article#content table{
  width: 100%; border-collapse: collapse; margin: 16px 0;
  font-size: 0.92rem; background: var(--bg-2);
  border: 1px solid var(--line); border-radius: 4px; overflow: hidden;
}
article#content th, article#content td{
  text-align: left; padding: 10px 14px;
  border-bottom: 1px solid var(--line-soft); vertical-align: top;
}
article#content th{
  font: 700 0.72rem var(--mono); text-transform: uppercase; letter-spacing: 1px;
  color: var(--muted); border-bottom: 1.5px solid var(--rule);
  background: var(--bg);
}
article#content tr:hover{ background: var(--accent-soft) }
article#content hr{ border: none; border-top: 1.5px solid var(--rule); margin: 32px 0 }

.doc-meta{
  font: 500 0.78rem var(--mono); color: var(--muted);
  padding: 14px 0; border-bottom: 1px dashed var(--line);
  margin-bottom: 28px;
}
.doc-meta a{ color: var(--accent) }
footer{
  padding: 24px 0; border-top: 1.5px solid var(--rule);
  font: 500 0.7rem var(--mono); color: var(--muted);
  text-transform: uppercase; letter-spacing: 1.4px;
}
footer a{ color: var(--accent); text-decoration: none }
footer a:hover{ text-decoration:underline }
"""


# Theme-toggle JS — same auto/light/dark cycle as md.html.
THEME_JS = r"""
const modes = ['auto','light','dark'];
const labels = { auto: 'Auto', light: 'Light', dark: 'Dark' };
let modeIndex = modes.indexOf(localStorage.getItem('theme') || 'auto');
if (modeIndex < 0) modeIndex = 0;
const tbtn = document.getElementById('themeToggle');
function applyTheme(){
  const m = modes[modeIndex];
  localStorage.setItem('theme', m);
  if (m === 'auto') document.documentElement.removeAttribute('data-theme');
  else document.documentElement.setAttribute('data-theme', m);
  if (tbtn) tbtn.textContent = labels[m];
}
if (tbtn) tbtn.addEventListener('click', () => {
  modeIndex = (modeIndex + 1) % modes.length; applyTheme();
});
applyTheme();
"""


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — UV Filter Atlas</title>
<meta name="color-scheme" content="light dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<div class="container">
  <div class="topbar">
    <span><a class="back" href="{atlas_href}">← Atlas</a></span>
    <span class="topbar-mid">{title}</span>
    <span class="topbar-right">
      <a class="raw-link" href="{raw_href}">View raw markdown</a>
      <button class="theme-toggle" id="themeToggle" aria-label="Cycle theme">Auto</button>
    </span>
  </div>

  <article id="content">
    <div class="doc-meta">\U0001F4C4 <a href="{raw_href}">View raw markdown</a> · Path: <code>{rel_path}</code></div>
{body}
  </article>

  <footer>
    <span>UV Filter Atlas · <code>{rel_path}</code> · <a href="{raw_href}">raw .md</a></span>
  </footer>
</div>

<div style="position:fixed;top:10px;right:10px;background:rgba(0,0,0,0.45);color:rgba(255,255,255,0.7);font-size:9px;padding:2px 7px;border-radius:8px;z-index:9999;font-family:system-ui,-apple-system,sans-serif;pointer-events:none;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);letter-spacing:0.3px;text-transform:uppercase;font-weight:500;">ai gen</div>

<script>{js}</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Markdown collection
# ---------------------------------------------------------------------------
def collect_markdown(root: Path) -> list[Path]:
    out: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # mutate dirnames in-place to skip irrelevant trees
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                out.append(Path(dirpath) / fn)
    return sorted(out)


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------
def render_markdown(text: str) -> str:
    """Render markdown to HTML using python-markdown if available, else a
    minimal but reasonable fallback covering headings, paragraphs, lists,
    code, blockquotes, and tables."""
    if HAVE_MARKDOWN:
        md = markdown.Markdown(
            extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
            output_format="html5",
        )
        return md.convert(text)
    return _fallback_render(text)


def _fallback_render(text: str) -> str:
    """Tiny markdown subset for graceful degradation when python-markdown
    is not installed. Handles ATX headings, fenced code, paragraphs, links,
    inline code, bold/italic, ul/ol, blockquotes, hr, tables."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_lang = ""
    code_buf: list[str] = []

    def inline(s: str) -> str:
        # escape HTML first, then re-introduce intentional formatting
        s = (s.replace("&", "&amp;")
              .replace("<", "&lt;")
              .replace(">", "&gt;"))
        # inline code
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        # bold / italic
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        # links
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                   lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
        return s

    def flush_paragraph(buf: list[str]) -> None:
        if not buf:
            return
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
        buf.clear()

    para: list[str] = []

    while i < len(lines):
        line = lines[i]
        if in_code:
            if line.startswith("```"):
                out.append(f'<pre><code class="language-{code_lang}">'
                           + "\n".join(s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") for s in code_buf)
                           + "</code></pre>")
                code_buf.clear()
                code_lang = ""
                in_code = False
            else:
                code_buf.append(line)
            i += 1
            continue

        if line.startswith("```"):
            flush_paragraph(para)
            in_code = True
            code_lang = line[3:].strip()
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_paragraph(para)
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if re.match(r"^---+\s*$", line) or re.match(r"^\*\*\*+\s*$", line):
            flush_paragraph(para)
            out.append("<hr>")
            i += 1
            continue

        if line.startswith(">"):
            flush_paragraph(para)
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue

        if re.match(r"^\s*[-*+]\s+", line):
            flush_paragraph(para)
            out.append("<ul>")
            while i < len(lines) and re.match(r"^\s*[-*+]\s+", lines[i]):
                item = re.sub(r"^\s*[-*+]\s+", "", lines[i])
                out.append("<li>" + inline(item) + "</li>")
                i += 1
            out.append("</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            flush_paragraph(para)
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                out.append("<li>" + inline(item) + "</li>")
                i += 1
            out.append("</ol>")
            continue

        # rudimentary table support
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[-: |]+\|?\s*$", lines[i + 1]):
            flush_paragraph(para)
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i]:
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            tbl = ["<table><thead><tr>"]
            tbl += [f"<th>{inline(h)}</th>" for h in header]
            tbl.append("</tr></thead><tbody>")
            for r in rows:
                tbl.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            tbl.append("</tbody></table>")
            out.append("".join(tbl))
            continue

        if line.strip() == "":
            flush_paragraph(para)
        else:
            para.append(line)
        i += 1

    flush_paragraph(para)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Post-processing: rewrite *.md -> *.html in href attributes (not http(s)),
# preserving fragments and query strings. Operates on rendered HTML so we
# match the markdown library's output exactly.
# ---------------------------------------------------------------------------
HREF_RE = re.compile(r'href="([^"]+)"')


def rewrite_md_links(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
            return m.group(0)
        # split off fragment / query
        frag = ""
        query = ""
        target = href
        if "#" in target:
            target, frag = target.split("#", 1)
            frag = "#" + frag
        if "?" in target:
            target, query = target.split("?", 1)
            query = "?" + query
        if target.endswith(".md"):
            target = target[:-3] + ".html"
            return f'href="{target}{query}{frag}"'
        return m.group(0)
    return HREF_RE.sub(repl, html)


# ---------------------------------------------------------------------------
# Title extraction
# ---------------------------------------------------------------------------
H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)


def extract_title(text: str, fallback: str) -> str:
    m = H1_RE.search(text)
    if m:
        # strip any trailing markdown formatting
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return fallback


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------
def relative_to_root(p: Path) -> str:
    return str(p.relative_to(PROJECT_ROOT)).replace(os.sep, "/")


def atlas_href_for(md_path: Path) -> str:
    """Relative path to /webapp/index.html from the directory containing md_path."""
    md_dir = md_path.parent
    target = PROJECT_ROOT / "webapp" / "index.html"
    return os.path.relpath(target, md_dir).replace(os.sep, "/")


def html_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


# ---------------------------------------------------------------------------
# Build / clean
# ---------------------------------------------------------------------------
def build_one(md_path: Path) -> tuple[bool, str | None]:
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return False, f"read error: {e}"

    title = extract_title(text, md_path.stem)
    rel = relative_to_root(md_path)

    try:
        body_html = render_markdown(text)
    except Exception as e:  # noqa: BLE001
        return False, f"render error: {e}"

    body_html = rewrite_md_links(body_html)

    raw_href = md_path.name  # raw .md sits next to the .html
    page = HTML_TEMPLATE.format(
        title=html_escape(title),
        css=CSS,
        js=THEME_JS,
        atlas_href=html_escape(atlas_href_for(md_path)),
        raw_href=html_escape(raw_href),
        rel_path=html_escape(rel),
        body=body_html,
    )

    out_path = md_path.with_suffix(".html")
    try:
        out_path.write_text(page, encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return False, f"write error: {e}"
    return True, None


def clean(root: Path) -> int:
    removed = 0
    for md_path in collect_markdown(root):
        html_path = md_path.with_suffix(".html")
        if html_path.exists():
            try:
                html_path.unlink()
                removed += 1
            except Exception as e:  # noqa: BLE001
                print(f"  warn: could not remove {html_path}: {e}", file=sys.stderr)
    return removed


def main() -> int:
    ap = argparse.ArgumentParser(description="Build static HTML docs from project markdown")
    ap.add_argument("--clean", action="store_true",
                    help="Remove generated .html files (the .html sibling of every .md)")
    args = ap.parse_args()

    if args.clean:
        n = clean(PROJECT_ROOT)
        print(f"clean: removed {n} generated .html files")
        return 0

    if not HAVE_MARKDOWN:
        print("note: python3-markdown not installed; using built-in fallback renderer.",
              file=sys.stderr)
        print("      install with `pip install markdown` for full feature parity.",
              file=sys.stderr)

    md_files = collect_markdown(PROJECT_ROOT)
    rendered = 0
    skipped: list[tuple[Path, str]] = []
    for p in md_files:
        ok, err = build_one(p)
        if ok:
            rendered += 1
        else:
            skipped.append((p, err or "unknown error"))

    print(f"\nrendered: {rendered}/{len(md_files)} files")
    if skipped:
        print(f"skipped:  {len(skipped)} files")
        for p, err in skipped:
            print(f"  - {relative_to_root(p)}: {err}")
    else:
        print("skipped:  0 files")
    print(f"engine:   {'python-markdown ' + markdown.__version__ if HAVE_MARKDOWN else 'fallback'}")
    return 0 if not skipped else 1


if __name__ == "__main__":
    sys.exit(main())
