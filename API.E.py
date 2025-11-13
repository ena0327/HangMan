
# ENABEANA
# pip install requests 
# Url..

import requests 

base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(pokemon):
  
    url = f"{base_url}/pokemon/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.pokemon)
    else:
        print(f"Error: {response.status_code}")


get_pokemon_info(pokemon)











