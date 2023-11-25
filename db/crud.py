from sqlalchemy.orm import Session
from db import models, schemas
from sqlalchemy import and_



def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, email: str, hash_password:str,name:str):
    db_user = models.User(email=email, password=hash_password,name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user