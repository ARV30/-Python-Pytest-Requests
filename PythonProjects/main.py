import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    "trainer_token": "fb5411f93a4057c8907af38ddabaedbf",
}

body = {
    "pokemon_id": "29746",
    "name": "Mavizzz",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.post(url=f"{URL}/pokemons", json=body, headers=HEADER, verify=False, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    "trainer_token": "fb5411f93a4057c8907af38ddabaedbf",
}

body = {
    "pokemon_id": "29871",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url=f"{URL}/pokemons", json=body, headers=HEADER, verify=False, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    "trainer_token": "fb5411f93a4057c8907af38ddabaedbf",
}

body = {
    "pokemon_id": "29871"
}
response = requests.post(url=f"{URL}/trainers/add_pokeball", json=body, headers=HEADER, verify=False, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')