from fastapi import FastAPI

from routers import auth
from routers import branches
from routers import tables
from routers import reservations

app = FastAPI(
    title="DineReserve Hub API"
)

app.include_router(auth.router)
app.include_router(branches.router)
app.include_router(tables.router)
app.include_router(reservations.router)

@app.get("/")
def home():
    return {
        "message": "DineReserve Hub Running"
    }