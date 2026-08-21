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

### v0.1.0-alpha.6 — Pulse Events

- elevated and critical memory-pressure events
- memory-pressure recovery
- sustained GPU saturation and recovery
- sustained performance degradation and recovery
- event deduplication while a detected condition remains active
- immediate `performance_event` persistence alongside raw telemetry
- severity, timestamp, summary, and supporting evidence stored with each event
- automated regression coverage for entry, recovery, deduplication, and persistence

Alpha.6 establishes **when something changed** without claiming root cause.

### v0.1.0-alpha.7 — Incident Forensics — validated

Alpha.7 established the first end-of-session failure-investigation workflow on top of the recorder and event timeline.

Validated termination and evidence handling:

- preserve a rolling final 60-second forensic review window
- capture session termination reason and Windows process exit code when available
- distinguish normal exits, evidence-backed abnormal exits, unresolved non-zero exits, process disappearance, monitoring interruption, and recorder interruption
- avoid treating an unknown non-zero process exit code as a crash by itself
- detect explicit contradictory termination evidence instead of forcing one source to win
- classify exit code `0` plus independent Star Citizen/Windows failure evidence as `CONFLICTING TERMINATION EVIDENCE`
- keep context-only evidence such as Windows Display Event 4101/TDR from overriding a clean exit by itself
- correlate recent Pulse Events with the termination timeline
- treat recovered warning conditions as historical evidence rather than active pre-exit precursors
- summarize final-window frame time, system memory, GPU, PulseCheck, focus, and workload context
- persist an `incident_report` before `session_end`
- keep the incident review visible after Star Citizen closes
- provide a cautious next diagnostic test without claiming unsupported root cause

Validated external evidence sources:

- current Star Citizen `Game.log`
- documented Star Citizen access-violation, CryEngine watchdog/fatal, out-of-system-memory, GPU-crash, breakpoint, and frozen-close signatures
- RSI Launcher `log.log` abnormal-exit records checkpointed to the tracked session
- Windows Application Error, Windows Error Reporting, and Application Hang records
- tracked-PID scoping for Windows records when PID metadata is available
- `%LOCALAPPDATA%\Star Citizen` crash-handler artifact checkpointing
- fresh `payload.zip`, `gpu_error.log`, and crash-handler `game.log` detection
- read-only `payload.zip` metadata / entry-name inspection without extraction
- Windows System `Display` Event 4101/TDR context
- four-second post-exit evidence enrichment for records written after process termination
- immediate/delayed evidence deduplication

Validated recurring incident intelligence:

- compare non-clean incident signatures against up to 40 recent local session files without loading full telemetry histories
- isolate LIVE / PTU / EPTU histories when channel context exists
- match termination family, exit-code state, independent evidence families, active/recovered event shape, and conservative PulseCheck context
- normalize legacy alpha.7 unknown-nonzero semantics into the current unresolved-exit family
- normalize Windows Application Error and WER into the same application-failure family without collapsing distinct Star Citizen crash signatures
- treat Star Citizen build as context rather than a hard match requirement
- exclude clean normal exits, interruptions, and context-only TDR from recurring-incident classification
- surface prior-match count, reviewed-incident count, latest match, and same-build/different-build context
- change the next-test guidance toward one-variable-at-a-time testing when a pattern repeats
- explicitly state that recurrence is evidence of repeatability, not proof of a shared root cause

Validated workload / focus context:

- per-process Windows `GPU Engine` attribution for Star Citizen when available
- Star Citizen-specific GPU utilization separated from adapter-wide activity
- strongest other non-system GPU workload on the same adapter retained as context
- conservative 20% first-pass concurrent-workload significance threshold
- adapter-wide fallback when per-process attribution is unavailable
- no fake `adapter - Star Citizen` subtraction
- foreground/background context based only on owning PID/process name; no window-title capture
- final-window workload and focus summaries remain contextual and do not establish contention or cause
- background GPU counter sampling prevents expensive Windows counter enumeration from continuously blocking the WPF UI

Validated environment fingerprinting:

- schema-v5 `environment_fingerprint` record at real session start
- Star Citizen executable file/product version, size, and modification time
- Windows build, CPU, logical CPU count, and installed RAM
- display-driver metadata and PresentMon version
- `USER.cfg` presence, selected `g_language`, metadata, and SHA-256 without recording contents
- selected localization `global.ini` metadata and SHA-256 without recording contents
- `Data.p4k` size/modification metadata without hashing or unpacking it
- no absolute Star Citizen installation paths stored in the fingerprint

Real-machine validation completed for alpha.7 includes clean exit-code `0` sessions, active-vs-recovered memory-pressure behavior, concurrent GPU workload attribution, foreground/focus persistence, recurring incident signatures, and the post-GPU-threading responsiveness pass.

Alpha.7 deliberately distinguishes **correlation from causation**. Crash signatures, telemetry precursors, foreground state, concurrent workloads, and repeated incidents are evidence to preserve and test—not automatic proof of root cause.

Natural-evidence follow-ups remain available for later refinement without blocking alpha.7 closure:

- deeper parsing of authentic crash-handler payload / GPU diagnostic contents after a natural Star Citizen crash provides validated artifacts
- additional Windows System-log failure signatures beyond Display Event 4101
- richer crash/driver-reset signatures as real-world evidence is encountered
- environment-fingerprint comparison between known-good and degraded/failed sessions
- broader validation of concurrent-workload significance thresholds

