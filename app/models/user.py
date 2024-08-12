from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    subscription_tier = Column(String(50), nullable=False, default="free")
    createdAt = Column(TIMESTAMP, server_default=func.now())
    updatedAt = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    deletedAt = Column(TIMESTAMP, nullable=True)

    predictions = relationship("UserPrediction", back_populates="user")