#!/usr/bin/env python3
"""Evaluate the strategic-advisor skill repository.

Usage:
    python scripts/evaluate_skill.py --root .
"""
from __future__ import annotations

import argparse
import json
import re
import struct
from pathlib import Path

SKILL_NAME = "strategic-advisor"

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "assets/hero.png",
    "tasks/deep_deliberation.md",
    "tasks/deep_research.md",
    "tasks/fact_check.md",
    "tasks/document_review.md",
    "tasks/decision_quality_gates.md",
    "tasks/subagent_orchestration.md",
    "references/function_evaluation_checklist.md",
    "references/source_reliability_policy.md",
    "references/research_quality_rubric.md",
    "references/risk_taxonomy.md",
    "references/codex_operating_notes.md",
    "templates/deep_deliberation_report.md",
    "templates/research_brief.md",
    "templates/evidence_matrix.csv",
    "templates/claim_register.csv",
    "templates/source_log.csv",
    "templates/risk_register.csv",
    "templates/document_review_map.csv",
    "templates/decision_log.md",
    "scripts/new_advisory_pack.py",
    "scripts/quality_gate.py",
    "scripts/evaluate_skill.py",
    "examples/usage_prompts.md",
    "examples/strategic_advisor_rag_vs_grep_memory.md",
    "manifest.txt",
]

KEY_PHRASES = [
    "Strategic Advisor",
    "Operating Contract",
    "Core Loop",
    "Evidence Discipline",
    "decision quality gates",
    "red-team",
    "Needs live verification",
    "do not expose hidden chain-of-thought",
]

DISALLOWED_PHRASE_CODES = [
    [97, 100, 118, 97, 110, 99, 101, 100, 45, 97, 115, 115, 105, 115, 116, 97, 110, 116, 45, 97, 103, 101, 110, 116],
    [65, 100, 118, 97, 110, 99, 101, 100, 32, 65, 115, 115, 105, 115, 116, 97, 110, 116, 32, 65, 103, 101, 110, 116],
    [86, 73, 83, 73, 66, 76, 69, 95, 83, 75, 73, 76, 76, 95, 70, 73, 76, 69, 83],
    [65, 67, 84, 85, 65, 76, 95, 83, 75, 73, 76, 76, 95, 68, 79, 67, 85, 77, 69, 78, 84],
]
DISALLOWED_PHRASES = ["".join(chr(code) for code in codes) for codes in DISALLOWED_PHRASE_CODES]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[bool, dict[str, str]]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return False, {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return True, data


def package_files(root: Path) -> set[str]:
    ignored = {".git", "__pycache__", "outputs"}
    files: set[str] = set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored for part in path.parts):
            continue
        if path.suffix in {".pyc", ".zip"}:
            continue
        rel = str(path.relative_to(root))
        if rel == "manifest.txt":
            continue
        files.add(rel)
    return files


def check_manifest(root: Path) -> tuple[bool, str]:
    manifest = root / "manifest.txt"
    if not manifest.exists():
        return False, "manifest.txt missing"
    listed = {line.strip() for line in read(manifest).splitlines() if line.strip()}
    actual = package_files(root)
    missing = actual - listed
    extra = listed - actual
    if missing or extra:
        return False, f"missing={sorted(missing)[:8]}, extra={sorted(extra)[:8]}"
    return True, "manifest matches repository files"


def png_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as f:
            header = f.read(24)
        if header[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        return struct.unpack(">II", header[16:24])
    except OSError:
        return None


def find_disallowed_hits(root: Path) -> list[str]:
    hits: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix in {".png", ".pyc", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        for phrase in DISALLOWED_PHRASES:
            if phrase.lower() in lower:
                hits.append(f"{path.relative_to(root)} contains {phrase}")
                break
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    results: list[dict[str, object]] = []

    def add(name: str, ok: bool, detail: str = "") -> None:
        results.append({"check": name, "ok": bool(ok), "detail": detail})

    for rel in REQUIRED_FILES:
        add(f"required file: {rel}", (root / rel).exists())

    skill_md = root / "SKILL.md"
    if skill_md.exists():
        text = read(skill_md)
        ok_fm, fm = parse_frontmatter(text)
        add("frontmatter present", ok_fm)
        add("frontmatter name", fm.get("name") == SKILL_NAME, fm.get("name", ""))
        add("frontmatter description", bool(fm.get("description")), fm.get("description", "")[:160])
        add("frontmatter has only name and description", set(fm.keys()) <= {"name", "description"})
        for phrase in KEY_PHRASES:
            add(f"SKILL.md contains: {phrase}", phrase.lower() in text.lower())
        add("no TODO placeholders in SKILL.md", "TODO" not in text)

    ok_manifest, manifest_detail = check_manifest(root)
    add("manifest consistency", ok_manifest, manifest_detail)

    hero_size = png_size(root / "assets" / "hero.png")
    add("hero image is PNG", hero_size is not None, str(hero_size or "missing/invalid"))
    if hero_size:
        add("hero image has wide aspect", hero_size[0] >= 1200 and hero_size[0] > hero_size[1], f"{hero_size[0]}x{hero_size[1]}")

    readme = root / "README.md"
    if readme.exists():
        readme_text = read(readme)
        add("README references hero", "assets/hero.png" in readme_text)
        add("README includes Korean install section", "## 설치" in readme_text)
        add("README includes public usage prompt", "$strategic-advisor" in readme_text)

    hits = find_disallowed_hits(root)
    add("legacy duplicate package labels removed", not hits, "; ".join(hits[:8]))

    passed = sum(1 for item in results if item["ok"])
    total = len(results)
    score = round(100 * passed / total, 1) if total else 0
    ok = passed == total
    payload = {"ok": ok, "score": score, "passed": passed, "total": total, "results": results}

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print("# Strategic Advisor Skill Evaluation")
        print(f"Root: {root}")
        print(f"Score: {passed}/{total} ({score}%)")
        print()
        for item in results:
            mark = "PASS" if item["ok"] else "FAIL"
            detail = f" - {item['detail']}" if item.get("detail") else ""
            print(f"- {mark}: {item['check']}{detail}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
