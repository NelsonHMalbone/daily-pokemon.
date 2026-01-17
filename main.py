import requests
import random


url = 'https://pokeapi.co/api/v2/pokemon?limit=100000'
request = requests.get(url)
content = request.json()
print(content['results']['name'])


#pokemon_data = content["results"]

#random_pokemon = random.choice(pokemon_data)
