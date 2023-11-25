import email
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from db import crud, models
from db.schemas import User, UserCreate
from api.dependencies.jwt import create_access_token

router = APIRouter()


@router.post("/signup",status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db=crud.create_user(db,email=user.email,hash_password=user.password,name=user.name)
    return {"message": "User registered successfully"}

@router.post("/login",status_code=status.HTTP_200_OK)
def login(user: User, db: Session = Depends(get_db)):
    print(user)
    email = user.email
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    access_token=create_access_token(data={'email':email})
    return {"access_token": access_token,"token_type": "bearer"}