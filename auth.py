from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import JWTError,jwt
from helpers.logger import logger
from dotenv import load_dotenv
import os
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto" 
)

def hash_password(password:str):
    logger.info("Hashing password")
    return pwd_context.hash(password)


def verify_password(user_password:str,hash_password:str):
    logger.info("verifying password")
    return pwd_context.verify(user_password,hash_password)

def create_access_token(data:dict,expires_delta:timedelta=None):
    logger.info("Creatiung access Token")
    to_encode=data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))