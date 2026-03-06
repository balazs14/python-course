---
description: "Debug Python errors from selected code, traceback, or notebook cells with concrete fix steps"
name: "Debug Python Code"
argument-hint: "Paste traceback and what you expected"
agent: "agent"
model: "GPT-5 (copilot)"
---
Debug the provided Python issue.

Inputs you can use:
- User argument (`${input}`): traceback, error message, expected behavior
- Current workspace files
- Selected code or active notebook cell (if available)

Your job:
1. Identify the most likely root cause.
2. Explain the failure in 2-4 short bullets.
3. Propose the smallest safe fix first.
4. If useful, provide one improved alternative fix.
5. Add a minimal verification step to confirm the fix.

Output format:
- `Root cause:` one concise paragraph
- `Fix:` exact code block or patch-style snippet
- `Why it works:` 1-3 bullets
- `Verify:` 1-2 commands or code lines to run
- `If this is a notebook:` mention whether to rerun only the current cell or all dependent cells

Constraints:
- Prefer minimal, local changes over rewrites.
- Preserve existing style and variable naming unless incorrect.
- If data comes from network (CSV/API), include a fallback path for offline use.
- If details are missing, state assumptions explicitly before suggesting fixes.
