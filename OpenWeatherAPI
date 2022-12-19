from dataclasses import dataclass
import requests
import json

@dataclass
class Weather:
    longitude: float
    latitude: float
    temperature: float
    feels_like: float
    pressure: int
    humidity: int
    clouds: int

def get_weather_for_point(longitude: float, latitude: float) -> Weather:
    
    lat = latitude
    lon = longitude
    apikey = input()
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=metric"  % (latitude, longitude, apikey)

    response = requests.get(url)
    data = json.loads(response.text)

    main = data["main"]
    clouds = data["clouds"]

    Weather.longitude = longitude
    Weather.latitude = latitude
    Weather.temperature = main["temp"]
    Weather.feels_like = main["feels_like"]
    Weather.pressure = main["pressure"]
    Weather.humidity = main["humidity"]
    Weather.clouds = clouds["all"]

    #print(Weather.clouds, " ", Weather.temperature)

    return Weather
