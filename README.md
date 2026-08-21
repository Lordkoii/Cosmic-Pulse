<p align="center">
  <img src="assets/cosmic-pulse-banner.gif"
       alt="Cosmic Pulse — Star Citizen Performance & Reliability Forensics"
       width="100%">
</p>

<p align="center">
  <strong>Status:</strong> Private Alpha
  &nbsp;•&nbsp;
  <strong>Platform:</strong> Windows x64
  &nbsp;•&nbsp;
  <strong>Source:</strong> Private
</p>

<!-- AUTO_HERO_RELEASE_START -->
<p align="center">
  <img src="https://img.shields.io/badge/Public_Test_Builds-Coming_Soon-8a62ff?style=for-the-badge" alt="Public test builds coming soon">
</p>

<p align="center">
  <strong>Current development milestone:</strong> <code>v0.1.0-alpha.8 — Pulse Report</code>
</p>
<!-- AUTO_HERO_RELEASE_END -->

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
  <a href="https://ko-fi.com/cosmicutilities">
    <img src="https://img.shields.io/badge/Support-Cosmic_Utilities-ff5e5b?style=flat-square&logo=kofi&logoColor=white"
         alt="Support Cosmic Utilities on Ko-fi">
  </a>
</p>

---

## About Cosmic Pulse

**Cosmic Pulse is a Windows performance and reliability forensics tool for Star Citizen.**

It is being built to do more than display FPS, CPU, GPU, RAM, and VRAM. Those measurements are the sensors. The product goal is to correlate them over time and help answer four practical questions:

1. **What happened?**
2. **When did it start?**
3. **What changed immediately beforehand?**
4. **What should I test next?**

Traditional monitoring tools are excellent at showing what hardware is doing right now. Cosmic Pulse is being built as a local **black box for a Star Citizen session**: record the evidence, detect meaningful changes, preserve the moments before a failure, and produce cautious findings with visible confidence and supporting evidence.

This public repository is the home for **future tester downloads, release notes, bug reports, and performance / diagnosis feedback**. The application source code is maintained separately in a private repository and is **not distributed here**.

## Product focus

Cosmic Pulse is intentionally **not** being designed as an all-purpose Star Citizen companion suite.

The core mission is performance and reliability investigation. General trading tools, cargo/mining calculators, fleet management, navigation databases, gameplay automation, and similar gameplay-companion features are outside that mission unless they directly help explain a performance or stability event.

A feature belongs in Cosmic Pulse when it helps explain **why a Star Citizen session performed badly or failed**.

## How Cosmic Pulse works

```text
Star Citizen session
        │
        ├── FPS / frame time
        ├── CPU / GPU behavior
        ├── RAM / VRAM pressure
        ├── Windows telemetry
        └── available game / crash diagnostics
                 │
                 ▼
           COSMIC PULSE
          Local black box
                 │
        record → correlate → explain
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
 Performance   Incident   Before/After
   events      forensics    comparison
        └────────┼────────┘
                 ▼
             PULSE REPORT
```

Cosmic Pulse should be comfortable returning **Undetermined** when the available evidence is not strong enough for a responsible conclusion.

## Core systems

### Pulse Core — Validated foundation

The live telemetry layer provides Star Citizen process/channel detection, process CPU/RAM, system RAM, PresentMon FPS/frame time, Windows-native GPU telemetry, GPU identity, and dedicated VRAM usage.

### PulseCheck — Alpha.4 validated

The rolling performance-intelligence layer classifies CPU Limited, GPU Limited, Memory Pressure, Possibly Capped, or Undetermined with visible confidence and supporting evidence.

### Pulse Recorder — Alpha.5 validated

The local black box records append-only telemetry snapshots and session lifecycle evidence with immediate flush behavior for crash resilience.

### Pulse Events — Alpha.6 validated

The timeline layer detects sustained memory pressure/recovery, GPU saturation/recovery, and performance degradation/recovery without assigning root cause.

### Incident Forensics — Alpha.7 validated

Alpha.7 established the end-of-session investigation layer and was closed after regression and real-machine validation.

Validated behavior includes:

