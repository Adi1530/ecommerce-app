"""
User data model - how we store user information in the database.

This defines the structure of a User in our system. Each user has an ID (unique),
an email (also unique - no duplicates!), a hashed password (for security), and a
role that says whether they're a regular user or an admin. Think of this as a
template for saving user information in our database.
"""

import enum

from sqlalchemy import Column, Integer, String

from backend.domains.core.database import Base


class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default=UserRole.USER.value)
