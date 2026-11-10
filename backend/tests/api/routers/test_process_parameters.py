from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.process_parameters import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_list_default_process_parameters():
    response = client.get("/process-parameters")

    assert response.status_code == 200

    assert response.json() == {
        "tap_temperature_c": 1600.0,
        "electrode_kg_per_t_liquid": 2.0,
        "dust_loss_kg_per_t_charge": 15.0,
        "slag_feo_pct": 25.0,
        "slag_mgo_saturation_pct": 9.0,
        "slag_basicity": 2.0,
        "ch4_nm3_per_t_charge": 5.0,
        "post_combustion_pct": 20.0,
        "electric_energy_loss_pct": 20.0,
    }
