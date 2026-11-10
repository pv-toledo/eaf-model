from dataclasses import dataclass


@dataclass(frozen=True)
class ChargedScrap:
    pct_of_metallic_mix: float
    scrap_id: str
