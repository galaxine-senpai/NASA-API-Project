import requests
import os
from dotenv import load_dotenv
import sys
load_dotenv()
api = "https://api.nasa.gov/planetary/apod"  # Nasa API

if os.getenv("apikey") == None or "":  # Check if the API key is set in the .env file
    apikey = "DEMO_KEY"  # If not use the demo key
else:
    # else get the API key set by you in the .env file
    apikey = os.getenv("apikey")


class apod:
    """The APOD API"""


def get_todays_photo():
    """Get the APOD"""
    r = requests.get(f"{api}?api_key={apikey}")
    if r.status_code != 200:
        print("Error getting photos, exiting...")
        return
    else:
        Copyright = r.json()["copyright"]
        Title = r.json()["title"]
        Date = r.json()["date"]
        Photo = r.json()["hdurl"]
    # TODO: Figure out why python complains
    return f"Copyright/Author: {Copyright}\nTitle: {Title}\nDate Taken:{Date}\nPhoto URL: {Photo}"


# Month can be two or one didget (eg: 1 or 01, YEAR HAS TO BE 4)
def get_specific_apod(month, day, year):
    """Get the APOD (date example: 4,26,2007"""
    month = str(sys.argv[3])
    day = str(sys.argv[4])
    year = str(sys.argv[5])
    r = requests.get(f"{api}?api_key={apikey}&date={year}-{month}-{day}")
    # if year > 1995 and day > 16 and month > 6: # Need to figure out what is causing issues with this when getting vars
    # print("Error, date must be after June 16, 1995")
    if r.status_code != 200:
        print("Error getting photos, exiting...")
        return
    else:
        # Copyright = r.json()["copyright"] # Removed due to me being lazy and unable to figure out how to check if nothing is there
        Title = r.json()["title"]
        Date = r.json()["date"]
        Photo = r.json()["hdurl"]

    return f"Copyright/Author: N/A\nTitle: {Title}\nDate Taken:{Date}\nPhoto URL: {Photo}"


# print(get_todays_photo()) # Tested: Good, no issues
# print(get_specific_apod(11, 7, 1987)) # Tested: Good, no issues
if sys.argv[2] == "today":
    print(get_todays_photo())
elif sys.argv[3] == "date":
    # print(sys.argv)
    # if sys.argv[2] or sys.argv[3] or sys.argv[4] == None: # For some reason it doesn't detect vars right
    # print("Syntax error: Syntax '<month> <day> <year>'")
    # if sys.argv[2] < 6 and sys.argv[3] < 16 and sys.argv[4] < 1995: # Ref line 31
    # print("Error, date must be after June 16, 1995")
    # else:
    print(get_specific_apod(sys.argv[3], sys.argv[4], sys.argv[5]))
else:
    print("Error, please use 'today' or 'date' as the first argument")

"""
Made by galaxine~senapi

GitHub: https://github.com/galaxine-senapi
Discord: gawaxine.exe#1015
Instagram: @aydeng854

API made by NASA
"""
