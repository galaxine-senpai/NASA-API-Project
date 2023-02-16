import requests, os
from dotenv import load_dotenv
import argparse
load_dotenv()
api = "https://api.nasa.gov/mars-photos/api/v1" # Nasa API

if os.getenv("apikey") == None or "": # Check if the API key is set in the .env file
    apikey = "DEMO_KEY" # If not use the demo key
else:
    apikey = os.getenv("apikey") # else get the API key set by you in the .env file
"""
parser = argparse.ArgumentParser(
    prog="Martian Rover API",
    description="Get stuff on rovers from the Nasa Mars Rover API",
    epilog="Made by galaxine~senapi, API made by NASA",
    add_help=True,
    ) # Create a parser for the command line arguments
"""
# Arrays of rovers and cameras
rovers = ["curiosity", "opportunity", "spirit"] # Rovers available
cameras = ["NAVCAM", "FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM", "PANCAM", "MINITES"] # Cameras available
def get_photos(rover: str, sol: int, camera="NAVCAM"):
    """Get photos from the Nasa Mars Rover API"""
    # A ton of innecessary pre checks to make sure the user has provided the correct information
    if rover == "":
        print("No rover provided, exiting... please provide a rover")
        return
    elif rover.lower() not in rovers:
        print(f"Rover not recognised, exiting... please provide a valid rover, valid rovers are {', '.join(rovers)}")
        return
    if sol == "":
        print("No sol provided, exiting... please provide a sol")
        return
    elif sol.isdigit() == False:
        print("Sol is not a number, exiting... please provide a number")
        return
    elif camera.upper() not in cameras:
        print("Camera not recognised, exiting... please provide a valid camera")
        print(f"valid cameras are {', '.join(cameras)}")
        return

    url = f"{api}/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={apikey}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error getting photos, exiting...")
        return
    photourl = response.json()["photos"][0]["img_src"]
    earthdate = response.json()["photos"][0]["earth_date"]
    id = response.json()["photos"][0]["id"]
    return f"Photo URL: {photourl}\nEarth Date: {earthdate}\nPhoto ID: {id}"

def get_status(rover: str):
    """Get status of a specific rover"""
    if rover == "":
        print("No rover provided, exiting... please provide a rover")
        return
    elif rover.lower() not in rovers:
        print(f"Rover not recognised, exiting... please provide a valid rover, valid rovers are {', '.join(rovers)}")
        return

    url = f"{api}/manifests/{rover}?api_key={apikey}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error getting rover status, exiting...")
        return
    launchdate = response.json()["photo_manifest"]["launch_date"]
    landingdate = response.json()["photo_manifest"]["landing_date"]
    status = response.json()["photo_manifest"]["status"]
    return f"Launched: {launchdate}\nLanded on Mars: {landingdate},\n Is {rover} active?: {status}" 

#print(get_photos("curiosity", "100", "NAVCAM")) # Get photos from curiosity on sol 100 (testing)
#print(get_status("curiosity")) # Get status of curiosity (testing)

"""
Made by galaxine~senapi

GitHub: https://github.com/galaxine-senapi
Discord: gawaxine.exe#1015
InstagramL @aydeng854
"""
