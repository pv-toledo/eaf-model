from typing import Final
from types import MappingProxyType

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
    "ni": 58.693 
} 

ELEMENT_MASSES: Final = MappingProxyType(_element_masses)

_oxide_masses = {
    "feo":  159.687,
    "sio2": 60.084,
    "mno": 70.937,
    "al2o3": 101.960,
    "cao": 56.077,
    "mgo": 40.304
}

OXIDE_MASSES: Final = MappingProxyType(_oxide_masses)

_gas_masses = {
    "co": 28.010,
    "co2": 44.009,
    "ch4": 16.042
}

GAS_MASSES: Final = MappingProxyType(_gas_masses)

# ------------------- ENTHALPIES OF FORMATION AT 298K (kcal/mol) -------------------------------

_enthalpies_of_formation = {
    "co": -26.42,
    "co2": -94.05,
    "sio2": -217.60,
    "mno": -92.00,
    "p2o5": -356.60,
    "cr2o3": -270.00,
    "feo": -63.20
}

ENTHALPIES_OF_FORMATION: Final = MappingProxyType(_enthalpies_of_formation)