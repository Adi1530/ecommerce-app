from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from backend.domains.core.database import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_amount = Column(Float)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
