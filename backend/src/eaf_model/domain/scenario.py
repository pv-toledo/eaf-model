import json
from dataclasses import dataclass


@dataclass(frozen=True)
class ChargedScrap:
    amount_charged_t: float
    scrap_id: str


def load_default_scenario(path: str) -> list[ChargedScrap]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            ChargedScrap(scrap_id=item["scrap_id"], amount_charged_t=item["amount_charged_t"])
            for item in raw_data
        ]
