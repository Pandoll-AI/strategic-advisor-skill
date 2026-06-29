#!/usr/bin/env python3
"""Create a structured strategic advisory working folder from bundled templates.

Usage:
    python scripts/new_advisory_pack.py "AI safety benchmark" --out /tmp/advisory_pack
"""
from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path

TEMPLATE_FILES = [
    "deep_deliberation_report.md",
    "research_brief.md",
    "evidence_matrix.csv",
    "claim_register.csv",
    "source_log.csv",
    "risk_register.csv",
    "document_review_map.csv",
    "decision_log.md",
]


def slugify(text: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in text.strip())
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-") or "advisory-pack"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", help="Strategic topic or decision name")
    parser.add_argument("--out", help="Output directory. Defaults to ./advisory-pack-<slug>")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    template_dir = skill_root / "templates"
    out_dir = Path(args.out) if args.out else Path.cwd() / f"advisory-pack-{slugify(args.topic)}"
    out_dir.mkdir(parents=True, exist_ok=True)

    for name in TEMPLATE_FILES:
        src = template_dir / name
        if not src.exists():
            raise FileNotFoundError(f"Missing template: {src}")
        dst = out_dir / name
        if dst.exists():
            continue
        shutil.copy2(src, dst)

    readme = out_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# Advisory Pack: {args.topic}\n\n"
            f"Created: {date.today().isoformat()}\n\n"
            "Suggested order:\n"
            "1. Fill source_log.csv as sources are inspected.\n"
            "2. Extract claims into claim_register.csv.\n"
            "3. Link claims to evidence in evidence_matrix.csv.\n"
            "4. Record risks in risk_register.csv.\n"
            "5. Write final research_brief.md or deep_deliberation_report.md.\n",
            encoding="utf-8",
        )

    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
