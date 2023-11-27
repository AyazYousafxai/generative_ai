import requests
from core.config import settings
from transformers import pipeline

# summarizer = pipeline("text-generation", model="gpt2")
# summarizer = pipeline(
#     "summarization", model="t5-base", tokenizer="t5-base", framework="pt"
# )
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def fetch_weather(city: str):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": settings.WEATHER_API_KEY, "q": city}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def format_weather_data(weather_info):
    print(weather_info)
    formatted_data = f"Weather in {weather_info['location']['name']}, {weather_info['location']['country']}:\n "
    formatted_data += f"Current Temperature: {weather_info['current']['temp_c']}°C ({weather_info['current']['temp_f']}°F)\n "
    formatted_data += f"Condition: {weather_info['current']['condition']['text']}\n"
    formatted_data += f"Wind Speed: {weather_info['current']['wind_kph']} km/h, Direction: {weather_info['current']['wind_dir']}\n "
    formatted_data += f"Pressure: {weather_info['current']['pressure_mb']} mb\n"
    formatted_data += f"Humidity: {weather_info['current']['humidity']}%\n"
    return formatted_data


def get_summary(weather_data):
    formatted_text = format_weather_data(weather_data)
    summary = summarizer(formatted_text, max_length=150, min_length=30, do_sample=False)
    print(summary)
    return summary[0]["summary_text"]
