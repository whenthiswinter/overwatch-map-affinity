"""report/analysis_report.md -> a standalone web page for the live site.

The workflow regenerates the report daily and publishes this page at
/report/ on GitHub Pages (Markdown files there would open as raw text).
"""
import os
import sys

import markdown

BASE = os.path.join(os.path.dirname(__file__), "..")
SOURCE = os.path.join(BASE, "report", "analysis_report.md")
DEFAULT_OUT = os.path.join(BASE, "report", "index.html")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Map Affinity Report</title>
<style>
  :root {{ --bg: #fafafa; --surface: #fff; --border: #e4e4e7; --text: #18181b; --muted: #71717a; --accent: #ea580c; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: #101012; --surface: #18181b; --border: #29292e; --text: #e4e4e7; --muted: #91919a; --accent: #fb923c; }}
  }}
  body {{ margin: 0; background: var(--bg); color: var(--text); font: 14px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif; }}
  main {{ max-width: 1100px; margin: 0 auto; padding: 24px 16px 60px; }}
  a {{ color: var(--accent); }}
  .back {{ font-size: 0.85rem; }}
  h1 {{ font-size: 1.6rem; letter-spacing: -0.02em; }}
  h2 {{ margin-top: 2.2em; border-bottom: 1px solid var(--border); padding-bottom: 4px; }}
  h3 {{ margin-top: 1.8em; }}
  table {{ border-collapse: collapse; display: block; overflow-x: auto; font-size: 0.85rem; }}
  th, td {{ border-bottom: 1px solid var(--border); padding: 4px 10px; text-align: left; white-space: nowrap; }}
  th {{ color: var(--muted); font-weight: 600; }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 2em 0; }}
  code {{ font-size: 0.85em; }}
</style>
</head>
<body>
<main>
<p class="back"><a href="../web/index.html">&larr; Back to the dashboard</a> &middot; <a href="../data/csv/map_tierlists.csv">map_tierlists.csv</a> &middot; <a href="../data/csv/hero_volatility.csv">hero_volatility.csv</a></p>
{body}
</main>
</body>
</html>
"""


def main(out_path=DEFAULT_OUT):
    with open(SOURCE, encoding="utf-8") as f:
        body = markdown.markdown(f.read(), extensions=["tables", "toc"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PAGE.format(body=body))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
