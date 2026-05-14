import requests

hakusana = input("Anna hakusana: ")

pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:

    vastaus = requests.get(pyynto)

    if vastaus.status_code == 200:

        json_vastaus = vastaus.json()

        for ohjelma in json_vastaus:

            nimi = ohjelma["show"]["name"]
            kieli = ohjelma["show"]["language"]
            tyyppi = ohjelma["show"]["type"]

            print("-------------------")
            print("Nimi:", nimi)
            print("Kieli:", kieli)
            print("Tyyppi:", tyyppi)

    else:
        print("Virhe:", vastaus.status_code)

except requests.exceptions.RequestException:
    print("Palveluun ei saada yhteyttä.")
