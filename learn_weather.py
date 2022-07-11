import requests

API_key = "1b3a4a2010cfd8eb135628c812b425e3"
city = input("City: ")

response= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}")

obj = response.json()

temp = round(obj["main"]["temp"] - 273.15)
temp_max = round(obj["main"]["temp_max"] - 273.15)
temp_min = round(obj["main"]["temp_min"] - 273.15)
country = obj["sys"]["country"]
print(f"This is the weather in {obj['name']}, {country}")
print(f"Now: {temp}°C , Todays max: {temp_max}°C, Todays low: {temp_min}°C ")