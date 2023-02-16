import requests, os
from dotenv import load_dotenv
import argparse
load_dotenv()

if os.getenv("apikey") == None or "": # Check if the API key is set in the .env file
    apikey = "DEMO_KEY" # If not use the demo key
else:
    apikey = os.getenv("apikey") # else get the API key set by you in the .env file

api = f"https://api.nasa.gov/planetary/earth/imagery?api_key={apikey}&" # Nasa API

def get_earth_photo(lat:float, long:float, date:str):
    url = f"{api}lat={lat}&lon={long}&date={date}" # Date must be in YYYY-MM-DD format
    r = requests.get(url)
    if r.status_code != 200:
        print("Error getting photos (might not exist), exiting...")
        return
    photo = r.json()["url"]
    return photo #The only useable value
"""
Made by galaxine~senapi

GitHub: https://github.com/galaxine-senapi
Discord: gawaxine.exe#1015
Instagram: @aydeng854

API made by NASA
"""