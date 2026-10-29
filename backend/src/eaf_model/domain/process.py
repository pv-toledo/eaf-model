from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessParameters:
    tap_temperature_c: float
    electrode_kg_per_t_liquid: float
    dust_loss_kg_per_t_charge: float
    slag_feo_pct: float
    slag_bascity: float
    ch4_nm3_per_t_charge: float
    post_combustion_pct: float
    electric_energy_loss_pct: float
