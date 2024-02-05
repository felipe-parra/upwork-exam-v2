from typing import List
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.favorite import user_favorite_profiles
from app.models.profile import Profile
from app.schemas.user import UserCreate


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Get all users
    """
    return db.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    """
    Get a single user by id
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Get a single user by email
    """
    print("get_user_by_email->", email)
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a single user, with email & name
    """
    new_user = User(email=user.email, name=user.name)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, name: str, email: str,):
    """
    Update a single user by, can update email & name
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.email = email
        db.commit()
        db.refresh(user)
        return user
    return None


def delete_user(db: Session, user_id: int):
    """
    Delete a single user by
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None


def get_favorites_for_user(db: Session, user_id: int):
    """
    Get favorites profiles by user
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user.favorites_profiles
    return None


def create_favorite_profile(db: Session, user_id: int, profile_id: int):
    """
    Create a favorite profile
    """
    favorite_profile = user_favorite_profiles.insert().values(
        user_id=user_id, profile_id=profile_id)
    db.execute(favorite_profile)
    db.commit()


def get_user_favorite_profiles(db: Session, user_id: int):
    """
    Get favorites profiles by user id
    """
    return db.query(Profile).join(user_favorite_profiles).filter(user_favorite_profiles.c.user_id == user_id).all()


def delete_favorite_profile(db: Session, user_id: int, profile_id: int):
    """
    Delete a single favorite profile, need pass user id & profile id
    """
    favorite_profile = user_favorite_profiles.delete().where(
        (user_favorite_profiles.c.user_id == user_id) &
        (user_favorite_profiles.c.profile_id == profile_id)
    )
    db.execute(favorite_profile)
    db.commit()
