from dataclasses import dataclass


@dataclass(frozen=True)
class ChargedScrap:
    amount_charged_t: float
    scrap_id: str
