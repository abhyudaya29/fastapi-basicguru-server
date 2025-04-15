from fastapi import APIRouter,Depends,HTTPException,FastAPI,status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models import usermodels
from schemas import userSchema
from database import SessionLocal,get_db
from auth import hash_password,create_access_token,verify_password
from helpers.logger import logger
from models.usermodels import User
from fastapi.encoders import jsonable_encoder
router=APIRouter()


@router.post("/signup",response_model=userSchema.UserOut)
def signup(user:userSchema.UserCreate,db:Session=Depends(get_db)):
    print(user,"user response")
    # if user exist
    exist_user=db.query(User).filter(User.username==user.username).first()
    if exist_user:
        raise HTTPException(status_code=400,detail="User with this username already exist")
    # if not exist then hash he psw
    hash_psw=hash_password(user.password)
    print(hash_psw,"Hashed psw")
    db_user=usermodels.User(username=user.username,email=user.email,password=hash_psw,phone=user.phone,role=user.role)
    print(db_user,"db user")
    db.add(db_user)
    db.commit()
    
    db.refresh(db_user)
    return JSONResponse(status_code=status.HTTP_200_OK, content={
            "success": True,
            "message": "User Registerd successfully",
            "data": jsonable_encoder(db_user)  
        })


@router.post("/login",response_model=userSchema.UserOut)
def login(user:userSchema.userLogin,db:Session=Depends(get_db)):
    logger.info("User initiated login",user)
    check_user_exist=db.query(User).filter(User.username==user.username).first()
    print(check_user_exist,"usere data")
    if not check_user_exist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not exist"
        )
    verify_user_password=verify_password(user.password,check_user_exist.password)
    if not verify_user_password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )
    # all matches,create token
    token=create_access_token(data={"sub":check_user_exist.username})
    user_data_for_response={
        "id": check_user_exist.id,
            "username": check_user_exist.username,
            "email": check_user_exist.email,
            "phone": check_user_exist.phone,
            "role":check_user_exist.role
    }
    print(user_data_for_response,"user_data_for_response")
    return JSONResponse(status_code=status.HTTP_200_OK, content={
            "success": True,
            "message": "User logined successfully",
            "token":token,
            "data": jsonable_encoder(user_data_for_response)  
        })
