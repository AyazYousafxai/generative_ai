from sqlalchemy.orm import Session
from fastapi import HTTPException
from db import models, schemas
from sqlalchemy import and_


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email: str, hash_password: str, name: str):
    db_user = models.User(email=email, password=hash_password, name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_recommendation(
    email: str,
    city: str,
    activities: str,
    outfits: str,
    temperature: str,
    db: Session,
):
    existing_recommendation = (
        db.query(models.Recommendation)
        .filter(
            and_(
                models.Recommendation.user_id == email,
                models.Recommendation.city == city,
            )
        )
        .first()
    )
    if existing_recommendation:
        raise HTTPException(
            status_code=400,
            detail="Recommendation already exists for this user and city",
        )
    db_recommendation = models.Recommendation(
        user_id=email,
        city=city,
        activity=activities,
        outfit=outfits,
        temperature=temperature,
    )
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation


def get_recommendation(email: str, city: str, db: Session):
    recommendation = (
        db.query(models.Recommendation)
        .filter(
            and_(
                models.Recommendation.city == city,
                models.Recommendation.user_id == email,
            )
        )
        .all()
    )
    print(recommendation)
    if not recommendation:
        raise HTTPException(
            status_code=404, detail=f"Recommendation for {city} not found"
        )
    return recommendation


def update_recommendation(
    email: str,
    city: str,
    activities: str,
    outfits: str,
    temperature: str,
    db: Session,
):
    recommendation = (
        db.query(models.Recommendation)
        .filter(
            and_(
                models.Recommendation.user_id == email,
                models.Recommendation.city == city,
            )
        )
        .first()
    )
    print(city, email, recommendation)
    if not recommendation:
        raise HTTPException(
            status_code=404,
            detail=f"Recommendation for {city} not found",
        )
    recommendation.activity = activities
    recommendation.outfit = outfits
    recommendation.temperature = temperature
    db.commit()


def delete_recommendation(email: str, city: str, db: Session):
    recommendation_to_delete = (
        db.query(models.Recommendation)
        .filter(
            and_(
                models.Recommendation.user_id == email,
                models.Recommendation.city == city,
            )
        )
        .first()
    )

    if recommendation_to_delete:
        db.delete(recommendation_to_delete)
        db.commit()
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Recommendation for {city} not found",
        )


def fetch_recommendation(
    email: str, city: str, temperature: str, summary: str, db: Session
):
    recommendation = (
        db.query(models.Recommendation)
        .filter(
            and_(
                models.Recommendation.city == city,
                models.Recommendation.user_id == email,
                models.Recommendation.temperature == temperature,
            )
        )
        .first()
    )
    print(recommendation)
    if not recommendation:
        raise HTTPException(
            status_code=404,
            detail=f"Recommendation not found Please add recommendation and check the summary {summary}",
        )
    return recommendation
