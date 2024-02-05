from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.database import Base

# Tabla de relación many-to-many
user_favorite_profiles = Table('favorites', Base.metadata,
                               Column('user_id', Integer,
                                      ForeignKey('users.id')),
                               Column('profile_id', Integer,
                                      ForeignKey('profiles.id'))
                               )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    profiles = relationship("profiles", back_populates="user")
    favorites_profiles = relationship("Profile", secondary=user_favorite_profiles,
                                      back_populates="favorited_by")
