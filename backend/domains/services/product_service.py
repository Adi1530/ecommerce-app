from sqlalchemy.orm import Session
from backend.domains.models.product import Product
from backend.domains.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db.product)
    return db_product


def get_active_products(db: Session):
    return db.query(Product).filter(Product.is_active == True).all()

def soft_delete_product(db: Session, product_id: int):
    product = db.query(Product).get(product_id)
    if product:
        product.is_active = False
        db.commit()