import requests
import pytest

Url = 'https://api.pokemonbattle.ru/v2'
Token = 'User_Token'
Header = {'Content-Type':'application/json', 'trainer_token':Token}

def test_get_trainers_200():
    responce = requests.get(url = f'{Url}/trainers', headers = Header)
    assert responce.status_code == 200

def test_get_trainers_mine():
    responce_my_trainer = requests.get(url = f'{Url}/trainers', headers = Header, params = {'trainer_id':'32518'})
