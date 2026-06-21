from fastapi import FastAPI
from app.api.v1 import router
from app.db.init_db import init_db

app = FastAPI(
    title="FinanceAPI",
    description="API REST for finance pessoal management",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FinanceAPI is running 🚀"}
