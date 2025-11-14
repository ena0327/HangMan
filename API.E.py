
# ENABEANA
# pip install requests 
# Url..
import json
import requests 

base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
  
    url = f"{base_url}pokemon/"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        # print("this is the raw data")
        # print(data)
        print("here are the list of pokemons:")
        for item in data['results']:
            print(item['name'])
    else:
        print(f"Error: {response.status_code}")


get_pokemon_info('')










