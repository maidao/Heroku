import requests

url = 'https://myfirst-roku.herokuapp.com/'

params = {
    'superficie': 40,
    'nb_pieces': 2,
    'latitude': 45.769752,
    'longitude': 4.853208
}

session = requests.Session()
r = session.get(url=url, params=params)
print(r.text)