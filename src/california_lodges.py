import requests
import bs4
import json


url = 'https://www.freemason.org/json/lodgeLocator'
query = {
    'method': 'getAllLodges',
    '_': '1538511871298'
}

req = requests.get(url, params=query)
text = req.text
json_body = json.loads(text)

for l in json_body['locations']:
    lodge = l['lodges'][0]
    print(lodge['phone'] if 'phone' in lodge else '')
