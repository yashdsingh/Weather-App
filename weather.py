import requests

# API key from OpenWeatherMap
API_KEY = "b12bbcd871a6ed03831e9eaa04b37e41"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
else:
    print("City not found. Please check the name.")
