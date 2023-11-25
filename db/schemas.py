from pydantic import BaseModel,EmailStr

class Recommendation(BaseModel):
    id: int
    city: str
    activity: str
    outfit: str


class User(BaseModel):
    email: EmailStr
    password: str


class UserCreate(User):
    name: str

    