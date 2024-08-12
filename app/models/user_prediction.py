from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func

class UserPrediction(Base):
    __tablename__ = "user_predictions"

    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    category = Column(String(100), nullable=False)
    size = Column(Integer, nullable=False)
    type = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    content_rating = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    current_version = Column(String(100), nullable=False)
    android_version = Column(String(100), nullable=False)
    sentiment = Column(Integer, nullable=False)
    success_rate = Column(Float, nullable=False)
    tips = Column(String(255), nullable=True)
    createdAt = Column(TIMESTAMP, server_default=func.now())
    updatedAt = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    deletedAt = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="predictions")