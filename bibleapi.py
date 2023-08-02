import requests
import json

base_url = 'https://bible-api.com/'
query = input("Enter Bible Verse: ")

r = requests.get(f'{base_url}{query}', verify=False)
r = r.json()
verse = r['text']

print(verse)
