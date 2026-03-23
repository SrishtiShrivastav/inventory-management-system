from fastapi import FastAPI
from app.database.db import Base, engine
from app.routers import item_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item_router.router)
