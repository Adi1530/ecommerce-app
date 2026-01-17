from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.domains.core.database import SessionLocal
from backend.domains.schemas.product import ProductResponse
from backend.domains.services.product_service import get_active_products

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/",response_model=list[ProductResponse])
def list_products(db:Session = Depends(get_db)):
    return get_active_products(db)

