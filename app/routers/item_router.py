from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.services import item_service

router = APIRouter()

@router.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)

@router.get("/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return item_service.get_items(db)

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.delete_item(db, item_id)
