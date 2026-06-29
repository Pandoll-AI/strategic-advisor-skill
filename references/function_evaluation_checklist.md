# Functional Evaluation Checklist

Use this checklist before releasing or modifying the skill.

## Skill packaging

- [ ] `SKILL.md` exists.
- [ ] Frontmatter includes `name` and `description`.
- [ ] Description contains trigger words for explicit and implicit activation.
- [ ] Package includes `manifest.txt`.
- [ ] Install instructions are present.
- [ ] Naming is `strategic-advisor` and user-facing copy consistently says `Strategic Advisor`.

## Codex orchestration

- [ ] Skill explicitly says Codex should perform available web search/research/document review itself.
- [ ] Live web search is required for current or unstable facts unless user forbids it.
- [ ] Fallback behaviour is defined when live search/connectors/subagents are unavailable.
- [ ] Subagent protocol is present.
- [ ] Sequential fallback is present.

## Research quality

- [ ] Deep research workflow decomposes the question.
- [ ] Source hierarchy prioritises primary/authoritative sources.
- [ ] Contradiction search is required.
- [ ] Evidence matrix template exists.
- [ ] Source log template exists.

## Fact verification

- [ ] Atomic claim extraction is required.
- [ ] Claim statuses are defined.
- [ ] Safer wording is required for overstrong claims.
- [ ] High-risk/current claims cannot be treated as verified without sources.

## Existing document review

- [ ] Local/repository document review is covered.
- [ ] Uploaded/session/connector/MCP documents are covered when accessible.
- [ ] Document authority/freshness is assessed from content, not metadata alone.
- [ ] Document review map template exists.

## Decision quality

- [ ] Steelman and red-team loops are both present.
- [ ] Trade-off alternatives include aggressive/balanced/defensive/defer.
- [ ] Quality gates are explicit.
- [ ] Output ends with next actions and stop criteria.

## Safety and trust

- [ ] Medical/legal/financial/regulatory caveats are present.
- [ ] Unsupported claims are marked, not hidden.
- [ ] The skill forbids fabricated citations.
- [ ] The skill avoids promises of asynchronous or background work unless the environment supports it.

## Usability

- [ ] Example prompts are included.
- [ ] Templates are included.
- [ ] Scripts are no-dependency or document dependencies.
- [ ] Evaluation script runs successfully.
- [ ] README, hero image, and install instructions are ready for public sharing.
