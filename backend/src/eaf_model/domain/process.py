import json
from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessParameters:
    tap_temperature_c: float
    electrode_kg_per_t_liquid: float
    dust_loss_kg_per_t_charge: float
    slag_feo_pct: float
    ch4_nm3_per_t_charge: float
    post_combustion_pct: float
    electric_energy_loss_pct: float


def load_default_process_parameters(path: str) -> list[ProcessParameters]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            ProcessParameters(
                tap_temperature_c=raw_data["tap_temperature_c"],
                electric_energy_loss_pct=raw_data["electrode_kg_per_t_liquid"],
                dust_loss_kg_per_t_charge=raw_data["dust_loss_kg_per_t_charge"],
                slag_feo_pct=raw_data["slag_feo_pct"],
                ch4_nm3_per_t_charge=raw_data["ch4_nm3_per_t_charge"],
                post_combustion_pct=raw_data["post_combustion_pct"],
                electrode_kg_per_t_liquid=raw_data["electric_energy_loss_pct"],
            )
        ]
