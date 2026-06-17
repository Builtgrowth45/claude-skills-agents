# Plan: Re-run Higgsfield `/sync-agents` with import fixes

## Context
The user re-issued `/sync-agents` against the Higgsfield MCP (`https://mcp.higgsfield.ai/mcp`, already connected). The previous run imported only **15 of 42** local skills. A plain re-run would reproduce the same 15 successes and 23 failures, so this run's value is in **fixing the root causes** discovered last time. No personal/personality data exists on this host (empty memory dir), so nothing personal is uploaded — skills only.

### Root causes (diagnosed, read-only, this session)
- **18 "missing YAML frontmatter" rejections** → those `SKILL.md` files use **CRLF** line endings (`---\r\n`). The importer only recognizes `---\n`. Confirmed: every imported skill is LF; every rejected one is CRLF (e.g. `ads`, `ads-meta`, `impeccable`).
- **3 "name must match `^[a-z0-9][a-z0-9_-]{0,63}$`"** → `name:` values like `Agent Development` (capitals + space).
- **4 refused (binary files)** → `higgsfield` (PDF baselines), `openclaw` (`Dockerfile.e2e`), `planning-with-files` (`.ps1`), `skills` (`.template`). Importer is text-only; the whole skill is refused if any binary is present.
- **1 upload failure** → empty `skill-creator/scripts/__init__.py` (0 bytes) rejected by S3 `content-length-range` min=1.

### Environment gotcha (already solved last run)
Git Bash `/tmp` = `…\AppData\Local\Temp`, but the uploader script is **native Windows Python**, which resolves its hardcoded `/tmp/profile-import` to **`C:\tmp\profile-import`**. Staging must go to `C:\tmp\profile-import` (`/c/tmp/...` in Git Bash). The script is launched as `python3 /tmp/upload.py` (MSYS path-translates the arg to where it was downloaded); only the script's internal `WORK_DIR` needs the `C:\tmp` location.

## Permission prerequisite (Option A — user chose this)
The auto-mode classifier hard-blocks the uploader **download** (`curl … mcp.higgsfield.ai/internal/upload-script`), flagging "external code download + mass upload of local config." An in-chat "approve" does not clear it — it needs a standing `permissions.allow` rule. Plan-mode also blocks it, which is why execution must wait for plan approval.

**Step 0 (after approval, before anything else):** add a `permissions` block to `C:\Users\mcvea\.claude\settings.json` (currently has none), merging — not replacing — existing keys:
```json
"permissions": {
  "allow": [
    "Bash(curl:*)",
    "Bash(python3:*)"
  ]
}
```
- `Bash(curl:*)` is broad (allows all curl). A tighter alternative is a prefix rule like `Bash(curl -fsSL https://mcp.higgsfield.ai/*)`, but Claude Code prefix-matches the literal command string and the real invocation is quoted (`curl -fsSL 'https://…'`), so the narrow rule is brittle. Recommend the broad rule for reliability, or keep it project-local. *(Confirm scope at approval; see ExitPlanMode prompts.)*
- These persist; the user can remove them after the sync if they only want a one-time grant.

## Approach
1. **Apply Step 0** (permission rule above), then **invoke** `mcp__claude_ai_Higgsfield__sync_agents` with `message:"/sync-agents"`, `host:"claude_code"` to get a fresh one-time presigned upload URL + the Python uploader. Print the short ack. *(Note: each prior `/sync-agents` trigger issues a new ~15-min presigned URL; the one fetched mid-conversation is now stale and must be re-triggered.)*
2. **Stage** skills into `C:\tmp\profile-import\skills\<name>\` (copy from `C:\Users\mcvea\.claude\skills\*`, each dir that has `SKILL.md`, excluding `.git/.github/.hub/__pycache__/node_modules`). Originals are never modified — all fixes apply to the staged copies only.
3. **Apply fixes to the staged copies:**
   - **Normalize CRLF→LF** on all text files (`*.md`, `*.txt`, `*.json`, `*.yaml/yml`, etc.). Recovers ~18 skills.
   - **Strip binary files** (`*.png/jpg/jpeg/gif/webp/pdf/zip/mp4/mov/woff*/ttf/otf/ico` + the specific offenders `Dockerfile.e2e`, `*.ps1`, `*.template`) so the *text* of the 4 refused skills still imports.
   - **Drop empty (0-byte) files** to avoid the S3 min-size 400.
   - **Slugify non-conforming `name:` frontmatter values** to a valid slug (e.g. `Agent Development` → `agent-development`) to recover the 3 name-rejected skills. *(User chose Full fix.)*
4. **Run** the uploader: `python3 /tmp/upload.py` (writes to the `C:\tmp` staging). Capture the single-line JSON summary.
5. **Finalize**: call `sync_agents` again with `message:<summary JSON>`, `host:"claude_code"`. Report created/updated/invalid/refused counts back to the user.
6. **Clean up** `C:\tmp\profile-import`, staged temp, and the downloaded `upload.py`/logs.

## Expected outcome (Full fix)
Up to **~41–42 of 42** skills imported: 15 prior + ~18 CRLF-fixed + 4 binary-stripped text + 3 name-slugified. 0 empty-file upload errors.

## Critical files / tools
- Tool: `mcp__claude_ai_Higgsfield__sync_agents` (modes: `/sync-agents` trigger, then summary JSON).
- Source skills: `C:\Users\mcvea\.claude\skills\*\SKILL.md` (+ `references/`, `scripts/`, etc.).
- Staging (native-Python `/tmp`): `C:\tmp\profile-import\skills\…`.
- Uploader: downloaded `upload.py` (reviewed last run — write-only POST to user-scoped S3 prefix `users/user_309…/profile-import/…`; no system/credential access).

## Verification
- After step 4, the script prints `{"uploaded":N,...}`; confirm `N` ≈ total staged files and check the `failures` array is empty (no 0-byte/4xx).
- After step 5, inspect the finalize response: `imported`/`created` should jump from 15 toward ~38–42; the `refused` list should no longer contain `<unknown>` "missing frontmatter" entries; `invalid` count should drop to 0 (or 3 if names not slugified).
- Spot-check one previously-failing skill (e.g. `ads-meta`) appears with a real `skill_id` and `status:"created"`/`"updated"`.
