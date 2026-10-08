from types import MappingProxyType
from typing import Final

# ---------------------- ELEMENT, OXIDES AND GAS MASSES (g/mol) -------------------------------

_element_masses = {
    "fe": 55.845,
    "h": 1.008,
    "h2": 2.016,
    "o": 15.999,
    "c": 12.011,
    "si": 28.086,
    "mn": 54.938,
    "p": 30.974,
    "s": 32.065,
    # "cr": 51.996,
    # "ni": 58.693,
}

ELEMENT_MASSES_G_PER_MOL: Final = MappingProxyType(_element_masses)

_oxide_masses = {
    "feo": 159.687,
    "sio2": 60.084,
    "mno": 70.937,
    "al2o3": 101.960,
    "cao": 56.077,
    "mgo": 40.304,
}

OXIDE_MASSES_G_PER_MOL: Final = MappingProxyType(_oxide_masses)

_gas_masses = {"co": 28.010, "co2": 44.009, "ch4": 16.042}

GAS_MASSES_G_PER_MOL: Final = MappingProxyType(_gas_masses)

# ------------------- ENTHALPIES OF FORMATION AT 298K (kcal/kg) -------------------------------

_enthalpies_of_formation = {
    "co": -943.23,
    "co2": -2137.02,
    "sio2": -3621.60,
    "mno": -1296.95,
    "p2o5": -2512.98,
    # "cr2o3": -1776.45,
    "feo": -879.96,
}

ENTHALPIES_OF_FORMATION_KCAL_PER_KG: Final = MappingProxyType(_enthalpies_of_formation)

# ------------------- HEAT CAPACITY (kcal/kg) -------------------------------

_heat_capacity = {
    
    "co": {"t_min": 298, "t_max": 2000, "a": -124.9, "b": 0.3043},
    "co2": {"t_min": 298, "t_max": 2000, "a": -147.4, "b": 0.3217},
    "h2": {"t_min": 298, "t_max": 2000, "a": -1582.7, "b": 3.9227},

    "sio2": {"t_min": 298, "t_max": 2000, "a": -23.9, "b": 0.3200},
    "mno": {"t_min": 298, "t_max": 2000, "a": -167.6, "b": 0.3200},
    "p2o5": {"t_min": 298, "t_max": 2000, "a": -108.0, "b": 0.3200},
    "feo": {"t_min": 298, "t_max": 2000, "a": -17.4, "b": 0.2366},
    "al2o3": {"t_min": 298, "t_max": 2000, "a": -8.4, "b": 0.3200},
    "cao": {"t_min": 298, "t_max": 2000, "a": -104.0, "b": 0.3200},
    "mgo": {"t_min": 298, "t_max": 2000, "a": 5.0, "b": 0.3200},

    "fe": {"t_min": 298, "t_max": 2000, "a": -46.3, "b": 0.1969},
    "c": {"t_min": 298, "t_max": 2000, "a": -260.0, "b": 0.4812},
    "si": {"t_min": 298, "t_max": 2000, "a": 369.7, "b": 0.2171},
    "mn": {"t_min": 298, "t_max": 2000, "a": -34.3, "b": 0.2002},
    "s": {"t_min": 298, "t_max": 2000, "a": 47.5, "b": 0.1401},
    "o": {"t_min": 298, "t_max": 2000, "a": -108.0, "b": 0.3200},
    "p":  {"t_min": 298, "t_max": 2000, "a": -48.2, "b": 0.1431}
}