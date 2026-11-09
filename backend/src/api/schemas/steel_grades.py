from pydantic import BaseModel, ConfigDict


class ElementLimit(BaseModel):
    element: str
    min_pct: float | None
    max_pct: float | None


class SteelGrade(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str

    element_limits: list[ElementLimit]
