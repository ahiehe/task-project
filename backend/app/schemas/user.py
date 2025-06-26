from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str

class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True