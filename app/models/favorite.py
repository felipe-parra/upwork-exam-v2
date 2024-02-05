from sqlalchemy import Column, Integer, Table, ForeignKey
from app.database import Base

user_favorite_profiles = Table('favorites', Base.metadata,
                               Column('user_id', Integer,
                                      ForeignKey('users.id')),
                               Column('profile_id', Integer,
                                      ForeignKey('profiles.id'))
                               )
