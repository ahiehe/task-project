from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool

class TaskOut(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    owner_id: int

class TaskUpdate(BaseModel):
    is_completed: Optional[bool] = None
    task_description: Optional[str] = None