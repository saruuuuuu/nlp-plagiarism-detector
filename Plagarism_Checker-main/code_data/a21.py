def get_weather(city):
    # Dummy data for weather
    weather_data = {
        "New York": "Sunny, 25°C",
        "Los Angeles": "Cloudy, 22°C",
        "Chicago": "Rainy, 18°C",
        "Houston": "Sunny, 30°C",
    }
    return weather_data.get(city, "Weather data not available.")

def main():
    print("Welcome to the Weather App!")
    
    while True:
        city = input("Enter a city name to get the weather (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather = get_weather(city)
        print(f"The weather in {city} is: {weather}")

if __name__ == "__main__":
    main()
