#!/usr/bin/env python3
"""Verify the repository's Codex plugin package using the standard library."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402

PLUGIN_ROOT = REPO_ROOT / "plugins" / "marketing-compass"
MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
except Exception as exc:
    manifest = {}
    fail(f"invalid plugin manifest: {exc}")

if manifest.get("name") != "marketing-compass":
    fail("plugin manifest name must be marketing-compass")
if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
    fail("plugin manifest version must be semver")
if manifest.get("skills") != "./skills/":
    fail("plugin manifest must point skills to ./skills/")

try:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == "marketing-compass"]
    if len(entries) != 1 or entries[0].get("source", {}).get("path") != "./plugins/marketing-compass":
        fail("marketplace must contain one local marketing-compass entry")
except Exception as exc:
    fail(f"invalid marketplace manifest: {exc}")

sync_check = subprocess.run(
    [sys.executable, str(REPO_ROOT / "scripts" / "sync-codex-plugin.py"), "--check"],
    capture_output=True,
    text=True,
)
if sync_check.returncode:
    fail(sync_check.stdout.strip() or sync_check.stderr.strip() or "plugin skills are out of sync")

for name in SKILLS:
    root = PLUGIN_ROOT / "skills" / name
    if not (root / "SKILL.md").is_file():
        fail(f"missing skills/{name}/SKILL.md")
    if not (root / "agents" / "openai.yaml").is_file():
        fail(f"missing skills/{name}/agents/openai.yaml")

for path in PLUGIN_ROOT.rglob("*"):
    if path.is_symlink():
        fail(f"symlink is not allowed: {path.relative_to(REPO_ROOT)}")

if failures:
    print("Codex plugin verification failed:")
    for message in failures:
        print(f"- {message}")
    raise SystemExit(1)

print(f"Codex plugin verification passed: {len(SKILLS)} skills bundled and in sync.")
