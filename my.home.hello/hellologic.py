"""Logic without the broker, so it can be tested with plain pytest."""

from typing import Any


def period(settings: dict[str, Any], default: float = 60) -> float:
    try:
        return max(5.0, float(settings.get("period") or default))
    except TypeError, ValueError:
        return default


def is_round(n: int, every: Any) -> bool:
    try:
        step = int(every)
    except TypeError, ValueError:
        step = 10
    return step > 0 and n > 0 and n % step == 0


def page(n: int) -> dict[str, Any]:
    return {"blocks": [{"type": "hero", "icon": "spark", "tone": "ok", "value": n, "digits": 0, "text": "ticks"}]}
