import email
import weakref
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from db import crud, models

from api.services.weather_service import fetch_weather
from api.dependencies.jwt import verify_token
import requests
from core.config import settings
from api.services.weather_service import get_summary
from api.services.weather_enums import TemperatureRangeEnum


router = APIRouter()


@router.get(
    "/{city}",
    status_code=status.HTTP_200_OK,
)
def get_weather_and_recommendations(
    city: str, token: dict = Depends(verify_token), db: Session = Depends(get_db)
):
    email = token["email"]
    fetch_data = fetch_weather(city=city)
    if fetch_data:
        summary = get_summary(fetch_data)
        # weather = fetch_data["current"]["condition"]["text"]
        temp = fetch_data["current"]["temp_c"]
        if temp < 12:
            temperature = TemperatureRangeEnum.temp1
        elif 20 > temp > 12:
            temperature = TemperatureRangeEnum.temp2
        elif 20 < temp < 30:
            temperature = TemperatureRangeEnum.temp3
        elif temp > 30:
            temperature = TemperatureRangeEnum.temp4
        recommendation = crud.fetch_recommendation(
            email=email, city=city, temperature=temperature, db=db
        )
        return {
            "summary": summary,
            "outfits": recommendation.outfit,
            "activity": recommendation.activity,
        }
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Weather data is not found for {city}",
        )
