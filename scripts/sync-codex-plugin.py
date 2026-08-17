#!/usr/bin/env python3
"""Synchronize canonical Codex skills into plugins/marketing-compass/skills."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from _skills_list import SKILLS  # noqa: E402

SOURCE_ROOT = REPO_ROOT / "skills"
TARGET_ROOT = REPO_ROOT / "plugins" / "marketing-compass" / "skills"
PRODUCT_BLOCK = b"  products:\n  - chatgpt\n  - codex\n  - api\n  - atlas\n"


def expected_bytes(source_root: Path, source_file: Path) -> bytes:
    relative = source_file.relative_to(source_root).as_posix()
    content = source_file.read_bytes().replace(b"\r\n", b"\n")
    if relative == "agents/openai.yaml":
        content = content.replace(PRODUCT_BLOCK, b"")
    if relative == "references/model.md" and content.endswith(b"\n\n"):
        content = content[:-1]
    return content


def tree_matches(source: Path, target: Path) -> bool:
    if not target.is_dir():
        return False
    source_files = {path.relative_to(source).as_posix(): path for path in source.rglob("*") if path.is_file()}
    target_files = {path.relative_to(target).as_posix(): path for path in target.rglob("*") if path.is_file()}
    if source_files.keys() != target_files.keys():
        return False
    return all(
        expected_bytes(source, path) == target_files[relative].read_bytes().replace(b"\r\n", b"\n")
        for relative, path in source_files.items()
    )


def normalize_package(skill_root: Path) -> None:
    agent_file = skill_root / "agents" / "openai.yaml"
    if agent_file.is_file():
        agent_file.write_bytes(agent_file.read_bytes().replace(b"\r\n", b"\n").replace(PRODUCT_BLOCK, b""))
    model_file = skill_root / "references" / "model.md"
    if model_file.is_file():
        content = model_file.read_bytes().replace(b"\r\n", b"\n")
        if content.endswith(b"\n\n"):
            content = content[:-1]
        model_file.write_bytes(content)


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
        normalize_package(destination)
        print(f"Synced {name}")
    if not stale and not extras:
        print("Already in sync. No files changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
