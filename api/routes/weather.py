import email
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from db import crud, models
from db.schemas import User, UserCreate
from api.services.weather_service import fetch_weather 
from api.dependencies.jwt import verify_token
import requests
from core.config import settings



router = APIRouter()



@router.get("/{city}",status_code=status.HTTP_200_OK,)
def get_weather_and_recommendations(city: str,  token: dict=Depends(verify_token)):
    fetch_data=fetch_weather(city=city)
    return {"data": fetch_data}
