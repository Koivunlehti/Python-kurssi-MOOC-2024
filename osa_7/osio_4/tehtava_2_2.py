import urllib.request
import json
import math

def hae_kaikki() -> list:
    tiedot = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    kurssit = json.loads(tiedot.read())

    kurssit_menossa = []
    for kurssi in kurssit:
        if kurssi["enabled"] == True:
            harjoitukset = sum(kurssi["exercises"])
            kurssit_menossa.append((kurssi["fullName"], kurssi["name"], kurssi["year"], harjoitukset))

    return kurssit_menossa

def hae_kurssi(kurssi: str) -> dict:
    tiedot = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/"+kurssi+"/stats")
    tiedot = json.loads(tiedot.read())

    kurssin_tiedot = {}
    kurssin_tiedot["viikkoja"] = len(tiedot)

    opiskelijoita = 0
    tunteja = 0
    tunteja_keskimaarin = 0
    tehtavien_maara = 0

    for viikko, viikon_tiedot in tiedot.items():
        if opiskelijoita < viikon_tiedot["students"]:
            opiskelijoita = viikon_tiedot["students"]
        tunteja += viikon_tiedot["hour_total"]
        tehtavien_maara += viikon_tiedot["exercise_total"]

    tunteja_keskimaarin = math.floor(tunteja / opiskelijoita)
    tehtavia_keskimaarin = math.floor(tehtavien_maara / opiskelijoita)

    kurssin_tiedot["opiskelijoita"] = opiskelijoita
    kurssin_tiedot["tunteja"] = tunteja
    kurssin_tiedot["tunteja_keskimaarin"] = tunteja_keskimaarin
    kurssin_tiedot["tehtavia"] = tehtavien_maara
    kurssin_tiedot["tehtavia_keskimaarin"] = tehtavia_keskimaarin

    return kurssin_tiedot

if __name__ == "__main__":
    kurssit = hae_kaikki()

    print(hae_kurssi(kurssit[1][1]))

