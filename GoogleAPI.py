from pprint import pprint

__author__ = 'arpeetkale1'

# Import the relevant libraries
import requests
import json

# Set the Places API key for your application
AUTH_KEY = 'AIzaSyBaL0Vdxlo0iEIUSdOF6NbWJFt71PS0RaU'

# Define the location coordinates
LOCATION = '37.787930,-122.4074990'

# Define the radius (in meters) for the search
RADIUS = 5000

# Compose a URL to query a predefined location with a radius of 5000 meters
url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s&key=%s') % (LOCATION, AUTH_KEY)
print(url)

# Send the GET request to the Place details service (using url from above)
response = requests.get(url).json()

# Get the response and use the JSON library to decode the JSON
json_data = json.dumps(response)
print(json_data)

#for i in range(len(response)):
#    print(response["results"][i+1]["name"])
#    print(response["results"][i+1]["rating"])