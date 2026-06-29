# Codex Operating Notes

## Skill location

Codex reads global skills from `~/.codex/skills`. This repository is designed to be installed directly as:

```text
~/.codex/skills/strategic-advisor/SKILL.md
```

## Custom agents

Codex custom agents are standalone TOML files under `.codex/agents/` for project scope or `~/.codex/agents/` for personal scope. This skill does not require custom agent files; when subagents are unavailable, run the research, document-review, fact-check, red-team, and synthesis roles sequentially.

## Live search

For current facts, launch Codex with live search if your environment supports it:

```bash
codex --search -C /path/to/repo
```

If live search is not available, the skill still works for local documents and reasoning, but current factual claims must be marked as unverified or needing live verification.

## Suggested repository config

Keep agent depth at 1 unless there is a deliberate reason for recursive delegation.
