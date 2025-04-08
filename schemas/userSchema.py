from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    phone:str


class UserOut(BaseModel):
    id :int
    username:str
    email:str
    phone:str


    class Config:
        orm_mode = True

class userLogin(BaseModel):
    username:str
    password:str