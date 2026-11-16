# Smoked Glass

A standalone **dark-only** Hermes skin: smoked charcoal surfaces, restrained mint
highlights and softer Desktop controls. The complete skin is
[`extras/smoked-glass.yaml`](../extras/smoked-glass.yaml).

## What changes

- Rounded sidebar panels, conversation rows, menus and composer surfaces.
- Softer selected-row highlights and matching working-state outlines.
- Quieter timestamps, token figures and other small secondary labels; those
  labels brighten on hover or keyboard focus. Titles and status dots stay clear.
- Matching rounded search, pane tabs and small native toolbar buttons, with
  visible hover and keyboard-focus treatments.
- Reduced-motion and reduced-transparency accommodations.

This is a **theme-only** change. It does not install or modify a plugin, change
native window transparency, alter fonts, move panes or replace navigation.

## Why this is an extra

The stock collection in `themes/` is generated and expects opposite-polarity
fallback palettes. Smoked Glass intentionally keeps `colors`, `dark_colors` and
`light_colors` dark, so its fixed dark Desktop surfaces never sit over an
incompatible light text palette. It has no separate light twin.

It therefore lives in `extras/`, outside the stock generator, gallery and
`install.sh`. Install this file individually. Do not run the full pack installer
just to get Smoked Glass.

## Install or update

On **the computer or backend host that owns your active Hermes profile**, run the
following from the root of this repository. These shell commands are for macOS or
Linux. If Desktop connects to a remote backend, that backend owns the profile's
skin directory.

First, record your previous skin for rollback:

```sh
hermes config get display.skin
```

Copy the standalone file, preserving an existing Smoked Glass installation:

```sh
hermes_home="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$hermes_home/skins"
if [ -f "$hermes_home/skins/smoked-glass.yaml" ]; then
  mkdir -p "$hermes_home/skin-backups"
  cp "$hermes_home/skins/smoked-glass.yaml" \
    "$hermes_home/skin-backups/smoked-glass-$(date +%Y%m%d-%H%M%S).yaml"
fi
cp extras/smoked-glass.yaml "$hermes_home/skins/smoked-glass.yaml"
hermes config set display.skin smoked-glass
```

On Windows, copy the same YAML into the active profile's `skins` directory and
run the same `hermes config set display.skin smoked-glass` command. No Unix shell
installer is required.

Hermes normally reloads the active skin automatically. The rounded session search
field and matching pane tabs are useful visual checks. If a build does not pick
up the update, select another theme and then Smoked Glass in Settings → Appearance.
There is no need to reload plugins or change native Glass settings.

## Roll back

On the **same Hermes host/profile**, replace `previous-skin` with the value you
recorded before installation:

```sh
hermes config set display.skin previous-skin
```

Switching away removes Smoked Glass's injected CSS. To undo only an update while
keeping Smoked Glass selected, copy your saved YAML backup back to
`$hermes_home/skins/smoked-glass.yaml`.

## Compatibility and limits

- The palette applies to the CLI, TUI and Desktop. The `customCSS` block is for
  GUI surfaces; the CLI and TUI ignore it.
- The detailed styling targets Hermes Desktop's native sidebar/session rows,
  SearchField, PaneTab and icon-button markup. It is not a replacement interface
  and does not claim to reproduce the Desktop layout in the web dashboard.
- Native wallpaper blur is separate from CSS surface styling. Existing native
  window-translucency settings are left alone, including when already enabled.
- Selecting a light appearance does not turn this intentionally dark-only skin
  into a light theme.
- Skin files survive app updates, but Desktop selectors can change. If controls
  stop matching after an update, inspect the installed markup before adjusting
  the CSS; do not modify the app package or install a plugin as a workaround.

Official reference: [Hermes skins and custom CSS](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins#raw-customcss).

## Validation

After setting up the repository's development dependencies as described in
[CONTRIBUTING.md](../CONTRIBUTING.md), run on **your development computer**, from
the repository root:

```sh
python -m pytest tests/test_smoked_glass.py -q
python -m pytest tests/ -q
```

The portable tests check the schema, deliberate dark-only palette slots, palette
contrast, local-only CSS, size limit, and discoverable installation guidance.
They do not substitute for a visual check in the installed Desktop build. During
styling work, verify metadata readability, selection/hover, focus rings, disabled
controls, narrow sidebars and drag/close affordances against that build's own
stylesheet. Keep private conversations and screenshots out of public test data.
