"""
Llamada a api en python
"""

import requests

url ="https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)

print(response.json())
