"""Using Requests + JSON."""

# requests is a Python package that you must install...
import requests

# A JSON Placeholder that returns fake data
POSTS_URL = "https://wttr.in/Boston?format=j1"

print(f"Getting live data from {POSTS_URL}.")
r = requests.get(POSTS_URL, timeout=60)
posts = r.json()


#print(f"{posts['weather']}")

#print(f"{posts['weather']}")

vweather = posts['weather']

print ( vweather[0],['astronomy'],'avgtempC')

     #  .'astronomy'.'avgtempC' )




