import requests
import sys

def get_photo(query: str):
    """Get the APOD"""
    query = sys.argv[1]
    r = requests.get(f"https://images-api.nasa.gov/search?q={query}")
    if r.status_code != 200:
        print("Error getting photos, exiting...")
        return
    else:
        print(r.json()["collection"]["items"][0]["links"][0]["href"]) # Doesn't print not sure why, will fix later