import requests
import json

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
query = input("Enter a drink name: ")

r = requests.get(f'{base_url}{query}', verify=False)
result = r.json()['drinks']

instructions = result[0]['strInstructions']
print(f'Intructions: {instructions}')
