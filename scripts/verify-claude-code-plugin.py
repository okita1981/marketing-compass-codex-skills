#!/usr/bin/env python3
"""Structural + content-parity verification for the plugin/ package
(the installable Claude Code plugin, distinct from the .claude/skills/
project-skill copy — see scripts/verify-claude-code-skills.py for that one).

Checks:
  1. plugin/.claude-plugin/plugin.json exists and is valid JSON.
  2. Required field `name` is present, non-empty, kebab-case (matches the
     Claude Code plugin manifest schema's naming rule).
  3. `version` is present (recommended by `claude plugin validate`; not
     technically required by the schema, but the review pipeline and this
     script both flag its absence).
  4. `description`, `author`, `homepage`, `repository`, `license` are
     present (not schema-required, but expected for a professional
     marketplace listing).
  5. For every skill in scripts/_skills_list.py: plugin/skills/<name>/SKILL.md
     exists, has parseable frontmatter with non-empty `name`/`description`.
  6. Every relative reference/*.md link in each SKILL.md resolves inside
     plugin/skills/<name>/.
  7. plugin/skills/<name>/{SKILL.md,references/*.md} are byte-identical to
     the canonical skills/<name>/ source (no silent simplification when
     packaging for the plugin).
  8. No symlinks anywhere under plugin/.
  9. No local absolute paths or secret-shaped tokens in the generated files.
  10. skills/ and canonical/ (the GPT/Codex + canonical corpus) are
      untouched by this change (git diff against origin/main is empty for
      those paths).
  11. If the `claude` CLI is available on PATH, runs
      `claude plugin validate ./plugin --strict` and reports its result.
      This check is skipped (not failed) when the CLI isn't installed,
      since it's a convenience wrapper around the official validator, not
      a replacement for it.

Exit code 0 = all checks passed (or skipped where noted). Non-zero = at
least one failure, printed.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# `claude plugin validate` output can contain non-ASCII symbols (checkmarks,
# etc.). On Windows consoles, stdout defaults to the system codepage (e.g.
# cp932), which can't encode them and would crash a plain print(). Fall back
# to replacement characters instead of crashing.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402 (see scripts/_skills_list.py)

PLUGIN_ROOT = REPO_ROOT / "plugin"
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\((references/[^)\s]+)\)")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

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


# --- 1-4: plugin.json manifest ---
manifest_path = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
manifest: dict = {}

if not manifest_path.is_file():
    fail(f"missing {manifest_path.relative_to(REPO_ROOT)}")
else:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json is not valid JSON: {exc}")

    if manifest:
        plugin_name = manifest.get("name", "")
        if not plugin_name:
            fail("plugin.json missing required field `name`")
        elif not NAME_RE.match(plugin_name):
            fail(f"plugin.json `name` '{plugin_name}' is not kebab-case (required by the plugin manifest schema)")

        if not manifest.get("version"):
            fail("plugin.json missing `version` (claude plugin validate flags this as a warning; set an explicit semver version)")

        for recommended in ("description", "author", "homepage", "repository", "license"):
            if not manifest.get(recommended):
                warn(f"plugin.json missing recommended field `{recommended}` for a marketplace listing")


# --- 5-9: per-skill checks inside plugin/skills/ ---
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
    plugin_dir = PLUGIN_ROOT / "skills" / name
    skill_md = plugin_dir / "SKILL.md"

    if not skill_md.is_file():
        fail(f"[{name}] missing plugin/skills/{name}/SKILL.md")
        continue

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        fail(f"[{name}] SKILL.md frontmatter did not parse (missing --- block?)")
        continue

    if not fm.get("name"):
        fail(f"[{name}] frontmatter has no `name` field")
    if not fm.get("description"):
        fail(f"[{name}] frontmatter has no `description` field")

    for link in LINK_RE.findall(text):
        target = plugin_dir / link
        if not target.is_file():
            fail(f"[{name}] SKILL.md links to '{link}' which does not exist at {target}")

    for p in plugin_dir.rglob("*"):
        if p.is_symlink():
            fail(f"[{name}] symlink found at {p} — not portable to Windows clones")

    bad_path_patterns = [r"C:\\Users", r"/home/[a-zA-Z0-9_-]+", r"/Users/[a-zA-Z0-9_-]+"]
    secret_patterns = [r"sk-[A-Za-z0-9]{16,}", r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"]
    for pat in bad_path_patterns:
        if re.search(pat, text):
            fail(f"[{name}] SKILL.md appears to contain a local absolute path matching /{pat}/")
    for pat in secret_patterns:
        if re.search(pat, text):
            fail(f"[{name}] SKILL.md appears to contain a secret-like token matching /{pat}/")

    # content parity vs canonical source
    src = REPO_ROOT / "skills" / name
    if src.is_dir():
        src_files = relevant_files(src)
        dst_files = relevant_files(plugin_dir)

        for rel in sorted(src_files - dst_files):
            fail(f"[{name}] canonical file {rel} was not copied to plugin/skills/{name}/")
        for rel in sorted(dst_files - src_files):
            warn(f"[{name}] plugin/skills/{name}/{rel} has no canonical counterpart in skills/{name}/")

        for rel in sorted(src_files & dst_files):
            a = (src / rel).read_bytes()
            b = (plugin_dir / rel).read_bytes()
            if a != b:
                fail(f"[{name}] {rel} differs between skills/{name}/ and plugin/skills/{name}/ (content drift)")


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


# --- 11: official validator, best-effort ---
claude_bin = shutil.which("claude")
if claude_bin:
    try:
        result = subprocess.run(
            [claude_bin, "plugin", "validate", str(PLUGIN_ROOT), "--strict"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
        output = ((result.stdout or "") + (result.stderr or "")).strip()
        if result.returncode != 0:
            fail(f"`claude plugin validate ./plugin --strict` failed:\n{output}")
        else:
            print(f"claude plugin validate ./plugin --strict:\n{output}\n")
    except Exception as exc:  # noqa: BLE001 - best-effort convenience check
        warn(f"could not run `claude plugin validate`: {exc}")
else:
    warn("`claude` CLI not found on PATH — skipped the official `claude plugin validate` check")


# --- report ---
print(f"Checked plugin/ ({len(SKILLS)} skills) against manifest and canonical source\n")

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
