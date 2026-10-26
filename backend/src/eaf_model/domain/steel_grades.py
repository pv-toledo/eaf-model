from dataclasses import dataclass


@dataclass(frozen=True)
class ElementLimit:
    element: str
    min_pct: float | None
    max_pct: float | None


@dataclass(frozen=True)
class Steel:
    id: str
    name: str
    element_limits: list[ElementLimit]
