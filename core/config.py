from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Settings(BaseSettings):
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOSTNAME: str = os.getenv("POSTGRES_HOSTNAME")
    WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY")

    class Config:
        pass


settings = Settings()
