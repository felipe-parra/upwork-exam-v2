from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.favorite import user_favorite_profiles

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    profiles = relationship("Profile", back_populates="user")
    favorites_profiles = relationship("Profile", secondary=user_favorite_profiles,
                                      back_populates="favorited_by")
