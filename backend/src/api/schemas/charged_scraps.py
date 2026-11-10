from pydantic import BaseModel


class ChargedScraps(BaseModel):
    pct_of_metallic_mix: float
    scrap_id: str
