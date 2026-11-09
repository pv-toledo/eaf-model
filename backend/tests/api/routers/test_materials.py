from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.materials import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_list_scraps_from_default_catalog():
    response = client.get("/scraps")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    scrap_ids = {scrap["id"] for scrap in data}

    assert "pig_iron" in scrap_ids
    assert "shredded" in scrap_ids
    assert "hbi" in scrap_ids
