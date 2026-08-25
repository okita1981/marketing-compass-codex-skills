#!/usr/bin/env python3
"""Verify the repository's Codex plugin packages using the standard library.

As of 2026-08-25 there are two Codex plugin packages, checked
independently:

  plugins/marketing-compass/  (8 Marketing Compass skills)
  plugins/thinking-staircase/ (the general-purpose thinking-staircase skill)

They are separate because thinking-staircase is not Marketing
Compass-specific — same reason the Claude Code plugin under plugin/ is
split into plugin/marketing-compass/ and plugin/thinking-staircase/ (see
scripts/verify-claude-code-plugin.py for that ecosystem's equivalent
check). Which skill belongs to which package is defined once, in
scripts/_skills_list.py, and shared by both ecosystems.

For each plugin package, checks:
  1. <plugin>/.codex-plugin/plugin.json exists, is valid JSON, has `name`
     matching the plugin's directory name, a semver `version`, and
     `skills` pointing to "./skills/".
  2. .agents/plugins/marketplace.json contains exactly one local entry for
     this plugin, pointing at ./plugins/<plugin>.
  3. For every skill assigned to that plugin: <plugin>/skills/<name>/SKILL.md
     and <plugin>/skills/<name>/agents/openai.yaml exist.
  4. No skill assigned to this plugin appears under the other plugin's
     skills/ directory (the two packages must not overlap).
  5. No stray skill directories left inside <plugin>/skills/ that aren't
     assigned to this plugin.

Once, independent of any single plugin:
  6. scripts/sync-codex-plugin.py --check passes for both packages
     together (that script itself loops over both).
  7. No symlinks anywhere under plugins/.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import (  # noqa: E402
    MARKETING_COMPASS_PLUGIN_SKILLS,
    THINKING_STAIRCASE_PLUGIN_SKILLS,
)

PLUGINS = {
    "marketing-compass": MARKETING_COMPASS_PLUGIN_SKILLS,
    "thinking-staircase": THINKING_STAIRCASE_PLUGIN_SKILLS,
}

PLUGINS_ROOT = REPO_ROOT / "plugins"
MARKETPLACE = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


try:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
except Exception as exc:  # noqa: BLE001
    marketplace = {}
    fail(f"invalid marketplace manifest: {exc}")


def check_plugin(plugin_name: str, skill_names: list[str]) -> None:
    plugin_root = PLUGINS_ROOT / plugin_name
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        manifest = {}
        fail(f"[{plugin_name}] invalid plugin manifest: {exc}")

    if manifest:
        if manifest.get("name") != plugin_name:
            fail(f"[{plugin_name}] plugin manifest name must be '{plugin_name}'")
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
            fail(f"[{plugin_name}] plugin manifest version must be semver")
        if manifest.get("skills") != "./skills/":
            fail(f"[{plugin_name}] plugin manifest must point skills to ./skills/")

    if marketplace:
        entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == plugin_name]
        expected_path = f"./plugins/{plugin_name}"
        if len(entries) != 1 or entries[0].get("source", {}).get("path") != expected_path:
            fail(f"[{plugin_name}] marketplace must contain exactly one local entry pointing at {expected_path}")

    for name in skill_names:
        root = plugin_root / "skills" / name
        if not (root / "SKILL.md").is_file():
            fail(f"[{plugin_name}/{name}] missing skills/{name}/SKILL.md")
        if not (root / "agents" / "openai.yaml").is_file():
            fail(f"[{plugin_name}/{name}] missing skills/{name}/agents/openai.yaml")

    for other_name, other_skills in PLUGINS.items():
        if other_name == plugin_name:
            continue
        overlap = set(skill_names) & set(other_skills)
        if overlap:
            fail(f"[{plugin_name}] skill(s) {sorted(overlap)} also assigned to plugin '{other_name}' — the two Codex plugins must not overlap")

    skills_dir = plugin_root / "skills"
    if skills_dir.is_dir():
        actual = {p.name for p in skills_dir.iterdir() if p.is_dir()}
        extra = actual - set(skill_names)
        if extra:
            fail(f"[{plugin_name}] plugins/{plugin_name}/skills/ contains unexpected skill dir(s) {sorted(extra)} not assigned to this plugin")


for plugin_name, skill_names in PLUGINS.items():
    check_plugin(plugin_name, skill_names)


sync_check = subprocess.run(
    [sys.executable, str(REPO_ROOT / "scripts" / "sync-codex-plugin.py"), "--check"],
    capture_output=True,
    text=True,
)
if sync_check.returncode:
    fail(sync_check.stdout.strip() or sync_check.stderr.strip() or "plugin skills are out of sync")

for path in PLUGINS_ROOT.rglob("*"):
    if path.is_symlink():
        fail(f"symlink is not allowed: {path.relative_to(REPO_ROOT)}")

total_skills = sum(len(s) for s in PLUGINS.values())

if failures:
    print("Codex plugin verification failed:")
    for message in failures:
        print(f"- {message}")
    raise SystemExit(1)

print(f"Codex plugin verification passed: {len(PLUGINS)} package(s), {total_skills} skills bundled and in sync.")
