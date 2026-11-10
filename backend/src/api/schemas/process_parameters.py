from pydantic import BaseModel


class ProcessParameters(BaseModel):
    tap_temperature_c: float
    electrode_kg_per_t_liquid: float
    dust_loss_kg_per_t_charge: float
    slag_feo_pct: float
    slag_mgo_saturation_pct: float
    slag_basicity: float
    ch4_nm3_per_t_charge: float
    post_combustion_pct: float
    electric_energy_loss_pct: float
