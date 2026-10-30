import json

from eaf_model.domain.constraints import ChargeConstraint, ScrapLimit
from eaf_model.domain.materials import Material, Scrap
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.scenario import ChargedScrap
from eaf_model.domain.steel_grades import ElementLimit, Steel


def load_default_metallic_mix(
    charged_scraps_path: str, charged_constraints_path: str
) -> dict[str, float]:
    with (
        open(charged_scraps_path) as charged_scraps,
        open(charged_constraints_path) as charge_constraints,
    ):
        charged_scraps = json.load(charged_scraps)
        charge_constraints = json.load(charge_constraints)

        basket_capacity_t = charge_constraints["basket_capacity_t"]
        metallic_mix = {}

        for item in charged_scraps:
            metallic_mix[item["scrap_id"]] = item["amount_charged_t"] * basket_capacity_t / 100
        return metallic_mix


def load_default_scrap_catalog(path: str) -> list[Scrap]:
    with open(path) as file:
        raw_data = json.load(file)

    return [
        Scrap(
            id=item["id"],
            name=item["name"],
            price_usd_per_t=item["price_usd_per_t"],
            metallic_yield_pct=item["metallic_yield_pct"],
            composition_pct=item["composition_pct"],
        )
        for item in raw_data
    ]


def load_default_charge_constraints(path: str) -> list[ChargeConstraint]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            ChargeConstraint(
                basket_capacity_t=raw_data["basket_capacity_t"],
                scrap_limits=[
                    ScrapLimit(
                        material_id=limit["material_id"],
                        min_pct=limit["min_pct"],
                        max_pct=limit["max_pct"],
                    )
                    for limit in raw_data["scrap_limits"]
                ],
            )
        ]


def load_default_materials(path: str) -> list[Material]:
    with open(path) as file:
        raw_data = json.load(file)

    return [
        Material(
            id=item["id"],
            name=item["name"],
            price_usd_per_t=item["price_usd_per_t"],
            composition_pct=item["composition_pct"],
        )
        for item in raw_data
    ]


def load_default_process_parameters(path: str) -> ProcessParameters:
    with open(path) as file:
        raw_data = json.load(file)

        return ProcessParameters(
            tap_temperature_c=raw_data["tap_temperature_c"],
            electric_energy_loss_pct=raw_data["electrode_kg_per_t_liquid"],
            dust_loss_kg_per_t_charge=raw_data["dust_loss_kg_per_t_charge"],
            slag_feo_pct=raw_data["slag_feo_pct"],
            slag_mgo_saturation_pct=raw_data["slag_mgo_saturation_pct"],
            slag_bascity=raw_data["slag_basicity"],
            ch4_nm3_per_t_charge=raw_data["ch4_nm3_per_t_charge"],
            post_combustion_pct=raw_data["post_combustion_pct"],
            electrode_kg_per_t_liquid=raw_data["electric_energy_loss_pct"],
        )


def load_default_scenario(path: str) -> list[ChargedScrap]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            ChargedScrap(scrap_id=item["scrap_id"], amount_charged_t=item["amount_charged_t"])
            for item in raw_data
        ]


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


def load_selected_steel_grade(
    default_steel_grades: list[Steel], steel_id: str = "low_carbon"
) -> Steel:
    return next(steel for steel in default_steel_grades if steel.id == steel_id)
