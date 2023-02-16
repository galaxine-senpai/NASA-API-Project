import requests, os
from dotenv import load_dotenv
import argparse
load_dotenv()
api = "https://api.nasa.gov/planetary/apod" # Nasa API

if os.getenv("apikey") == None or "": # Check if the API key is set in the .env file
    apikey = "DEMO_KEY" # If not use the demo key
else:
    apikey = os.getenv("apikey") # else get the API key set by you in the .env file


def get_todays_photo():
    """Get the APOD"""
    r = requests.get(f"{api}?api_key={apikey}")
    Copyright = r.json()["copyright"]
    Title = r.json()["title"]
    Date = r.json()["date"]
    Photo = r.json()["hdurl"]
    if r.status_code != 200:
        print("Error getting photos, exiting...")
        return
    else:
        return f"Copyright/Author: {Copyright}\nTitle: {Title}\nDate Taken:{Date}\nPhoto URL: {Photo}" #TODO: Figure out why python complains

def get_specific_apod(month: int, day: int, year: int):
    """Get the APOD"""
    r = requests.get(f"{api}?api_key={apikey}&date={year}-{month}-{day}")
    #Copyright = r.json()["copyright"] # Removed due to me being lazy and unable to figure out how to check if nothing is there
    Title = r.json()["title"]
    Date = r.json()["date"]
    Photo = r.json()["hdurl"]
    if r.status_code != 200:
        print("Error getting photos, exiting...")
        return
    else:
        return f"Copyright/Author: N/A\nTitle: {Title}\nDate Taken:{Date}\nPhoto URL: {Photo}"

#print(get_todays_photo()) # Tested: Good, no issues
#print(get_specific_apod(4, 26, 2007)) # Tested: Good, no issues

"""
Made by galaxine~senapi

GitHub: https://github.com/galaxine-senapi
Discord: gawaxine.exe#1015
Instagram: @aydeng854

API made by NASA
"""