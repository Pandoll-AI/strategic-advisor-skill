# Existing Document Review Workflow

Use when the user asks Codex to inspect existing documents, uploaded files, repository files, meeting notes, specs, PDFs, spreadsheets, slide decks, policies, or previous drafts.

## Principle

Codex should inspect accessible documents itself. Do not ask the user to paste text unless the documents are genuinely inaccessible.

## Discovery

Use the best available discovery method for the current environment:

- Repository: `rg --files`, `find`, `ls`, targeted reads.
- Markdown/text/code: `rg -n`, direct file reads with line references.
- PDF/DOCX/PPTX/XLSX: use available parsers or conversion tools; inspect pages/sheets/slides as needed.
- Connector/MCP sources: use available connector tools and cite connector references.
- Uploaded/session files: use the file/context tool exposed to the session.

## Review protocol

1. **Inventory**
   - Document title/path
   - Type
   - Owner/author if available
   - Created/updated date if available
   - Content date/version inside the document
   - Authority level

2. **Authority and freshness**
   - Do not trust metadata alone.
   - New upload date does not mean current content.
   - Recent modification can be minor.
   - Prefer content version, effective date, approval status, or cited source dates.

3. **Extraction**
   - Decisions
   - Requirements
   - Claims
   - Numbers/KPIs
   - Promises/commitments
   - Risks
   - Open questions
   - Dependencies

4. **Cross-check**
   - Compare across documents for contradictions.
   - Verify external factual claims with web search when relevant.
   - Flag outdated or unsupported claims.

5. **Output**
   - Document review map
   - Findings grouped by theme
   - Conflicts/outdated sections
   - Recommended edits or decisions
   - Evidence gaps

## Document review map

| Document | Location | Version/date | Authority | Key claims | Issues | Recommended action |
|---|---|---|---|---|---|---|

## Citation examples

- Local text: `path/to/file.md:42-57`
- PDF: `report.pdf p. 12, Table 3`
- Spreadsheet: `model.xlsx, Sheet "Assumptions", B12:D20`
- Slides: `deck.pptx, slide 7`
- Connector: use the connector-provided title/reference/link.
