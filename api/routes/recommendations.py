from fastapi import APIRouter, HTTPException, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from api.dependencies.jwt import verify_token
from db import crud
from enum import Enum
from db.schemas import Recommendation
from api.services.weather_enums import TemperatureRangeEnum

router = APIRouter()


@router.post("/recommendations/")
async def create_recommendation(
    city: str,
    activities: str,
    outfits: str,
    temperature: TemperatureRangeEnum = TemperatureRangeEnum.temp1,
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token),
):
    print(token)
    email = token["email"]
    add_recommendation = crud.create_recommendation(
        temperature=temperature.value,
        email=email,
        city=city,
        activities=activities,
        outfits=outfits,
        db=db,
    )
    return add_recommendation


@router.get("/recommendations/{city}", response_model=list[Recommendation])
async def read_recommendation(
    city: str, db: Session = Depends(get_db), token: dict = Depends(verify_token)
):
    email = token["email"]
    recommendation = crud.get_recommendation(email=email, city=city, db=db)

    return recommendation


@router.put("/recommendations/{city}")
async def update_recommendation(
    city: str,
    activities: str,
    outfits: str,
    temperature: TemperatureRangeEnum = TemperatureRangeEnum.temp1,
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token),
):
    email = token["email"]
    crud.update_recommendation(
        email=email,
        city=city,
        activities=activities,
        outfits=outfits,
        temperature=temperature,
        db=db,
    )
    return {"message": f"Recommendations for {city} updated successfully"}


@router.delete("/recommendations/{city}")
async def delete_recommendation(
    city: str, db: Session = Depends(get_db), token: dict = Depends(verify_token)
):
    email = token["email"]
    crud.delete_recommendation(email=email, city=city, db=db)
    return {"message": f"Recommendations for {city} deleted successfully"}
