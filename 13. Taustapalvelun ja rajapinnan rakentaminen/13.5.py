import requests
import json

hakusana = input("Anna hakusana: ")

pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:

    vastaus = requests.get(pyynto)

    if vastaus.status_code == 200:

        json_vastaus = vastaus.json()

        print(json.dumps(json_vastaus, indent=2))

        print("\nLöydetyt ohjelmat:\n")

        for ohjelma in json_vastaus:
            print(ohjelma["show"]["name"])

    else:
        print("Virhe HTTP-pyynnössä.")
        print("Statuskoodi:", vastaus.status_code)

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")
