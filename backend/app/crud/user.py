from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate, UserOut


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(username=user.name, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_name(db: Session, name: str) -> User | None:
    return db.query(User).filter(User.username == name).first()

