from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..crud.task import get_all_tasks, get_tasks_by_owner_id, create_task
from ..database import get_db
from ..models import User
from ..schemas.task import TaskOut, TaskCreate
from ..utils.auth import get_current_user

router = APIRouter(tags=["tasks"], prefix="/tasks")


@router.get("/all/", response_model=List[TaskOut])
async def get_tasks(db: Session = Depends(get_db)) -> List[TaskOut] | None:
    return get_all_tasks(db)

@router.get("/mytasks/", response_model=List[TaskOut])
async def get_my_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> List[TaskOut] | None:
    return get_tasks_by_owner_id(db, current_user.id)

@router.get("/newtask/", response_model=TaskOut)
async def create_new_task(new_task: TaskCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> TaskOut:
    return create_task(db, new_task, current_user)

