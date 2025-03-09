# https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png
# https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/132.png
import requests
import json

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    data = response.json()
    
    return {
        "id": data["id"],
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "height": data["height"],
        "weight": data["weight"],
        "sprite": data["sprites"]["other"]["official-artwork"]["front_default"]
    }

pokemon_list = []

# Obtener datos del Pokémon 1 al 200
for pokemon_id in range(1, 201):
    try:
        pokemon = get_pokemon_data(pokemon_id)
        pokemon_list.append(pokemon)
        print(f"Obtenido Pokémon: {pokemon['name'].capitalize()} (ID: {pokemon_id})")
    except Exception as e:
        print(f"Error obteniendo Pokémon {pokemon_id}: {str(e)}")

# Guardar en archivo JSON
with open("pokemon_data.json", "w") as f:
    json.dump(pokemon_list, f, indent=2)

print("¡Datos guardados en pokemon_data.json!")