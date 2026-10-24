import json
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


def load_default_steel_grades(path: str) -> list[Steel]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            Steel(
                id=item["id"],
                name=item["name"],
                element_limits=[
                    ElementLimit(
                        element=limit["element"], max_pct=limit["max_pct"], min_pct=limit["min_pct"]
                    )
                    for limit in item["element_limits"]
                ],
            )
            for item in raw_data
        ]
