# Cosmic Pulse Security Policy

Cosmic Pulse is a proprietary Windows application currently in private alpha development. This policy describes how security-sensitive reports should be handled for the public distribution repository and future tester builds.

## Reporting a security issue

Please **do not open a public GitHub issue containing vulnerability details**, exploit steps, credentials, tokens, proof-of-concept code, or other sensitive technical information.

If GitHub's **Private vulnerability reporting** option is available on this repository, use that channel so the report and technical details remain private.

If private vulnerability reporting is not available, open a minimal public issue titled **[Security] Request private contact** without including sensitive technical details. A private reporting channel can then be arranged.

When reporting a security issue, include only the information necessary to reproduce and understand the problem:

- Cosmic Pulse version
- Windows version
- affected component or workflow
- reproduction steps
- expected and observed behavior
- security impact
- relevant logs or screenshots after removing credentials, tokens, personal information, and unrelated private data

## Scope

Security reports may include issues involving:

- official Cosmic Pulse binaries or release packages
- update or release-distribution behavior
- local diagnostic or session-data handling
- unsafe file permissions or storage behavior
- accidental secret, token, or credential exposure
- code execution or privilege-escalation behavior attributable to Cosmic Pulse
- vulnerabilities in bundled third-party components when they materially affect Cosmic Pulse users

General bugs, performance-diagnosis disagreements, feature ideas, and Star Citizen gameplay issues should use the normal public issue forms instead.

## Supported versions

Cosmic Pulse does not yet have a public tester release. Until public releases begin, security fixes apply to the actively developed alpha line only.

After public distribution begins, the latest published tester build will be the primary supported version unless a release note states otherwise.

## Disclosure

Please allow reasonable time to investigate and prepare a fix before publicly disclosing a security issue. Confirmed security fixes will be documented appropriately when a corrected build is released.

## Privacy

Do not include account credentials, authentication tokens, private keys, personally identifying information, unrelated logs, or other sensitive data in a report.

Cosmic Pulse is designed around a local-first model. Performance and diagnostic information is intended to remain on the user's PC unless the user explicitly exports or shares it. Review and remove information that is not necessary for the security report before sharing diagnostics.
