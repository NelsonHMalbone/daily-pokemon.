import requests
import json
import random


url = 'https://pokeapi.co/api/v2/pokemon?limit=100000'
request = requests.get(url)
request.raise_for_status()
content = request.json()

pokemon_data = content["results"]

random_pokemon = random.choice(pokemon_data)

print("Random Pokemon")
print("name: ", random_pokemon["name"])
print("url: ", random_pokemon["url"])