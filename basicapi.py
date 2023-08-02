from urllib import response
import requests
import json

r = requests.get('https://api.chucknorris.io/jokes/random', verify=False)

r = r.json()
punchline = r['value']

print(f'I have a good Chuck Norris joke for you... {punchline}')
