# Cosmic Pulse — Public Release Checklist

This repository is the public distribution and feedback home for Cosmic Pulse. Application source code remains in the private `Cosmic-Pulse-Source` repository.

## Release naming

Use semantic prerelease tags while Cosmic Pulse is in alpha:

```text
v0.1.0-alpha.0
v0.1.0-alpha.1
v0.1.0-alpha.2
```

Recommended Windows package naming:

```text
CosmicPulse-v0.1.0-alpha.0-win-x64.zip
```

The ZIP should contain the complete runnable Windows x64 build and any required third-party notices.

## Before publishing

- Confirm the matching private-source commit has passed its Windows build check.
- Run the build locally on Windows.
- Launch Cosmic Pulse from the packaged output, not only from the development project.
- Verify Star Citizen detection and the features included in that version.
- Confirm the version shown by the application matches the release tag.
- Review included files for accidental source code, secrets, local paths, logs, or private telemetry.
- Include `THIRD-PARTY-NOTICES.txt` when third-party redistributable components are bundled.

## GitHub release

1. Create a release using the matching version tag.
2. Use a concise release title, for example:

   ```text
   Cosmic Pulse v0.1.0-alpha.0 — Pulse Core
   ```

3. Add release notes describing what changed, known limitations, and what feedback is most useful.
4. Upload the Windows x64 ZIP.
5. Publish the release.

## README automation

The `Sync release README` GitHub Actions workflow runs when a release is published or edited.

It automatically updates the marked sections in `README.md` with:

- the latest release link
- current tester version
- exact ZIP filename
- SHA-256 checksum of the ZIP

If a release is changed after publishing, the workflow can also be run manually from the **Actions** tab.

The automation intentionally does nothing when it cannot find a ZIP release asset.

## Distribution rule

Only official builds published by **Lordkoii** in this repository should be presented as Cosmic Pulse public releases.
