# Introduction  -|
# ---------------|
# Python Assingnment for the week 1 while being a part of the Data Science internship team at Zeno 
# Talent under the guidance of Aishwarya. The assignment involves fetching live weather data using
# the OpenWeatherMap API, analyzes the result, and logs key information into a CSV file


import requests
# requests library used to make HTTP requests to APIs
import csv
# to read or write CSV files

def fetch_weather(city: str, api_key: str) -> dict:
    # function takes a city name and API key as input and returns a dictionary
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        # request to the URL
        response.raise_for_status()
        # it raises an error if the HTTP response status_code is not 200
        return response.json()
        # returns the JSON response converting in the form of a dictionary
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return {}
        # to catch any request related errors(invalid city)

def analyze_weather(data: dict) -> str:
    # function takes dictionary as input and returns string
    try:
        temp = data['main']['temp']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        # extracting temperature, wind speed, humidity from data

        if temp <= 10:
            summary = "Cold (≤10°C)"
        elif temp <= 24:
            summary = "Mild (11-24°C)"
        else:
            summary = "Hot (≥25°C)"
        # categorizing temperature into cold, mild, or hot based on temperature

        if wind > 10:
            summary += " | High wind alert!"
        if humidity > 80:
            summary += " | Humid conditions!"
        # creating wind, humidity alerts

        return summary
    except KeyError:
        # if any key like 'main' is missing, it returns following message
        return "Incomplete data."

def log_weather(city: str, filename: str, api_key: str):
    # function to write into a file
    data = fetch_weather(city, api_key)
    # function call
    if data:
        # if data is not empty
        summary = analyze_weather(data)
        # function call
        f = open(filename, 'a', newline='', encoding='utf-8')
        writer = csv.writer(f)
        # file in append mode, uses the csv.writer() to write a new row
        writer.writerow([city, data['main']['temp'], data['wind']['speed'], data['main']['humidity'], summary])
        # row containing the city name, temperature, wind speed, humidity, and summary to file
        f.close()
        # closes the file after writing
        print("Weather logged successfully:", summary)

api_key = "api_key"
city = input("Enter city name: ")
log_weather(city, "city_weather.csv", api_key)
# calling function with city name from user and API key


# Conclusion  -|
# -------------|
# In this Week 1 assignment, I worked on provides practical exposure to working with APIs, 

# JSON parsing, CSV handling, and writing modular functions in Python.
