from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.profile import Profile
from app.database import get_db
from app.controller import profile_crud

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/", response_model=Profile)
def create_profile(name: str, description: str, user_id: int, db: Session = Depends(get_db)):
    """
    Create a profile
    """
    return profile_crud.create_profile(db=db, name=name, description=description, user_id=user_id)


@router.get("/", response_model=list[Profile])
def read_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    get all profiles
    """
    return profile_crud.get_profiles(db=db, skip=skip, limit=limit)


@router.get("/{profile_id}", response_model=Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    get a single profile
    """
    return profile_crud.get_profile(db=db, profile_id=profile_id)


@router.put("/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, name: str, description: str, db: Session = Depends(get_db)):
    """
    Update a single profile
    """
    return profile_crud.update_profile(db=db, profile_id=profile_id, name=name, description=description)


@router.delete("/{profile_id}", response_model=Profile)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    Delete a single profile
    """
    return profile_crud.delete_profile(db=db, profile_id=profile_id)
