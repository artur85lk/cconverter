import requests
import json


first = str(input())
cache = first
r = requests.get(f'http://www.floatrates.com/daily/{cache}.json')
content = json.loads(r.text)
if first.lower() != "usd":
    dolar = content['usd']['inverseRate']
if first.lower() != "eur":
    euro = content['eur']['inverseRate']
cache2 = {}
waluta = 0
while True:
    second = str(input()).lower()
    if second == "":
        break
    how_many = float(input())

    if second in cache2.keys():
        result = round((float(how_many) / (float(cache2[second]))), 2)
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print(f"You received {result} {second.upper()}.")
        cache2 = {second: str(waluta)}
        continue

    print("Checking the cache...")
    if second == "eur":
        print("Oh! It is in the cache!")
        result = round((float(how_many) / float(euro)), 2)
        print(f"You received {result} {second.upper()}.")
    elif second == "usd":
        print("Oh! It is in the cache!")
        result = round((float(how_many) / float(dolar)), 2)

        print(f"You received {result} {second.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")

        r = requests.get(f'http://www.floatrates.com/daily/{cache}.json')

        content = json.loads(r.text)
        waluta = float(content[second]['inverseRate'])
    # print(content['eur']['inverseRate'])

        result = round((float(how_many) / waluta), 2)
        print(f"You received {result} {second.upper()}.")
    cache2[second] = str(waluta)
