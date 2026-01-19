"""
Product business logic - managing products in our store.

This module handles all the work with products. It can add new products,
get the list of active (available) products to display, and remove products
from sale by marking them as inactive. It's the "warehouse manager" for our store.
"""

from sqlalchemy.orm import Session

from backend.domains.models.product import Product
from backend.domains.schemas.product_schema import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_active_products(db: Session):
    return db.query(Product).filter(Product.is_active).all()


def soft_delete_product(db: Session, product_id: int):
    product = db.query(Product).get(product_id)
    if product:
        product.is_active = False
        db.commit()
