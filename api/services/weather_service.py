import requests
from core.config import settings
from transformers import pipeline

# Loading the pre-trained GPT-2 model for text generation
generator = pipeline("text-generation", model="gpt2")


def fetch_weather(city: str):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": settings.WEATHER_API_KEY, "q": city}
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None