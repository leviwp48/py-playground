import requests as r
from pokemon import Pokemon
from team import Team
import json
import random


def create_pokemon():
    poke_id = random.randint(1, 100)
    raw_res = r.get("https://pokeapi.co/api/v2/pokemon/" + str(poke_id))
    json_res = raw_res.json()
    name, abilities, id = json_res["name"], json_res["abilities"], json_res["id"]
    pokemon = Pokemon(name, abilities, id)
    print('id: ', pokemon.get_id())
    print('name: ', pokemon.get_name())
    spot = 1
    for ability in pokemon.get_abilities():
        print(f"ability {spot}: {ability['ability']['name']}")
        spot += 1
    return pokemon


def create_team():
    new_team = Team("best team")
    for i in range(0, 6):
        new_pokemon = create_pokemon()
        new_team.add_pokemon(new_pokemon)
    print(json.dumps(new_team.get_team()))


create_team()