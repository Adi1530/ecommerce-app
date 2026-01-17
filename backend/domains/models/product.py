from sqlalchemy import Column, Integer, String, Float, Boolean
from backend.domains.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    is_active = Column(Boolean, default=True)

