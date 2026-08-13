<p align="center">
  <img src="https://raw.githubusercontent.com/Lordkoii/Cosmic-Pulse/b2a835ec69525f18e47ab7942474bd3ff53d2486/assets/cosmic-pulse-banner.jpg"
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
  <strong>Current development milestone:</strong> <code>v0.1.0-alpha.7 — Incident Forensics</code>
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

A future finding should read more like this than a generic monitoring dashboard:

> **Memory Pressure — High Confidence**  
> System memory crossed 90% before sustained frame-time degradation began. GPU utilization fell during the slowdown, making GPU saturation an unlikely primary cause.

Cosmic Pulse should also be comfortable returning **Undetermined** when the available evidence is not strong enough for a responsible conclusion.

## Core systems

### Pulse Core — Validated foundation

The live telemetry layer currently provides:

- Star Citizen process detection
- LIVE / PTU / EPTU environment identification
- process CPU monitoring
- process memory monitoring
- system memory monitoring
- external PresentMon-based live FPS telemetry
- rolling PresentMon-based frame-time telemetry
- Windows-native GPU utilization telemetry
- dedicated VRAM usage and GPU identity

### PulseCheck — Alpha.4 validated

The first performance-intelligence layer correlates a rolling telemetry window rather than judging a single reading.

Current conservative classifications:

- CPU Limited
- GPU Limited
- Memory Pressure
- Possibly Capped / VSync / menu-limited behavior
- Undetermined

Each ready result includes a confidence level and supporting evidence. The classifier also has automated regression scenarios so known signatures cannot silently change without failing CI.

### Pulse Recorder — Alpha.5 validated

The local black-box foundation records one append-only telemetry snapshot per second while Star Citizen is running.

Records are flushed immediately for crash resilience and currently preserve FPS, frame time, CPU, GPU, process RAM, system RAM, VRAM, and PulseCheck state. Session start/end lifecycle markers and zero-sample acquisition cleanup are covered by regression tests.

### Pulse Events — Alpha.6 validated

The first timeline-intelligence layer identifies **when a sustained condition changes** without claiming root cause.

Current event signatures include:

- elevated and critical memory pressure
- memory-pressure recovery
- sustained GPU saturation
- GPU-saturation recovery
- sustained performance degradation using pre-event vs recent FPS/frame-time windows
- performance recovery toward the pre-event baseline

Detected events are immediately persisted as `performance_event` records alongside the raw telemetry, with severity, timestamp, summary, and supporting measurements. Repeated samples do not continuously duplicate an already-active condition.

### Incident Forensics — Alpha.7 in development

The first end-of-session investigation layer reviews the **final 60 seconds** of recorded evidence when a Star Citizen session ends.

Current alpha.7 behavior includes:

- session-duration tracking
- process termination reason and Windows exit-code capture when available
- normal-exit vs abnormal/non-zero-exit vs process-unavailable handling
- correlation of recent Pulse Events with the termination timeline
- recovered warnings excluded from active pre-exit precursor calls
- final-window frame-time, RAM, GPU, and PulseCheck evidence summaries
- persistent `incident_report` records written before `session_end`
- incident review retained visibly after Star Citizen closes
- a cautious suggested next test without claiming unsupported root cause
- correlation of the current user-accessible Star Citizen `Game.log`
- recognition of documented Star Citizen crash signatures including access violation, CryEngine watchdog/fatal, out-of-system-memory, and GPU-crash codes
- correlation of nearby Windows Application Error, Windows Error Reporting, and Application Hang records
- process-ID scoping for Windows evidence when the event exposes a PID
- structured external evidence preserved in schema-v2 incident records

Alpha.7 deliberately reports **precursors and correlations**, not automatic crash causes. A crash signature or performance event near a non-zero process exit is evidence worth preserving and testing, but it is not automatically treated as proof of the underlying root cause.

The next forensic refinements include richer crash-handler artifacts, driver-reset/System-log evidence, delayed Windows-event enrichment, and contradictory-evidence handling. Concurrent-workload awareness is also planned so system-wide GPU saturation is not incorrectly attributed solely to Star Citizen when other GPU-intensive applications are active.

### Pulse Report — Planned

Turn a session or incident into a concise explanation containing the event timeline, probable cause, confidence, evidence, and a recommended next test.

### PulseCompare — Planned

Compare controlled before-and-after sessions to determine whether a graphics setting, Windows setting, driver change, or hardware change actually improved the experience.

See [`ROADMAP.md`](ROADMAP.md) for the current development sequence.

## Current development status

Cosmic Pulse is in **private alpha development** and is being built incrementally against real Star Citizen sessions.

The current development milestone is:

```text
v0.1.0-alpha.7 — Incident Forensics
```

The current emphasis is **responsible multi-source incident correlation**: preserve the final telemetry window, distinguish normal and abnormal termination, correlate available Star Citizen and Windows diagnostic evidence, and keep observed evidence separate from unsupported root-cause claims.

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

Future public builds are intended for personal, non-commercial use under the terms in this repository's `LICENSE` file. Redistribution, resale, repackaging, rebranding, or claiming Cosmic Pulse as your own work is not permitted.

The private source repository is not licensed for public reuse or redistribution.

## Star Citizen disclaimer

Cosmic Pulse is an independent, unofficial fan-made utility and is not affiliated with, endorsed by, or sponsored by Cloud Imperium Games or Roberts Space Industries. Star Citizen and related marks belong to their respective owners.

## Creator

**Lordkoii**

Thanks for following Cosmic Pulse and helping shape what comes next.