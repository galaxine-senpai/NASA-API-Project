import sys, os

from apis import apodapi as apod # Import the apodapi.py file
from apis import imageandvideoapi as imageandvideo # Import the imageandvideoapi.py file
from apis import marsroverapi as marsrover # Import the marsroverapi.py file


if sys.argv[1].lower() == "apod": # Check if the first argument is apod
    if sys.argv[2].lower() == "today": # Check if the second argument is today
        print(apod.get_todays_photo()) # Print the photo
    elif sys.argv[2].lower() == "date": # Check if the second argument is date
        print(apod.get_specific_apod(sys.argv[3], sys.argv[4], sys.argv[5])) # Print the photo
    else:
        print("Error, please use 'today' or 'date' as the first argument")
elif sys.argv[1].lower() == "marsrover": # Check if the first argument is imageandvideo
    if sys.argv[2].lower() == "roverphoto": # Check if the second argument is roverphoto
        print(marsrover.get_photos(sys.argv[3], sys.argv[4], sys.argv[5]))
    elif sys.argv[2].lower() == "roverstatus": # Check if the second argument is roverstatus
        print(marsrover.get_status(sys.argv[3]))
else:
    print("Error, valid arguments are 'apod', 'marsrover'")
