# Welcome to my project

## What is my goal?

My goal is to use almost every NASA API listed on the <a href="https://api.nasa.gov" target=_blank>NASA</a> website, this will hopefully make me more proficiant when it comes to coding in python.

## What do I do if I find an issue whithin the code?

Just submit a pull request and I will review it ASAP or just submit an issue if you don't know how to fix it and I will try my very hardest to get that done!

# Introduction

## How to set up the project

First rename example.env to .env it has all the values you need to set up what you need to run the project (even if you dont fill it out it will still run it just helps NASA know who and how you are using their API's)

Next run the following command in your terminal

```bash
pip install -r requirements.txt
```

That will install all the things you need to run the project

Now since that was all that needed to be done you can now just run the file of your choosing!

An example is:
```bash
python3 marsroverapi.py
```

### Bugs

~~As of current (2/15/23) the File outputs everything it gets from the API flooding the terminal, I will be fixing this ASAP~~ ***FIXED***

As of 2/27/23 APOD file doesn't accept the vars and do the date check correctly, and vars are not detected correctly by the empty check // Will fix when able

As of 2/27/23 Image and video API is not printing anything to the console // Will fix when able

As of 3/8/23 Just doing "python3 main.py" will not work, unknown why (I am stupid) // Will fix when I figure it out

### Notes

I will be doing the whole args thing with the Mars Rover API File soon