from pydantic import BaseModel, EmailStr
from typing import Literal,Optional


class UserBase(BaseModel):
    username:str
    email:EmailStr
    phone:Optional[str]=None
class UserCreate(UserBase):
    password:str
    role: Literal['admin', 'student'] = 'student'
    



class UserOut(UserBase):
    id :int
    username:str
    email:str
    phone:str
    role:str


    class Config:
        orm_mode = True

class userLogin(BaseModel):
    username:str
    password:str