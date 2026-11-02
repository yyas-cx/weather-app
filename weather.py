import requests

def get_weather(city):
    api_key = "YOUR_API_KEY_HERE"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": round(data["main"]["temp"]),
        "description": data["weather"][0]["description"].title(),
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather

def display_weather(weather):
    print("\n" + "-" * 35)
    print(f"📍 {weather['city']}, {weather['country']}")
    print(f"🌡️ Temperature: {weather['temperature']}°C")
    print(f"☁️ Weather: {weather['description']}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"💨 Wind Speed: {weather['wind_speed']} m/s")
    print("-" * 35 + "\n")

# Main program
print("🌤️  Python Weather App  🌤️")
city = input("Enter city name: ")

weather = get_weather(city)

if weather:
    display_weather(weather)
else:
    print(f"\n❌ Sorry, couldn't find weather for '{city}'. Try again!\n")
