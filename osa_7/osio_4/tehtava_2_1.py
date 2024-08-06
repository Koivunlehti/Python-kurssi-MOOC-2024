import urllib.request
import json

def hae_kaikki() -> list:
    tiedot = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    kurssit = json.loads(tiedot.read())

    kurssit_menossa = []
    for kurssi in kurssit:
        if kurssi["enabled"] == True:
            harjoitukset = sum(kurssi["exercises"])
            kurssit_menossa.append((kurssi["fullName"], kurssi["name"], kurssi["year"], harjoitukset))

    return kurssit_menossa

if __name__ == "__main__":

    print(hae_kaikki())