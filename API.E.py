
# ENABEANA
# pip install requests 
# Url..
import json
import random
import requests 

pokeylist = []
base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    global pokeylist
    url = f"{base_url}pokemon/"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        # print("this is the raw data")
        # print(data)
        print("here are the list of pokemons:")
        pokeylist = data['results']
        for item in data['results']:
            print(item['name'])
    else:
        print(f"Error: {response.status_code}")     
        #hdgfhxskghdgfskgtksk QUAFIA HATES ME ;[

        get_pokemon_info(" ")
        random = __import__('random')
onePokemon = random.choice(pokeylist)
choosenName = onePokemon["name"]

print(f"The randomly chosen element is: {choosenName}")
