import PyPDF2
import requests
import webbrowser
import json
import pprint

cities = ['karachi', 'canada', 'hiroshima']

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8a6a6ab8d86b9c283d304da65a11dc7'

weather_data = []

for city in cities:
    r = requests.get(url.format(city)).json()
    city_weather = {
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }
    weather_data.append(city_weather)
    
print(weather_data)
