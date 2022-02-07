import requests
from pprint import pprint

API_Key = '3573b049dbbf2710e6180233d48b6598'


city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