- final 60-second telemetry/event review window
- Windows process exit-code preservation
- conservative normal, abnormal, unresolved, interrupted, and contradictory termination handling
- unknown non-zero exit codes withheld from crash classification unless corroborated
- Star Citizen `Game.log` and RSI Launcher abnormal-exit evidence
- Windows Application Error, WER, Application Hang, and contextual Display/TDR evidence
- Star Citizen crash-handler artifact checkpointing and fresh-artifact detection
- four-second post-exit evidence enrichment
- active-vs-recovered Pulse Event precursor handling
- read-only environment fingerprinting
- Star Citizen-specific GPU attribution and concurrent-workload context
- foreground/focus awareness without capturing window titles
- recurring incident-signature comparison across recent local session history
- repeatability guidance that explicitly does not claim repeated incidents share one root cause
- Windows activation diagnostics and background GPU sampling to avoid expensive counter enumeration blocking the WPF UI

Real-session validation confirmed clean exits remain clean with the expanded collectors active, recovered warnings are not falsely promoted to active precursors, concurrent workloads stay contextual, and a repeated abnormal termination pattern can be recognized from local history without claiming causation.

### Pulse Report — Alpha.8 in development

Alpha.8 turns the validated evidence stack into a stable user-facing report layer.

The first report foundation defines a structured result that separates:

- session outcome
- confidence
- what happened
- what changed beforehand
- evidence-supported assessment
- supporting evidence
- contradictory evidence
- ordered event timeline
- recommended next diagnostic test

The report layer deliberately inherits alpha.7's conservative evidence rules rather than inventing a stronger causal conclusion during presentation.

Planned alpha.8 work includes the report view, richer timeline presentation, environment/workload context summaries, and a local export suitable for support or community sharing.

### PulseCompare — Planned

Compare controlled before-and-after sessions to determine whether a graphics setting, Windows setting, driver change, or hardware change actually improved the experience.

See [`ROADMAP.md`](ROADMAP.md) for the current development sequence.

## Current development status

Cosmic Pulse is in **private alpha development** and is being built incrementally against real Star Citizen sessions.

The current development milestone is:

```text
v0.1.0-alpha.8 — Pulse Report
```

The current emphasis is turning the validated telemetry/event/forensic evidence into an understandable report **without weakening the distinction between correlation and causation**.

There is **no public build available yet**. Public downloads will appear here only after a build has been tested and is ready for community evaluation.

<!-- AUTO_RELEASE_START -->
## Download

**Public test builds are coming soon.**

When the first tester build is ready, this section will contain the official release link, package name, installation instructions, release notes, and SHA-256 file verification information.

Only download Cosmic Pulse from releases published by **Lordkoii** in this repository.
<!-- AUTO_RELEASE_END -->

## Help test Cosmic Pulse

When public testing begins, varied real-world hardware and genuine Star Citizen failures will be essential to improving diagnostic accuracy.

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

**Local-first:** session and diagnostic data is intended to remain on the user's PC unless a feature clearly asks the user to export or share it.

## Security

Security-sensitive findings should **not** be reported through a public issue.

Please review [`SECURITY.md`](SECURITY.md) for the responsible-reporting process, supported-version guidance, and privacy expectations for security reports.

## License and distribution

Cosmic Pulse is **proprietary software**. It is not open source.

Copyright © 2026 **Lordkoii**. All rights reserved.

Future official compiled releases may be downloaded, installed, and used for personal, non-commercial evaluation and personal use under the terms in [`LICENSE`](LICENSE).

The application source code is maintained privately and is not licensed for public reuse, modification, or redistribution.

Redistribution, resale, repackaging, rebranding, or claiming Cosmic Pulse as your own work is not permitted.

Third-party components included with future official builds will remain subject to their respective licenses and notices, which will be provided with release packages where required.

## Star Citizen disclaimer

Cosmic Pulse is an independent, unofficial fan-made utility and is not affiliated with, endorsed by, or sponsored by Cloud Imperium Games or Roberts Space Industries. Star Citizen and related marks belong to their respective owners.

## Creator

Created and maintained by **Lordkoii**.

Thanks for following Cosmic Pulse and helping shape what comes next.
