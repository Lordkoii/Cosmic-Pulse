# Cosmic Pulse Roadmap

Cosmic Pulse is being developed as a **Star Citizen performance and reliability forensics tool**, not as a general gameplay companion.

The guiding product question is:

> Does this feature help explain why a Star Citizen session performed badly or failed?

If not, it is probably outside the core scope.

## Validated foundation

### v0.1.0-alpha.0 — Pulse Core

- Star Citizen process detection
- LIVE / PTU / EPTU detection
- process CPU monitoring
- process memory monitoring
- system memory monitoring

### v0.1.0-alpha.1 — FPS Telemetry

- external PresentMon integration
- live rolling FPS telemetry

### v0.1.0-alpha.2 — Frame-Time Telemetry

- rolling frame-time telemetry from the same PresentMon stream

### v0.1.0-alpha.3 — GPU Telemetry

- Windows-native GPU utilization
- GPU identity
- dedicated VRAM usage
- resilience to dynamic Windows GPU counter instances

### v0.1.0-alpha.4 — PulseCheck

- rolling evidence window
- confidence-based classifications
- CPU Limited
- GPU Limited
- Memory Pressure
- Possibly Capped
- Undetermined
- automated regression coverage for known signatures

### v0.1.0-alpha.5 — Pulse Recorder

- automatic session recording when Star Citizen is detected
- one append-only telemetry snapshot per second
- immediate record flush for crash resilience
- local session storage under the user's application-data directory
- FPS, frame time, CPU, GPU, RAM, VRAM, and PulseCheck state preservation
- session start/end lifecycle markers
- zero-sample acquisition sessions discarded
- persistence and lifecycle regression coverage

### v0.1.0-alpha.6 — Event Detection

- elevated and critical memory-pressure events
- memory-pressure recovery
- sustained GPU saturation and recovery
- sustained performance degradation and recovery
- event deduplication while a detected condition remains active
- immediate `performance_event` persistence alongside raw telemetry
- severity, timestamp, summary, and supporting evidence stored with each event
- automated regression coverage for event entry, recovery, deduplication, and persistence

Alpha.6 establishes **when something changed** without claiming root cause.

## Current development

### v0.1.0-alpha.7 — Incident Forensics

Build the first end-of-session failure-investigation workflow on top of the validated recorder and event timeline.

Current alpha.7 implementation:

- preserve a rolling final 60-second forensic review window
- capture session termination reason and Windows process exit code when available
- distinguish normal process exit, abnormal/non-zero exit, process disappearance, recorder interruption, and Cosmic Pulse closing before the game
- correlate recent Pulse Events with the termination timeline
- treat recovered warning conditions as historical evidence rather than active pre-exit precursors
- summarize frame-time, system-memory, GPU, and final PulseCheck evidence from the review window
- persist an `incident_report` record before `session_end`
- keep the incident review visible in the app after Star Citizen closes
- provide a cautious next diagnostic test without claiming an unsupported root cause
- show live session duration in the status row
- automated regression coverage for normal exits, abnormal exits with precursors, recovered conditions, the 60-second boundary, and incident persistence

Alpha.7 deliberately distinguishes **correlation from causation**. An event occurring before an abnormal exit is reported as a precursor, not automatically as the crash cause.

Still planned for later incident-forensics passes:

- correlation with relevant Windows diagnostic events
- correlation with user-accessible Star Citizen log evidence
- richer crash/driver-reset signatures
- additional termination evidence when Windows exposes it safely
- explicit contradictory-evidence handling

Possible later event signatures:

- dedicated short-duration frame-time spike / stutter events
- GPU-utilization collapse events meaningful independently of a broader degradation event
- richer memory-transition staging

## Forensic intelligence sequence

### v0.1.0-alpha.8 — Pulse Report

Turn raw session evidence into an understandable report.

A report should answer:

1. What happened?
2. When did it start?
3. What changed beforehand?
4. What is the likely cause?
5. How confident is that conclusion?
6. What should the player test next?

Planned outputs:

- event timeline
- likely cause and confidence
- supporting evidence
- contradictory evidence where relevant
- recommended next diagnostic test
- local export suitable for sharing in support / community discussions

### v0.1.0-alpha.9 — PulseCompare

Add controlled before-and-after testing.

Examples:

- graphics setting A vs B
- resolution / upscaler changes
- driver changes
- Windows configuration changes
- hardware changes

The goal is to answer **whether the change actually improved the Star Citizen experience**, using recorded evidence rather than subjective impressions alone.

## Public alpha target

The first public test build should feel like a product rather than a developer project.

Before broad public testing, the intended experience is:

```text
Install
  ↓
Launch Cosmic Pulse
  ↓
Launch Star Citizen
  ↓
Cosmic Pulse records and analyzes automatically
```

Public users should not need Git, PowerShell, a .NET SDK, or manual developer setup.

## Longer-term possibilities

Only after the forensic core is reliable:

- session history and searchable incident archive
- patch-to-patch comparisons
- hardware/configuration baselines
- richer per-core / thread correlation where Windows telemetry permits it safely
- stutter classification
- community-shareable anonymized diagnostic reports with explicit user opt-in
- local rules / signature updates without weakening privacy or safety

## Non-goals

Cosmic Pulse is not currently intended to become:

- a trading assistant
- a cargo/mining/salvage calculator
- a fleet manager
- a navigation database
- a general Star Citizen wiki client
- a gameplay automation tool
- an injected overlay

These boundaries keep the project focused on a specific job: **performance and reliability forensics for Star Citizen**.
