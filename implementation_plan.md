# Implementation Plan: Draft Epic for ietf-geo-location

## 1. Parse Schema
- Schema: `ietf-geo-location@2022-02-11.yang`
- Extracted structural models:
  - Container `geo-location`
  - Container `reference-frame`
  - Choice `location` (cases: `ellipsoid`, `cartesian`)
  - Container `velocity`
  - Leaf `timestamp`
  - Leaf `valid-until`

## 2. Draft Epic
- File: `docs/epics/epic-01-geo-location.md`
- Content: 
  - Subsystem Component Definition (`<<component>> GeoLocationSubsystem`)
  - System-Level UML Class Diagram showing composition of `geo-location` and its children (`reference-frame`, `location`, `velocity`, `timestamp`, `valid-until`).
  - System State Machine Diagram representing the macro-level domain.
  - Tasklist of features (leaving the Issue ID generation to Step 5).

## 3. Dispatch a context-isolated subagent (Role: `Feature Spec Writer`) to draft `docs/features/feat-02-reference-frame.md`.
- Target schema node: `ietf-geo-location:geo-location/reference-frame` (excluding the `geodetic-system` child).
- Parent Epic: `epic-01-geo-location`.
- Adhere to the structural and formatting templates in `.agents/skills/schema-specification-engineering/SKILL.md` and `rules/platform-independence.md`.
- Ensure the YAML frontmatter declares exactly one schema container: `ietf-geo-location:geo-location/reference-frame`.
- Ensure the subagent runs the local validation gate and registers/synchronizes the Feature with the issue tracker.

## 4. Verify subagent completion and ensure tracker sync is successful.

## 5. Issue Tracker Sync
- Create epic issue: `gh issue create --title "..." --body-file ...`
- Sync body: `gh issue edit <ID> --body-file ...`

## 6. Report Back
- Complete the task and notify the user.
