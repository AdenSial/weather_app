from weather import get_weather


def main():
    print("=" * 40)
    print("      🌤️ Weather App")
    print("=" * 40)

    city = input("Enter city name: ")

    weather = get_weather(city)

    if weather:
        print("\nCurrent Weather")
        print("-" * 40)
        print(f"📍 City        : {weather['city']}, {weather['country']}")
        print(f"🌡 Temperature : {weather['temperature']}°C")
        print(f"🤗 Feels Like  : {weather['feels_like']}°C")
        print(f"💧 Humidity    : {weather['humidity']}%")
        print(f"🌬 Wind Speed  : {weather['wind_speed']} m/s")
        print(f"☁ Condition    : {weather['description']}")


if __name__ == "__main__":
    main()