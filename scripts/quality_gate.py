#!/usr/bin/env python3
"""Run lightweight quality checks on an advisory pack.

Checks claim_register.csv, evidence_matrix.csv, source_log.csv, risk_register.csv if present.
No external dependencies.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

HIGH = {"high", "critical", "높음", "치명적"}
BAD_STATUSES = {"", "unsupported", "contradicted", "outdated", "needs live verification", "unverified"}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def norm(value: str | None) -> str:
    return (value or "").strip().lower()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", nargs="?", default=".", help="Advisory pack directory")
    args = parser.parse_args()
    pack = Path(args.pack)

    warnings: list[str] = []

    claims = read_csv(pack / "claim_register.csv")
    evidence = read_csv(pack / "evidence_matrix.csv")
    risks = read_csv(pack / "risk_register.csv")
    sources = read_csv(pack / "source_log.csv")

    evidence_by_claim: dict[str, list[dict[str, str]]] = {}
    for row in evidence:
        cid = row.get("claim_id", "").strip()
        if cid:
            evidence_by_claim.setdefault(cid, []).append(row)
        if not (row.get("source_location") or row.get("source_title")):
            warnings.append(f"Evidence row missing source locator: claim_id={cid or '<blank>'}")

    for row in claims:
        cid = row.get("claim_id", "").strip()
        importance = norm(row.get("importance"))
        status = norm(row.get("status"))
        evidence_ids = (row.get("evidence_ids") or "").strip()
        if importance in HIGH and status in BAD_STATUSES:
            warnings.append(f"High-importance claim is not adequately verified: {cid or row.get('claim','<blank>')}")
        if importance in HIGH and not evidence_ids and not evidence_by_claim.get(cid):
            warnings.append(f"High-importance claim has no linked evidence: {cid or row.get('claim','<blank>')}")

    for row in risks:
        rid = row.get("risk_id", "").strip()
        severity = norm(row.get("severity"))
        mitigation = (row.get("mitigation") or "").strip()
        stop = (row.get("stop_or_escalation_criterion") or "").strip()
        if severity in HIGH and not mitigation:
            warnings.append(f"High/Critical risk missing mitigation: {rid or row.get('description','<blank>')}")
        if severity in HIGH and not stop:
            warnings.append(f"High/Critical risk missing stop/escalation criterion: {rid or row.get('description','<blank>')}")

    if sources and not any(norm(r.get("reliability_grade")) in {"a", "primary", "authoritative"} for r in sources):
        warnings.append("No A/primary/authoritative source logged. This may be acceptable only for low-stakes exploratory work.")

    print("# Advisory Pack Quality Gate")
    print(f"Pack: {pack.resolve()}")
    print(f"Claims: {len(claims)} | Evidence rows: {len(evidence)} | Sources: {len(sources)} | Risks: {len(risks)}")
    if warnings:
        print("\n## Warnings")
        for warning in warnings:
            print(f"- {warning}")
        return 1
    print("\nPASS: no blocking quality-gate warnings detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
