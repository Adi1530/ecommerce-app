"""
User business logic .creating users and authenticating them.

"""

from pydantic import EmailStr
from sqlalchemy.orm import Session

from backend.domains.core.hashing import hash_password, verify_password
from backend.domains.models.user import User
from backend.domains.schemas.user_process import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: EmailStr, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, str(user.hashed_password)):
        return None
    return user