## Current development

### v0.1.0-alpha.8 — Pulse Report

Turn the validated session evidence into an understandable, stable report layer.

A Pulse Report should answer:

1. **What happened?**
2. **When did it happen / what changed beforehand?**
3. **What does the evidence support?**
4. **What evidence supports that assessment?**
5. **Is any evidence contradictory?**
6. **How confident is the assessment?**
7. **What should the player test next?**

Alpha.8 foundation now implemented:

- project/version metadata advanced to `v0.1.0-alpha.8`
- structured `PulseReport` contract
- structured timeline item contract
- separate supporting-evidence and contradictory-evidence collections
- deterministic oldest-to-newest timeline ordering
- evidence trimming/deduplication for report presentation
- conservative adapter from alpha.7 `IncidentReport` output
- normal exits explicitly avoid inferring a crash/performance root cause
- contradictory termination reports remain unresolved rather than being presented as a probable cause
- recurring/correlated abnormal reports preserve the statement that repeatability/correlation does not prove root cause
- recommended alpha.7 next-test guidance carries into the report unchanged
- complete final 60-second Pulse Event timeline buffer for report construction while the live panel remains limited to its compact recent-event view
- exact 60-second boundary inclusion with older/future events excluded from the report timeline
- Pulse Report object now built automatically after both ordinary and late-evidence incident finalization
- ORL-inspired typography foundation: Inter-first UI text with Windows-native fallbacks and a dedicated mono family for telemetry/status data
- dedicated Pulse Report regression project
- Pulse Report regression suite added to Windows CI

Near-term alpha.8 work:

- add report summaries for environment fingerprint changes and concurrent workload/focus context
- design the in-app Pulse Report view without disrupting the validated live telemetry shell
- distinguish a report's **session outcome** from any stronger **likely-cause assessment** so the UI cannot accidentally present an abnormal exit title as a proven cause
- persist/export a stable report representation only after the report contract is regression-stable
- add a local export suitable for support/community sharing
- include privacy-safe environment/build context needed to make a shared report interpretable
- keep export explicit and local; no automatic upload/cloud account requirement
- add regression coverage for rendering/export semantics and privacy boundaries

The alpha.8 presentation layer must **not** weaken alpha.7's evidence rules. If the evidence is unresolved, contradictory, or merely correlated, Pulse Report must say so.

### v0.1.0-alpha.9 — PulseCompare

Add controlled before-and-after testing.

Examples:

- graphics setting A vs B
- resolution / upscaler changes
- driver changes
- Windows configuration changes
- hardware changes
- known-good vs degraded/failed environment fingerprints

The goal is to answer **whether a controlled change actually improved the Star Citizen experience**, using recorded evidence rather than subjective impressions alone.

Planned comparison context includes:

- FPS / frame-time distributions
- PulseCheck classifications and confidence
- Pulse Events and incident outcomes
- Star Citizen-specific vs adapter-wide GPU behavior
- concurrent workload / foreground context
- environment fingerprint differences
- repeatability across multiple sessions where enough data exists

## Pre-public UX / Visual Polish

After alpha.9, perform a dedicated application-wide UI/UX pass before the first broad tester build. This is a deliberate milestone rather than incidental cleanup during feature work.

Planned polish areas:

- complete Inter + mono typography audit across live telemetry, Incident Forensics, Pulse Report, and PulseCompare
- spacing, alignment, card-height, wrapping, and truncation consistency
- high-DPI behavior and minimum-window/resizing validation
- presentation-friendly process names while preserving raw process names in recorded evidence where useful
- taskbar/application identity and icon consistency
- system-tray integration with explicit Exit
- optional start-minimized / Start with Windows behavior rather than silent startup changes
- hover/focus/keyboard states and general Windows interaction polish
- visual consistency between PulseCheck, Pulse Events, Incident Forensics, Pulse Report, and PulseCompare
- final Violet Frost palette audit so semantic warning/critical/healthy states remain readable
- packaging/install/remove/upgrade tester experience

The goal is to enter public testing with one coherent product surface rather than a collection of individually polished feature panels.

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
  ↓
Review / export Pulse Report
```

Public users should not need Git, PowerShell, a .NET SDK, or manual developer setup.

Pre-public packaging work includes:

- self-contained Windows x64 packaging
- reliable application/taskbar identity and icon behavior
- third-party notices / PresentMon redistribution verification
- tested upgrade/removal behavior
- public release notes and SHA-256 verification information

## Longer-term possibilities

Only after the forensic core and report layer are reliable:

- searchable session / incident archive
- patch-to-patch comparisons
- hardware/configuration baselines
- richer per-core/thread correlation where Windows telemetry permits it safely
- stutter classification
- community-shareable anonymized diagnostic reports with explicit user opt-in
- local rules/signature updates without weakening privacy or safety

## Non-goals

Cosmic Pulse is not currently intended to become:

- a trading assistant
- a cargo/mining/salvage calculator
- a fleet manager
- a navigation database
- a general Star Citizen wiki client
- a gameplay automation tool
- an injected overlay
- a localization replacement or game-file modification tool

These boundaries keep the project focused on a specific job: **performance and reliability forensics for Star Citizen**.
