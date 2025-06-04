import requests

Url = 'https://api.pokemonbattle.ru/v2'
Token = 'User_token'
Header = {'Content-Type':'application/json', 'trainer_token':Token}
Body_create = {
    "name": "Generate",
    "photo_id": -1
}
Body_change_name = {
    "pokemon_id": "312071",
    "name": "NewName"
}
Body_add_pokeball = {
    "pokemon_id": "312071"
}

Responce_create = requests.post(url = f'{Url}/pokemons', headers = Header, json = Body_create)
print(Responce_create.text)

Responce_change_name = requests.patch(url = f'{Url}/pokemons', headers = Header, json = Body_change_name)
print(Responce_change_name.text)

Responce_add_pokeball = requests.post(url = f'{Url}/trainers/add_pokeball', headers = Header, json = Body_add_pokeball)
print(Responce_add_pokeball.text)
