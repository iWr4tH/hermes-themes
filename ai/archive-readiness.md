# Smoked Glass publication handoff

## Outcome and scope

The completed Smoked Glass skin is preserved as a standalone extra. It includes
the charcoal/mint palette, scoped rounded Desktop surfaces, corrected conversation
rows, quieter metadata, and coordinated search, pane-tab and toolbar styling.

- **Skin:** [extras/smoked-glass.yaml](../extras/smoked-glass.yaml)
- **Human runbook:** [installation, update, rollback and compatibility](../docs/smoked-glass.md)
- **Discovery:** the README's Fork extras section and the Unreleased changelog.
- **Portable checks:** `tests/test_smoked_glass.py`, run by the normal test suite.

The extra is deliberately dark-only and is not part of the stock generator,
light/dark pair map, gallery or bulk installer. Stock themes and plugin code remain
unchanged. The publication contains no live profile configuration, private
screenshots, session content or machine-specific paths.

## Verification evidence

- The full repository pytest suite passed: **28 tests**.
- The public skin passed **27 isolated rendering checks** against the installed
  Desktop stylesheet: metadata contrast/hierarchy, controls, focus/hover, disabled
  states, preserved fonts/geometry, narrow sidebar and reduced motion.
- Those rendering checks are local development evidence, not an added CI job.
  Native live-window capture was unavailable for the final polish pass; do not
  represent the isolated component rendering as a live Desktop screenshot.
- The published YAML mapping is checked against the accepted installed skin;
  only the introductory comment and insignificant blank-line whitespace differ.
- No live theme, native transparency, plugin or configuration change is part of
  this repository publication.

## Integration and continuation

**State: preserved on a task branch; owner review and merge remain pending.**

- Repository: [iWr4tH/hermes-themes](https://github.com/iWr4tH/hermes-themes)
- Base: `main`
- Task branch: `agent/hermes/0400069e/smoked-glass`
- [Branch comparison / review entry point](https://github.com/iWr4tH/hermes-themes/compare/main...agent/hermes/0400069e/smoked-glass)
- Agent runtime: `hermes-desktop`
- Agent ID: `local-0400069e105dc1fe625a47b52fc63ba5b2e02c12ca34bf88d8f31f9c373636ac`

This handoff does not authorize merging or claim CI is green. The GitHub PR is the
review surface; its current checks and head commit are authoritative. Keep it
open until the owner merges it or explicitly directs an agent merge.

For final wrap-up:

1. Verify the PR is merged and its merge commit is contained in remote `main`.
2. Reconcile a clean shared checkout without changing any unrelated agent work.
3. Keep the human runbook and maintained tests. Preserve the task worktree until
   integration is verified, then remove it and its local branch only when clean
   and unused. Do not delete the remote branch automatically.
4. Review and clean only this task's no-longer-needed private scratch probes and
   generated previews. They were intentionally retained during publication
   preparation; no broad scratch cleanup has been performed.

The conversation is not yet archive-ready: review/integration and final
current-task scratch cleanup remain outstanding.
