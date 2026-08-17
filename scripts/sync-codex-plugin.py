#!/usr/bin/env python3
"""Synchronize canonical Codex skills into plugins/marketing-compass/skills."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402

SOURCE_ROOT = REPO_ROOT / "skills"
TARGET_ROOT = REPO_ROOT / "plugins" / "marketing-compass" / "skills"


def tree_matches(source: Path, target: Path) -> bool:
    if not target.is_dir():
        return False
    comparison = filecmp.dircmp(source, target)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(source / name, target / name, shallow=False) for name in comparison.common_files):
        return False
    return all(tree_matches(source / name, target / name) for name in comparison.common_dirs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    stale = [name for name in SKILLS if not tree_matches(SOURCE_ROOT / name, TARGET_ROOT / name)]
    extras = sorted(path.name for path in TARGET_ROOT.iterdir() if path.is_dir() and path.name not in SKILLS)

    if args.check:
        if stale or extras:
            print("Codex plugin is out of sync.")
            if stale:
                print("Stale or missing:", ", ".join(stale))
            if extras:
                print("Unexpected:", ", ".join(extras))
            return 1
        print("Codex plugin skill copies are in sync with skills/.")
        return 0

    TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    for name in extras:
        shutil.rmtree(TARGET_ROOT / name)
    for name in stale:
        destination = TARGET_ROOT / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(SOURCE_ROOT / name, destination)
        print(f"Synced {name}")
    if not stale and not extras:
        print("Already in sync. No files changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
