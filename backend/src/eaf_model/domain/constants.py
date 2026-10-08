from types import MappingProxyType
from typing import Final

# ---------------------- ELEMENT, OXIDES AND GAS MASSES (g/mol) -------------------------------

_element_masses = {
    "fe": 55.845,
    "h": 1.008,
    "o": 15.999,
    "c": 12.011,
    "si": 28.086,
    "mn": 54.938,
    "p": 30.974,
    "s": 32.065,
    "cr": 51.996,
    "ni": 58.693,
}

ELEMENT_MASSES: Final = MappingProxyType(_element_masses)

_oxide_masses = {
    "feo": 159.687,
    "sio2": 60.084,
    "mno": 70.937,
    "al2o3": 101.960,
    "cao": 56.077,
    "mgo": 40.304,
}

OXIDE_MASSES: Final = MappingProxyType(_oxide_masses)

_gas_masses = {"co": 28.010, "co2": 44.009, "ch4": 16.042}

GAS_MASSES: Final = MappingProxyType(_gas_masses)

# ------------------- ENTHALPIES OF FORMATION AT 298K (kcal/mol) -------------------------------

_enthalpies_of_formation = {
    "co": -26.42,
    "co2": -94.05,
    "sio2": -217.60,
    "mno": -92.00,
    "p2o5": -356.60,
    "cr2o3": -270.00,
    "feo": -63.20,
}

ENTHALPIES_OF_FORMATION: Final = MappingProxyType(_enthalpies_of_formation)

# ------------------ HEAT CAPACITY (cal/mol.K) - a + bT + cT^(-2) ----------------------------------------

_heat_capacity = {
    "co": {"t_min": 298, "t_max": 2500, "a": 6.9, "b": 0.00098, "c": -11000},
    "co2": {"t_min": 298, "t_max": 2500, "a": 10.55, "b": 0.00216, "c": -204000},
    "sio2": [
        {"t_min": 298, "t_max": 390, "a": 3.27, "b": 0.0248, "c": 0},
        {"t_min": 391, "t_max": 2000, "a": 13.64, "b": 0.00264, "c": 0},
    ],
    "mno": {"t_min": 298, "t_max": 1800, "a": 11.11, "b": 0.00194, "c": -88000},
    "p2o5": {"t_min": 298, "t_max": 2500, "a": 17.9, "b": 0.0388, "c": -373000}, #approx
    "cr2o3": {"t_min": 298, "t_max": 1800, "a": 28.53, "b": 0.0022, "c": -374000}, #approx
    "feo": {"t_min": 298, "t_max": 2500, "a": 28.53, "b": 0.0022, "c": -374000}, #approx
    "ni":  [
        {"t_min": 298, "t_max": 633, "a": 4.06, "b": 0.00704, "c": 0},
        {"t_min": 634, "t_max": 1728, "a": 6, "b": 0.0018, "c": 0},
        {"t_min": 1729, "t_max": 2000, "a": 9.2, "b": 0, "c": 0},
    ],
    "al2o3": {"t_min": 298, "t_max": 1800, "a": 25.48, "b": 0.00425, "c": -682000},
    "cao": {"t_min": 298, "t_max": 2000, "a": 11.86, "b": 0.00108, "c": -166000}, #approx
    "mgo": {"t_min": 298, "t_max": 3098, "a": 11.71, "b": 0.00075, "c": -280000},
    "fe": [
            {"t_min": 298, "t_max": 1809, "a": 8.873, "b": 0.00147, "c": 0},
            {"t_min": 1810, "t_max": 2000, "a": 10, "b": 0, "c": 0}, #approx
        ],
    "s": [
            {"t_min": 298, "t_max": 718, "a": 107.5, "b": -0.2294, "c": -4992000}, #approx
            {"t_min": 718, "t_max": 2000, "a": 5.4, "b": 0.0055, "c": 0}, #approx
        ],
}
