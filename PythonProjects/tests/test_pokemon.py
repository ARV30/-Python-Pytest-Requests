import requests
import pytest

def test_get_trainers_status_code_200():
    url = "https://api.pokemonbattle.me:9104/trainers"
    headers = {
        'Content-Type': 'application/json',
        "trainer_token": "fb5411f93a4057c8907af38ddabaedbf",
    }

    response = requests.get(url, headers=headers, verify=False, timeout=5)
    assert response.status_code == 200


def test_get_trainers():
    url = "https://api.pokemonbattle.me:9104/trainers"
    headers = {
        'Content-Type': 'application/json',
        "trainer_token": "fb5411f93a4057c8907af38ddabaedbf",
    }

    response = requests.get(url, headers=headers, params={'trainer_id': 3894}, verify=False, timeout=5)
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'Роман'