import requests, os
from dotenv import load_dotenv
load_dotenv()
api = "https://api.nasa.gov/mars-photos/api/v1" # Nasa API
if os.getenv["apikey"] == None or "": # Check if the API key is set in the .env file
    apikey = "DEMO_KEY" # If not use the demo key
else:
    apikey = os.getenv["apikey"] # else get the API key set by you in the .env file
rovers = ["curiosity", "opportunity", "spirit"] # Rovers available
cameras = ["NAVCAM", "FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM", "PANCAM", "MINITES"] # Cameras available

def get_photos(rover, sol, camera):
    """Get photos from the Nasa Mars Rover API"""
    # A ton of innecessary pre checks to make sure the user has provided the correct information
    if rover == "":
        print("No rover provided, exiting... please provide a rover")
        return
    elif rover.lower() not in rovers:
        print("Rover not recognised, exiting... please provide a valid rover")
        print(f"valid rovers are {rovers}")
        return
    if sol == "":
        print("No sol provided, exiting... please provide a sol")
        return
    elif sol.isdigit() == False:
        print("Sol is not a number, exiting... please provide a number")
        return
    if camera == "":
        camera = "NAVCAM"
    elif camera.upper() not in cameras:
        print("Camera not recognised, exiting... please provide a valid camera")
        print(f"valid cameras are {cameras}")
        return

    url = f"{api}/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={apikey}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error getting photos, exiting...") # TODO: Get the first photo for that sol (day) instead of every single photo
        return
    return response.json()

def get_status(rover):
    """Get status of a specific rover"""
    if rover == "":
        print("No rover provided, exiting... please provide a rover")
        return
    elif rover.lower() not in rovers:
        print("Rover not recognised, exiting... please provide a valid rover")
        print(f"valid rovers are {rovers}")
        return

    url = f"{api}/manifests/{rover}?api_key={apikey}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error getting rover status, exiting...")
        return
    return response.json() # TODO: Get specific values from the response

#print(get_photos("curiosity", "100", "NAVCAM")) # Get photos from curiosity on sol 100 (testing)
#print(get_status("curiosity")) # Get status of curiosity (testing)

"""
Made by galaxine~senapi

GitHub: https://github.com/galaxine-senapi
Discord: gawaxine.exe#1015
InstagramL @aydeng854
"""
