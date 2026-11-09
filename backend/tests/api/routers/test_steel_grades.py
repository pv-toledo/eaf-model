from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.steel_grades import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_list_default_steel_grades():
    response = client.get("/steel-grades")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    steel_grade_ids = {steel_grade["id"] for steel_grade in data}

    assert "low_carbon" in steel_grade_ids
    assert "structural" in steel_grade_ids
    assert "high_carbon" in steel_grade_ids
