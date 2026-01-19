"""
Authentication routes - handling user login and registration.

This module manages all the doors to our app - it's where users create new accounts
and log in. When someone registers, we securely save their info. When they log in,
we verify their password and give them a special token (like a key card) to access
the rest of the app.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.domains.core.auth import create_access_token
from backend.domains.core.database import SessionLocal
from backend.domains.schemas.user_process import UserCreate, UserLogin
from backend.domains.services.user_services import (authenticate_user,
                                                    create_user)

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return {
        "id": db_user.id,
        "email": db_user.email,
        "message": "User registered successfully",
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}
