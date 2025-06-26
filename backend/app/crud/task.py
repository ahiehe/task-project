from typing import List

from sqlalchemy.orm import Session

from ..models import User
from ..models.task import Task
from ..schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, new_task: TaskCreate, creator: User) -> Task:
    db_task = Task(title=new_task.header, description=new_task.description, owner_id=creator.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task



def get_all_tasks(db: Session) -> List[Task] | None:
    return db.query(Task).all()

def get_tasks_by_owner_id(db: Session, user_id: int) -> List[Task] | None:
    return db.query(Task).filter(Task.owner_id == user_id).all()

def get_task_by_id(db: Session, user_id: int, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.owner_id == user_id, Task.id == task_id).first()

def update_task(db: Session, task_id: int, user_id: int, task_update: TaskUpdate) -> Task | None:
    task = get_task_by_id(db, task_id, user_id)
    if task:
        task.description = task_update.task_description
        task.completed = task_update.is_completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, user_id: int) -> bool:
    task = get_task_by_id(db, task_id, user_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False

