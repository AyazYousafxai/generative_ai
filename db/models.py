from sqlalchemy.dialects.postgresql import UUID as UUIDType
# from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4
from sqlalchemy import (
    Boolean,
    Column,
    String,
    ForeignKey,
    ForeignKey,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(
         UUIDType(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
        index=True,
    )
    name = Column(String(length=100), index=True)
    password=Column(String)
    email = Column(String(length=30), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())
    recommendations = relationship("Recommendation", back_populates="user", cascade="all, delete")


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column( UUIDType(as_uuid=True),default=uuid4, primary_key=True, index=True)
    user_id = Column( UUIDType(as_uuid=True),ForeignKey("users.id"))
    city = Column(String, index=True)
    activity = Column(String)
    outfit = Column(String)
    summary = Column(String)
    user = relationship("User", back_populates="recommendations",cascade="all, delete")