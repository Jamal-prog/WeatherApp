#!/usr/bin/python3
"""Getting weather for certain city | Jamal Hawkins"""
import requests 
import pprint
import math
import keys 

APIKEY = keys.APIKEY

def printout(weather,name):
    temp = math.ceil(int(weather['main']['temp'] - 273.13) * 1.8 + 32)
    if temp < 70:
        print("Not too shabby!!")
    else:
        print("Nice weather!!!")
    description = f"{name} has a temperature of {temp} degrees - {weather['weather'][0]['main']},{weather['weather'][0]['description']}"
    print(description)

def zipcode():
    try:
        ZIPCODE = input("Please enter the zipcode for weather at that location!\n>")
        URL = f"http://api.openweathermap.org/geo/1.0/zip?zip={ZIPCODE}&appid={APIKEY}"
        exact = requests.get(URL).json()
        lat = exact['lat']
        lon = exact['lon']
        name = exact['name']
        BASEURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
        weather = requests.get(BASEURL).json()
        printout(weather,name)
    except:
        print("Please enter a valid zipcode")
     
def default():
    try:
        city = input("Please enter a city\n>")
        state = input("Please enter a state\n>")
        country = input("Please enter a country\n>")
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={5}&appid={APIKEY}"
        exact = requests.get(url).json()
        lat = exact[0]['lat']
        lon = exact[0]['lon']
        BASEURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
        wea = requests.get(BASEURL).json()
        printout(wea,city)
    except:
        print("Error in city, state, or country")

print("Welcome to Wonders Weather Teller")
print("=============================")
choice = input("Press '0' to look up by zipcode or press '1' to look up by city, state, and country\n>")
if choice == "0":
    zipcode()
elif choice == "1":
    default()
else:
    print("Please press 0 or 1!!!")