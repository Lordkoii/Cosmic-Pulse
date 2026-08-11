#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

README = Path("README.md")
HERO_START = "<!-- AUTO_HERO_RELEASE_START -->"
HERO_END = "<!-- AUTO_HERO_RELEASE_END -->"
RELEASE_START = "<!-- AUTO_RELEASE_START -->"
RELEASE_END = "<!-- AUTO_RELEASE_END -->"


def replace_block(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end),
        flags=re.DOTALL,
    )
    if not pattern.search(text):
        raise RuntimeError(f"README marker block not found: {start}")
    return pattern.sub(f"{start}\n{replacement.rstrip()}\n{end}", text, count=1)


def pick_windows_zip(assets: list[dict]) -> dict | None:
    zips = [a for a in assets if str(a.get("name", "")).lower().endswith(".zip")]
    if not zips:
        return None

    preferred = [
        a
        for a in zips
        if "win-x64" in str(a.get("name", "")).lower()
        or "windows" in str(a.get("name", "")).lower()
    ]
    return (preferred or zips)[0]


def sha256_for(url: str) -> str:
    digest = hashlib.sha256()
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Cosmic-Pulse-release-readme-sync"},
    )
    with urllib.request.urlopen(request) as response:
        while chunk := response.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: sync_release_readme.py release.json", file=sys.stderr)
        return 2

    release = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not release:
        print("No release data found; leaving README unchanged.")
        return 0

    tag = str(release.get("tag_name") or "").strip()
    release_name = str(release.get("name") or tag).strip()
    release_url = str(release.get("html_url") or "").strip()
    asset = pick_windows_zip(release.get("assets") or [])

    if not tag or not release_url:
        raise RuntimeError("Release is missing tag_name or html_url")

    if asset is None:
        print("Release has no ZIP asset yet; leaving README unchanged.")
        return 0

    asset_name = str(asset["name"])
    asset_url = str(asset["browser_download_url"])
    checksum = sha256_for(asset_url)

    hero = f'''<p align="center">
  <a href="{release_url}">
    <img src="https://img.shields.io/badge/Download-Latest_Build-14c8f5?style=for-the-badge&logo=github&logoColor=white"
         alt="Download latest Cosmic Pulse build">
  </a>
</p>

<p align="center">
  <strong>Current tester build:</strong> <code>{tag}</code>
</p>'''

    download = f'''## Download

**{release_name} is now available.**

➡️ **[Open the current Cosmic Pulse release]({release_url})**

Download `{asset_name}` from the release assets, extract the entire ZIP to a folder, and run `CosmicPulse.exe`.

Only download Cosmic Pulse from releases published by **Lordkoii** in this repository.

> Cosmic Pulse is currently alpha software. Test builds may contain bugs or incomplete features. Because the application is not yet code-signed, Windows may display an unknown-publisher or security warning on some systems.

### File verification

SHA-256 for `{asset_name}`:

`{checksum}`'''

    text = README.read_text(encoding="utf-8")
    text = replace_block(text, HERO_START, HERO_END, hero)
    text = replace_block(text, RELEASE_START, RELEASE_END, download)
    README.write_text(text, encoding="utf-8")

    print(f"README synced to {tag} ({asset_name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
