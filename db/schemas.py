from pydantic import BaseModel, EmailStr


class Recommendation(BaseModel):
    city: str
    activity: str
    outfit: str
    temperature: str


class User(BaseModel):
    email: EmailStr
    password: str


class UserCreate(User):
    name: str
