from typing import List
from app.database import get_db
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.controller import user_crud
from app.schemas.user import User, UserCreate
from app.schemas.profile import Profile

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", response_model=List[User])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def get_single_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print("User->", user)
    db_user = user_crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already taken")
    return user_crud.create_user(db, user)


@router.put("/{user_id}/", response_model=User)
def update_user_info(
    user_id: int,
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    updated_user = user_crud.update_user(
        db, user_id, name, email)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}/", response_model=User)
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_crud.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user


@router.post("/{user_id}/favorite-profiles/{profile_id}", tags=["Favorites"])
def add_favorite_profile(user_id: int, profile_id: int, db: Session = Depends(get_db)):
    user_crud.create_favorite_profile(
        db, user_id=user_id, profile_id=profile_id)
    return {"message": "Favorite profile added successfully"}


@router.get("/{user_id}/favorite-profiles/", response_model=List[Profile], tags=["Favorites"])
def get_user_favorite_profiles(user_id: int, db: Session = Depends(get_db)):
    favorite_profiles = user_crud.get_user_favorite_profiles(
        db, user_id=user_id)
    return favorite_profiles


@router.delete("/{user_id}/favorite-profiles/{profile_id}", tags=["Favorites"])
def delete_favorite_profile(user_id: int, profile_id: int, db: Session = Depends(get_db)):
    user_crud.delete_favorite_profile(
        db, user_id=user_id, profile_id=profile_id)
    return {"message": "Favorite profile deleted successfully"}
