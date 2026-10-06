#!/usr/bin/env python3
"""Build dashboard/index.html from dashboard/src.html.

Embeds the current agent definitions, skills and shared-desk files from the
repo so the "Agents & skills" page always shows what is committed.

    python3 dashboard/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "dashboard" / "src.html"
OUT = ROOT / "dashboard" / "index.html"

FILES = (
    sorted((ROOT / ".claude" / "agents").glob("*.md"))
    + sorted((ROOT / "skills").glob("*/SKILL.md"))
    + [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "handoffs" / "README.md"]
    + sorted(p for p in (ROOT / "handoffs").glob("[0-9]*.md"))
)

PIPELINE_FIRST = ["dealer.md", "assayer.md", "pit-boss-judge.md"]


def order(p: pathlib.Path) -> tuple:
    rel = p.relative_to(ROOT).as_posix()
    if rel.startswith(".claude/agents/"):
        name = p.name
        return (0, PIPELINE_FIRST.index(name) if name in PIPELINE_FIRST else 9, rel)
    return (1, 0, rel)


def main() -> None:
    files = [
        {"path": p.relative_to(ROOT).as_posix(), "content": p.read_text(encoding="utf-8")}
        for p in sorted((f for f in FILES if f.exists()), key=order)
    ]
    payload = json.dumps(files, ensure_ascii=False).replace("</", "<\\/")
    html = SRC.read_text(encoding="utf-8").replace("/*__REPO_FILES__*/[]", payload, 1)
    OUT.write_text(html, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)} with {len(files)} files, {len(html):,} bytes")


if __name__ == "__main__":
    main()
