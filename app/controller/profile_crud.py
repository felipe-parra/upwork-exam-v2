from sqlalchemy.orm import Session
from app.models.profile import Profile


def create_profile(db: Session, name: str, description: str, user_id: int):
    """
    Create a single profile, with name, description & user who belongs
    """
    profile = Profile(name=name, description=description, user_id=user_id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def get_profiles(db: Session, skip: int = 0, limit: int = 10):
    """
    Get all profiles
    """
    return db.query(Profile).offset(skip).limit(limit).all()


def get_profile(db: Session, profile_id: int):
    """
    Get a single profile by id
    """
    return db.query(Profile).filter(Profile.id == profile_id).first()


def update_profile(db: Session, profile_id: int, name: str, description: str):
    """
    Update a single profile by profile id, and can update just name & description
    """
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if profile:
        profile.name = name
        profile.description = description
        db.commit()
        db.refresh(profile)
        return profile


def delete_profile(db: Session, profile_id: int):
    """
    Delete a single profile by id
    """
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if profile:
        db.delete(profile)
        db.commit()
        return profile
