import requests
import json

API_key = "1b3a4a2010cfd8eb135628c812b425e3"
city = input("City: ")
#response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=&appid={API_key}")

response= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}")

obj = response.json()
print(obj)