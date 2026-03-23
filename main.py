from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

inventory = []

class Item(BaseModel):
    name: str
    quantity: int

@app.get("/")
def home():
    return {"message": "Inventory API running"}

@app.get("/items")
def get_items():
    return inventory

@app.post("/items")
def add_item(item: Item):
    inventory.append(item)
    return {"message": "Item added", "item": item}
