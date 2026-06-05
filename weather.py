# get_weather() goes here
import requests
from utils.logger import log_interaction

def get_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        r = requests.get(url, timeout=10)
        d = r.json()

        if d.get("cod") != 200:
            return f"Error: {d.get('message')}"

        weather = d["weather"][0]["description"].title()
        temp = d["main"]["temp"]
        hum = d["main"]["humidity"]
        wind = d["wind"]["speed"]

        result = f"""
🌍 {city}

🌤️ {weather}
🌡️ Temperature: {temp}°C
💧 Humidity: {hum}%
💨 Wind Speed: {wind} m/s
"""

        log_interaction("weather", city, result)
        return result

    except Exception as e:
        return str(e)
