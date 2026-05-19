import requests

def get_weather(city):
    api_key = "your_api_key"  # Replace with a valid OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = data['weather'][0]['description']
        return (temperature, pressure, humidity, weather_description)
    else:
        print("City not found.")
        return None

def main():
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    if weather_info:
        temperature, pressure, humidity, description = weather_info
        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Weather Description: {description}")
    else:
        print("Failed to fetch weather information.")

if __name__ == "__main__":
    main()
