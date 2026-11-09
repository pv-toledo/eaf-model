from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import materials, steel_grades

app = FastAPI(title="eaf-model")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(materials.router)
app.include_router(steel_grades.router)


@app.get("/health")
def health():
    return {"status": "ok"}
