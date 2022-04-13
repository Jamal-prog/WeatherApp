#!/usr/bin/python3
"""Getting weather for certain city | Jamal Hawkins"""
# imports 
import requests 
import math
import keys 

# Grabs API key from keys.py
APIKEY = keys.APIKEY

# method that takes in weather in Kelvin and city name, convert temp to F and printout description of the weather for desired city 
def printout(weather,name):
    # converts Kelvin to Farenheit and rounds up
    temp = math.ceil(int(weather['main']['temp'] - 273.13) * 1.8 + 32)
    # conditions 
    if temp < 70 and temp > 55:
        print("Not too shabby!!")
    elif temp < 54:
        print("You may need a jacket")
    else:
        print("Nice weather!!!")
    # creates a variable to hold print statement 
    description = f"{name} has a temperature of {temp} degrees - {weather['weather'][0]['main']},{weather['weather'][0]['description']}"

    print(description)

# method that searches weather by zipcode
def zipcode():
    try:
        # Takes in input from user and stores it in a variable
        ZIPCODE = input("Please enter the zipcode for weather at that location!\n>")

        # Zipcode URL to get Lat and Lon
        URL = f"http://api.openweathermap.org/geo/1.0/zip?zip={ZIPCODE}&appid={APIKEY}"

        # using requests calling get to zipcode URL then converts to json
        exact = requests.get(URL).json()

        # create variables for the specific location from the get request
        lat = exact['lat']
        lon = exact['lon']
        name = exact['name']

        # Get request to grab weather api then converts to json
        BASEURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
        weather = requests.get(BASEURL).json()

        # pass weather and name to printout() as arguments
        printout(weather,name)
    except:
        # Catches Error
        print("Please enter a valid zipcode")

# method that searches weather by city, state, and country   
def default():
    try:
        # takes in input from user for city, state, country
        city = input("Please enter a city\n>")
        state = input("Please enter a state\n>")
        country = input("Please enter a country\n>")

        # get requests to grab the lat and lon then convert to json
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={5}&appid={APIKEY}"
        exact = requests.get(url).json()
        lat = exact[0]['lat']
        lon = exact[0]['lon']
        
        # get requests to grab the weather api then convert to json
        BASEURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
        weather = requests.get(BASEURL).json()

        # pass weather and city name to printout()
        printout(weather,city)
    except:
        # Catches Error
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