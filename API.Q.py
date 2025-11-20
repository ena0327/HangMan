import random

pokemon_list = []

import requests

url = "https://cat-breeds.p.rapidapi.com/cat_breeds"

headers = {"x-rapidapi-host": "cat-breeds.p.rapidapi.com"}

response = requests.get(url, headers=headers)

print(response.json())
