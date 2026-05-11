# Name: Kris Kleiner
# Date: May 10, 2026
# Assignment: Module 9.2 - APIs
# Purpose: Practice connecting to APIs, printing raw JSON responses, and formatting JSON output.

import requests
import json


def jprint(obj):
    """Format and print JSON data."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print("Testing connection to Google")
response = requests.get("http://www.google.com")
print("Google status code:", response.status_code)

print("\nTesting connection to Open Notify Astronauts API")
astro_response = requests.get("http://api.open-notify.org/astros.json")
print("Astronaut API status code:", astro_response.status_code)

print("\nRaw astronaut API response:")
print(astro_response.json())

print("\nFormatted astronaut API response:")
jprint(astro_response.json())


print("\nTesting connection to Dog CEO API")
dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
print("Dog API status code:", dog_response.status_code)

print("\nRaw Dog API response:")
print(dog_response.json())

print("\nFormatted Dog API response:")
jprint(dog_response.json())