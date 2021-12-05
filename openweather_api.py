import requests
from configure import OPEN_WEATHER_KEY


def get_weather(city):
    req = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_KEY}").json()
    weather_desc, grade = req["weather"][0]["description"], req["main"]["temp"] - 273.15
    return weather_desc, format(grade, '.2f')


print(get_weather("Санкт-Петербург"))
