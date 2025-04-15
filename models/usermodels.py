from sqlalchemy import Enum,Column, Integer, String
from database import Base
import enum
class UserRole(str, enum.Enum):
    admin = "admin"
    student = "student"
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    email=Column(String,unique=True,index=True)
    phone=Column(String,unique=True,index=True)
    password=Column(String)
    role=Column(Enum(UserRole),default=UserRole.student,nullable=False)