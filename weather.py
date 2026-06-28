import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch weather data for a given city.
    Returns a dictionary containing weather information.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Raise an exception if the request failed
        response.raise_for_status()

        data = response.json()

        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except requests.exceptions.HTTPError:
        print("❌ Error: City not found or invalid API key.")

    except requests.exceptions.ConnectionError:
        print("❌ Error: No internet connection.")

    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"❌ An unexpected error occurred: {e}")

    return None