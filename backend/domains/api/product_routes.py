"""
Product routes - showing products to customers.

This module is like a store shelf. It displays all the products available for
sale and provides ways for the app to fetch and show them to customers. When
someone visits the store, these routes return the list of what's available.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.domains.core.database import SessionLocal
from backend.domains.schemas.product_schema import ProductResponse
from backend.domains.services.product_service import get_active_products

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_active_products(db)
