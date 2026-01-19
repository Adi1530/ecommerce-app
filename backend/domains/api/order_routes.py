from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.domains.core.database import SessionLocal
from backend.domains.core.dependencies import get_current_user
from backend.domains.models.user import User

router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/checkout")
def checkout(
    checkout_data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Checkout endpoint to create orders
    Expected JSON: {
        "items": [{"product_id": 1, "quantity": 2, "price": 100}],
        "address": "123 Main St",
        "total_amount": 200
    }
    """
    from backend.domains.models.order import OrderDetail

    items = checkout_data.get("items", [])
    address = checkout_data.get("address", "")

    if not items or not address:
        raise HTTPException(status_code=400, detail="Items and address required")

    try:
        for item in items:
            order = OrderDetail(
                user_id=current_user.id,
                product_id=item["product_id"],
                quantity=item["quantity"],
                total_amount=item["price"] * item["quantity"],
                address=address,
            )
            db.add(order)

        db.commit()
        return {"status": "success", "message": "Order placed successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/my-orders")
def get_user_orders(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """Get all orders for current user"""
    from backend.domains.models.order import OrderDetail

    orders = db.query(OrderDetail).filter(OrderDetail.user_id == current_user.id).all()
    return orders


@router.get("/all-orders")
def get_all_orders(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """Get all orders (admin only)"""
    from backend.domains.models.order import OrderDetail
    from backend.domains.models.user import UserRole

    if current_user.role != UserRole.ADMIN.value:
        raise HTTPException(status_code=403, detail="Admin access required")

    orders = db.query(OrderDetail).all()
    return orders
