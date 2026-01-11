import requests
import json

id_pokemon = int(input("Pokemon ID: "))

api = f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}'
request = requests.get(api)
content = request.json()

print(json.dumps(content["forms"], indent=4))