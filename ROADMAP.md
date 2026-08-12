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

## Current development

### v0.1.0-alpha.5 — Pulse Recorder

Build the local session black box.

Goals:

- automatically begin recording when Star Citizen is detected
- append one telemetry snapshot per second
- immediately flush records for crash resilience
- store sessions locally under the user's application-data directory
- preserve FPS, frame time, CPU, GPU, RAM, VRAM, and PulseCheck state
- mark session start and session end without pretending a normal process exit is a crash
- validate the persisted timeline before building higher-level interpretation

## Forensic intelligence sequence

### v0.1.0-alpha.6 — Event Detection

Detect meaningful changes in the recorded timeline.

Planned examples:

- sustained FPS degradation
- frame-time spikes and sustained frame-time increases
- system RAM / VRAM pressure transitions
- sustained GPU saturation
- GPU utilization collapse during a slowdown
- recovery after a degradation event

The goal is to identify **when something changed**, not yet to claim why.

### v0.1.0-alpha.7 — Incident Forensics

Build the first failure-investigation workflow.

Planned goals:

- detect that a recorded Star Citizen session ended unexpectedly when the evidence supports that conclusion
- preserve and summarize the final 60–120 seconds of telemetry
- correlate available Windows diagnostic events
- correlate user-accessible Star Citizen log evidence
- distinguish evidence from inference
- return Undetermined when a cause cannot be supported responsibly

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
