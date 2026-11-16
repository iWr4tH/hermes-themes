"""Portable contracts for the standalone, deliberately dark Smoked Glass skin."""
from pathlib import Path
import re

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIN = ROOT / "extras" / "smoked-glass.yaml"
GUIDE = ROOT / "docs" / "smoked-glass.md"


def load_skin():
    assert SKIN.is_file(), "Standalone Smoked Glass skin is missing"
    return yaml.safe_load(SKIN.read_text(encoding="utf-8"))


def luminance(color):
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def test_extra_has_a_portable_skin_schema():
    skin = load_skin()
    assert skin["name"] == SKIN.stem == "smoked-glass"
    assert skin["description"]
    for block in ("colors", "dark_colors", "light_colors"):
        assert isinstance(skin[block], dict) and skin[block]
        assert all(re.fullmatch(r"#[0-9a-fA-F]{6}", value) for value in skin[block].values())


def test_extra_deliberately_keeps_both_mode_slots_dark():
    skin = load_skin()
    assert skin["colors"] == skin["dark_colors"] == skin["light_colors"]
    assert luminance(skin["colors"]["background"]) < 0.5


@pytest.mark.parametrize("key,minimum", [("banner_text", 6.0), ("banner_dim", 4.5), ("ui_accent", 4.5)])
def test_extra_palette_clears_the_pack_contrast_gate(key, minimum):
    palette = load_skin()["colors"]
    values = sorted((luminance(palette["background"]), luminance(palette[key])))
    assert (values[1] + 0.05) / (values[0] + 0.05) >= minimum


def test_extra_css_is_local_only_and_within_the_hermes_limit():
    css = load_skin()["customCSS"]
    assert isinstance(css, str) and 0 < len(css.encode("utf-8")) <= 32768
    assert not re.search(r"@import\b|url\s*\(", css, re.IGNORECASE)
    assert not re.search(r"/Users/|/home/|[A-Z]:[\\/]Users[\\/]", css)
    assert "BEGIN smoked-glass actual-sidebar correction" in css
    assert "BEGIN smoked-glass metadata-and-controls polish" in css


def test_extra_has_discoverable_install_and_rollback_guidance():
    assert GUIDE.is_file(), "Smoked Glass usage guide is missing"
    guide = GUIDE.read_text(encoding="utf-8")
    assert "extras/smoked-glass.yaml" in guide
    assert "hermes config set display.skin smoked-glass" in guide
    assert "previous-skin" in guide
    assert "dark-only" in guide
    assert "native" in guide.lower() and "plugin" in guide.lower()
    assert "docs/smoked-glass.md" in (ROOT / "README.md").read_text(encoding="utf-8")
