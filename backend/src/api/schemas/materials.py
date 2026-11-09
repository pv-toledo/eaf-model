from pydantic import BaseModel, ConfigDict


class MaterialsComposition(BaseModel):
    fe: float
    c: float
    si: float
    mn: float
    p: float
    s: float

    cao: float
    sio2: float
    al2o3: float
    mgo: float
    feo: float


class Scrap(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    price_usd_per_t: float
    metallic_yield_pct: float

    composition_pct: MaterialsComposition


class AlloysAndFluxes(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    price_usd_per_t: float

    composition_pct: MaterialsComposition
