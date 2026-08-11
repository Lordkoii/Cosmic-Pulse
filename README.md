<p align="center">
  <strong>COSMIC PULSE</strong><br>
  <em>Star Citizen Performance Intelligence</em>
</p>

<!-- Banner target: assets/cosmic-pulse-banner.png -->

<p align="center">
  <strong>Status:</strong> Private Alpha
  &nbsp;•&nbsp;
  <strong>Platform:</strong> Windows x64
  &nbsp;•&nbsp;
  <strong>Source:</strong> Private
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Public_Test_Builds-Coming_Soon-8a62ff?style=for-the-badge" alt="Public test builds coming soon">
</p>

<p align="center">
  <strong>Current internal milestone:</strong> <code>v0.1.0-alpha.0 — Pulse Core</code>
</p>

<p align="center">
  <a href="https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=bug_report.yml">
    <img src="https://img.shields.io/badge/Report-a_Bug-f05d5e?style=flat-square&logo=github" alt="Report a Cosmic Pulse bug">
  </a>
  <a href="https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=feature_request.yml">
    <img src="https://img.shields.io/badge/Suggest-a_Feature-8a62ff?style=flat-square&logo=github" alt="Suggest a Cosmic Pulse feature">
  </a>
  <a href="https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=performance_feedback.yml">
    <img src="https://img.shields.io/badge/Performance-Feedback-2ecc71?style=flat-square&logo=github" alt="Share Cosmic Pulse performance feedback">
  </a>
</p>

---

## About Cosmic Pulse

**Cosmic Pulse is a Windows companion application for Star Citizen designed to help players understand why the game is performing poorly — not just show raw numbers.**

It is being built to analyze real gameplay telemetry, identify likely system bottlenecks, compare before-and-after changes, and eventually help diagnose stability problems such as crashes, disconnects, and poor frame pacing.

Traditional monitoring tools tell you **what your hardware is doing**. Cosmic Pulse is being built to tell you **what that means for Star Citizen and what you should do about it**.

This public repository is the home for **future tester downloads, release notes, bug reports, and performance feedback**. The application source code is maintained separately in a private repository and is **not distributed here**.

## How Cosmic Pulse works

```text
Star Citizen session
        │
        ├── Frame performance
        ├── CPU / GPU behavior
        ├── RAM / VRAM pressure
        ├── Windows telemetry
        └── Game / crash diagnostics
                 │
                 ▼
           COSMIC PULSE
        Analysis & correlation
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
  Performance  Stability  Optimization
   analysis    analysis      advice
        └────────┼────────┘
                 ▼
            PULSE REPORT
```

The goal is a clear result such as:

> **CPU Limited**  
> GPU headroom remains available. Reducing resolution is unlikely to significantly improve performance.

Recommendations are intended to be based on evidence from the user's own PC and gameplay session rather than generic optimization lists.

## Core systems

### Pulse Core — In development

The foundation for live Star Citizen session detection and performance telemetry.

Current internal focus:

- Star Citizen process detection
- LIVE / PTU / EPTU environment identification
- process CPU monitoring
- process memory monitoring
- system memory monitoring

### PulseCheck — Planned

Analyzes a gameplay session and identifies probable CPU, GPU, memory, frame-time, or system constraints.

### PulseCompare — Planned

Compares before-and-after tests to determine whether a graphics, Windows, driver, or hardware change actually improved the experience.

### Reliability — Planned

Correlates available Star Citizen and Windows diagnostic information to help explain crashes, disconnects, driver resets, and other stability problems.

### Session History — Planned

Tracks performance over time so users can compare configurations, locations, and eventually patch-to-patch behavior.

## Current development status

Cosmic Pulse is in **private alpha development** and is being built incrementally against real Star Citizen sessions.

The current internal milestone is:

```text
v0.1.0-alpha.0 — Pulse Core
```

There is **no public build available yet**. Public downloads will appear here only after a build has been tested and is ready for community evaluation.

## Download

**Public test builds are coming soon.**

When the first tester build is ready, this section will contain the official release link, package name, installation instructions, release notes, and SHA-256 file verification information.

Only download Cosmic Pulse from releases published by **Lordkoii** in this repository.

## Help test Cosmic Pulse

When public testing begins, real-world feedback will be one of the most important parts of improving diagnostic accuracy.

**Found an application problem?** Use the [Bug Report](https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=bug_report.yml) form.

**Have a QOL or feature idea?** Use the [Feature Suggestion](https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=feature_request.yml) form.

**Think a performance diagnosis is wrong or incomplete?** Use the [Performance / Diagnosis Feedback](https://github.com/Lordkoii/Cosmic-Pulse/issues/new?template=performance_feedback.yml) form and include your hardware, resolution, Star Citizen environment, gameplay scenario, and the diagnosis Cosmic Pulse produced.

Diagnostic information should be reviewed before posting publicly. Do not include account credentials, authentication tokens, personally identifying information, or unrelated private logs.

## Safety & privacy

Cosmic Pulse is designed as an **external companion application**.

It does not intend to:

- inject DLLs or code into Star Citizen
- read Star Citizen process memory
- intercept or manipulate game/network traffic
- automate keyboard, mouse, or gameplay actions
- modify Star Citizen client files

The project is being designed around external Windows/system telemetry and user-accessible diagnostic information.

**Local-first:** performance/session data is intended to remain on the user's PC unless a future feature clearly asks the user to export or share diagnostic information.

## License and distribution

Cosmic Pulse is **proprietary software**. It is not open source.

Copyright © 2026 **Lordkoii**. All rights reserved.

Future public builds are intended for personal, non-commercial use under the terms in this repository's `LICENSE` file. Redistribution, resale, repackaging, rebranding, or claiming Cosmic Pulse as your own work is not permitted.

The private source repository is not licensed for public reuse or redistribution.

## Star Citizen disclaimer

Cosmic Pulse is an independent, unofficial fan-made utility and is not affiliated with, endorsed by, or sponsored by Cloud Imperium Games or Roberts Space Industries. Star Citizen and related marks belong to their respective owners.

## Creator

**Lordkoii**

Thanks for following Cosmic Pulse and helping shape what comes next.
