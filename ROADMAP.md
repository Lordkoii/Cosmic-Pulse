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
- distinguish normal exits, evidence-backed abnormal exits, process disappearance, recorder interruption, and Cosmic Pulse closing before the game
- avoid treating an unknown non-zero process exit code as a crash by itself
- keep unknown non-zero codes in `SESSION END REVIEW` unless corroborating crash evidence is available
- correlate recent Pulse Events with the termination timeline
- treat recovered warning conditions as historical evidence rather than active pre-exit precursors
- summarize frame-time, system-memory, GPU, and final PulseCheck evidence from the review window
- persist an `incident_report` record before `session_end`
- keep the incident review visible in the app after Star Citizen closes
- provide a cautious next diagnostic test without claiming an unsupported root cause
- show live session duration in the status row
- correlate the current Star Citizen `Game.log` when it contains recognized crash evidence
- recognize documented Star Citizen crash signatures such as access violation, CryEngine watchdog/fatal, out-of-system-memory, and GPU-crash codes
- correlate RSI Launcher `log.log` abnormal-exit records written during the tracked Star Citizen session
- checkpoint the Launcher log when a session begins so stale entries from earlier runs are not reused
- correlate Windows Application Error, Windows Error Reporting, and Application Hang records near termination
- scope Windows evidence to the tracked Star Citizen process ID when the event record exposes one
- preserve external forensic evidence structurally in schema-v2 `incident_report` records
- distinguish an abnormal exit with independent diagnostic evidence from one supported only by telemetry precursors
- automated regression coverage for normal exits, documented crash codes, unknown non-zero exits, Launcher abnormal-exit evidence, abnormal exits with precursors, recovered conditions, the 60-second boundary, incident persistence, Game.log signatures, Windows event parsing, and external-evidence classification

Alpha.7 deliberately distinguishes **correlation from causation**. An event or crash signature occurring near an abnormal exit is reported as evidence, not automatically as proof of the underlying root cause. A non-zero process code that is not a documented RSI crash code is also treated as unresolved unless another evidence source corroborates it.

Still planned for later incident-forensics passes:

- richer parsing of Star Citizen crash-handler artifacts such as payload and GPU diagnostic files
- Windows driver-reset and additional System-log signatures
- delayed/late Windows-event enrichment when diagnostic records are written after process termination
- explicit contradictory-evidence handling
- recurring incident-signature comparison across sessions
- richer crash/driver-reset signatures as real-world evidence is validated

Possible later event signatures:

- dedicated short-duration frame-time spike / stutter events
- GPU-utilization collapse events meaningful independently of a broader degradation event
- richer memory-transition staging

### Near-term telemetry intelligence — Concurrent Workload Awareness

Current GPU utilization and dedicated-VRAM telemetry describe the adapter as a whole. That is useful system evidence, but a saturated GPU is not automatically proof that Star Citizen alone created the load.

Planned work:

- detect significant concurrent GPU workloads while Star Citizen is running
- distinguish system-wide GPU pressure from Star Citizen-specific frame-throughput evidence
- avoid attributing total adapter saturation solely to Star Citizen when other applications are active
- surface concurrent-workload evidence in PulseCheck and Incident Forensics
- investigate safe per-process / per-adapter attribution using external Windows telemetry where accuracy is sufficient

The goal is to make statements such as **“GPU contention detected”** more defensible than a generic “GPU bottleneck” call when another game, browser video, stream, or GPU-accelerated application is also active.

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
