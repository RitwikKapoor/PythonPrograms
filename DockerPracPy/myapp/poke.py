import requests


while True:
    pokemon_name = input("Enter the name or ID of a Pokemon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"The endpoint for {pokemon_name} does not exist. Please try again.")
        continue

    pokemon_data = response.json()

    print(f"Name: {pokemon_data['name']}")
    print(f"ID: {pokemon_data['id']}")
    print("Types:")
    for pokemon_type in pokemon_data['types']:
        print(f"- {pokemon_type['type']['name']}")

    continue_program = input("Do you want to continue(y/n) ")
    if continue_program == "n":
        break

