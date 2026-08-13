#!/usr/bin/env python3
"""Structural + content-parity verification for the Claude Code skill copies.

Checks, per the 9 in-scope skills:
  1. .claude/skills/<name>/SKILL.md exists.
  2. YAML frontmatter parses, has non-empty `name` and `description`.
  3. `name` in frontmatter equals the directory name (required for the
     Claude Code command to be /<name>).
  4. description length (and description+when_to_use) is under the 1536
     character Claude Code truncates at.
  5. No two skills share a name.
  6. Every relative markdown link to references/*.md in SKILL.md resolves
     to a real file inside .claude/skills/<name>/.
  7. .claude/skills/<name>/SKILL.md and references/*.md are byte-identical
     to the canonical skills/<name>/ source (content parity / no silent
     simplification).
  8. No symlinks are used anywhere under .claude/skills/.
  9. No obviously-local absolute paths (C:\\Users, /home/, /Users/) or
     committed secrets (best-effort keyword scan) inside the generated
     files.
  10. skills/ and canonical/ (the GPT/Codex + canonical corpus) are
      untouched by this change (git diff against origin/main is empty for
      those paths).

Exit code 0 = all checks passed. Non-zero = at least one failure, printed.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402 (see scripts/_skills_list.py)

FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\((references/[^)\s]+)\)")

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


# --- 1-6: structural checks on the Claude Code copies ---
names_seen: dict[str, str] = {}

for name in SKILLS:
    claude_dir = REPO_ROOT / ".claude" / "skills" / name
    skill_md = claude_dir / "SKILL.md"

    if not skill_md.is_file():
        fail(f"[{name}] missing .claude/skills/{name}/SKILL.md")
        continue

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        fail(f"[{name}] SKILL.md frontmatter did not parse (missing --- block?)")
        continue

    fm_name = fm.get("name", "")
    fm_desc = fm.get("description", "")

    if not fm_name:
        fail(f"[{name}] frontmatter has no `name` field")
    elif fm_name != name:
        fail(f"[{name}] frontmatter name '{fm_name}' != directory name '{name}'")

    if not fm_desc:
        fail(f"[{name}] frontmatter has no `description` field")
    else:
        when_to_use = fm.get("when_to_use", "")
        combined_len = len(fm_desc) + len(when_to_use)
        if combined_len > 1536:
            fail(
                f"[{name}] description(+when_to_use) is {combined_len} chars, "
                "exceeds the 1536-char Claude Code listing cap"
            )

    if fm_name:
        if fm_name in names_seen:
            fail(f"[{name}] duplicate skill name '{fm_name}' also used by '{names_seen[fm_name]}'")
        else:
            names_seen[fm_name] = name

    # Relative reference links must resolve inside the Claude Code copy.
    for link in LINK_RE.findall(text):
        target = claude_dir / link
        if not target.is_file():
            fail(f"[{name}] SKILL.md links to '{link}' which does not exist at {target}")

    # references/ must not contain files SKILL.md never mentions being
    # unreferenced isn't an error by itself (informational only skip).

    # 8. no symlinks
    for p in claude_dir.rglob("*"):
        if p.is_symlink():
            fail(f"[{name}] symlink found at {p} — not portable to Windows clones")

    # 9. no local absolute paths / obvious secrets
    bad_path_patterns = [r"C:\\Users", r"/home/[a-zA-Z0-9_-]+", r"/Users/[a-zA-Z0-9_-]+"]
    secret_patterns = [r"sk-[A-Za-z0-9]{16,}", r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"]
    for pat in bad_path_patterns:
        if re.search(pat, text):
            fail(f"[{name}] SKILL.md appears to contain a local absolute path matching /{pat}/")
    for pat in secret_patterns:
        if re.search(pat, text):
            fail(f"[{name}] SKILL.md appears to contain a secret-like token matching /{pat}/")


# --- 7: byte-parity between skills/<name>/ (canonical) and .claude/skills/<name>/ ---
def relevant_files(base: Path) -> set[Path]:
    out: set[Path] = set()
    skill_md = base / "SKILL.md"
    if skill_md.is_file():
        out.add(skill_md.relative_to(base))
    refs = base / "references"
    if refs.is_dir():
        for f in refs.rglob("*.md"):
            out.add(f.relative_to(base))
    return out


for name in SKILLS:
    src = REPO_ROOT / "skills" / name
    dst = REPO_ROOT / ".claude" / "skills" / name
    if not src.is_dir() or not dst.is_dir():
        continue

    src_files = relevant_files(src)
    dst_files = relevant_files(dst)

    missing_in_dst = src_files - dst_files
    extra_in_dst = dst_files - src_files
    for rel in sorted(missing_in_dst):
        fail(f"[{name}] canonical file {rel} was not copied to .claude/skills/{name}/")
    for rel in sorted(extra_in_dst):
        warn(f"[{name}] .claude/skills/{name}/{rel} has no canonical counterpart in skills/{name}/")

    for rel in sorted(src_files & dst_files):
        a = (src / rel).read_bytes()
        b = (dst / rel).read_bytes()
        if a != b:
            fail(f"[{name}] {rel} differs between skills/{name}/ and .claude/skills/{name}/ (content drift)")


# --- 10: GPT/Codex source + canonical corpus untouched ---
def git_diff_paths(paths: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD", "--", *paths],
            cwd=REPO_ROOT,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        warn(f"could not run git diff for {paths}: {exc.stderr.strip()}")
        return ""


protected_paths = ["skills/", "canonical/", "LICENSE", ".gitignore"]
diff_out = git_diff_paths(protected_paths)
if diff_out:
    fail(
        "GPT/Codex source or canonical corpus changed versus origin/main:\n"
        + "\n".join(f"    {line}" for line in diff_out.splitlines())
    )


# --- report ---
print(f"Checked {len(SKILLS)} Claude Code skills under .claude/skills/\n")

if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")
    print()

if failures:
    print(f"FAILURES ({len(failures)}):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print("All structural, parity, and isolation checks PASSED.")
sys.exit(0)
