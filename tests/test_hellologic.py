import json
import pathlib

import hellologic as hl

PKG = pathlib.Path(__file__).resolve().parents[1] / "my.home.hello"


def test_period_has_a_floor_and_a_default() -> None:
    assert hl.period({"period": "1"}) == 5.0
    assert hl.period({}) == 60
    assert hl.period({"period": "x"}) == 60


def test_round_numbers() -> None:
    assert hl.is_round(20, 10) and not hl.is_round(21, 10)
    assert not hl.is_round(0, 10) and not hl.is_round(5, 0) and hl.is_round(10, "bad")


def test_manifest_matches_the_module() -> None:
    m = json.loads((PKG / "manifest.json").read_text())
    for key in ("id", "version", "module", "name", "description", "perms"):
        assert key in m, key
    src = (PKG / f"{m['module']}.py").read_text()
    for b in m.get("blocks", []):
        if b["kind"] == "trig":
            assert f'trigger("{b["key"]}"' in src
    for p in m.get("pages", []):
        assert f'@ext.page("{p["key"]}")' in src
    for lang in ("en", "uk", "ru"):
        assert (PKG / "docs" / f"{lang}.md").read_text().startswith("# ")
