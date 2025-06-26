from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from ..crud.task import get_all_tasks, get_tasks_by_owner_id
from ..crud.user import get_user_by_name, create_user
from ..database import get_db
from ..schemas.task import TaskOut
from ..schemas.user import UserCreate, UserOut
from ..utils.auth import get_current_user, get_password_hash, authenticate_user, create_access_token

user_router = APIRouter(tags=["user"], prefix="/user")


@user_router.post("/register/", response_model=UserOut)
async def register_user(user_credentials: UserCreate,  db: Session = Depends(get_db)):
    user = get_user_by_name(db, user_credentials.name)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user_credentials.password)
    user_credentials.password = hashed_password
    new_user = create_user(db, user_credentials)
    return new_user

@user_router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> str:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = create_access_token({"username": user.username})
    return token
