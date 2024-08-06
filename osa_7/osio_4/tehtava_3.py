import csv
from datetime import time, timedelta

def huijarit() -> list:
    opiskelijat = {}
    with open("osa_7/osio_4/tentin_aloitus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            aika = rivi[1].split(":")
            aika = time(int(aika[0]),int(aika[1]))
            opiskelijat[rivi[0]] = {"aloitusaika":aika, "palautus":[]}

    with open("osa_7/osio_4/palautus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            aika = rivi[3].split(":")
            aika = time(int(aika[0]),int(aika[1]))
            opiskelijat[rivi[0]]["palautus"].append([rivi[1],rivi[2],aika])

    huijarit = []

    for opiskelija, tiedot in opiskelijat.items():
        for palautukset in tiedot["palautus"]:
            aloitus = timedelta(hours = tiedot["aloitusaika"].hour, minutes = tiedot["aloitusaika"].minute)
            palautus = timedelta(hours = palautukset[2].hour, minutes = palautukset[2].minute)   
            ero = palautus - aloitus
            if ero > timedelta(hours=3):
                if opiskelija not in huijarit:
                    huijarit.append(opiskelija)
    return huijarit

if __name__ == "__main__":
    print(huijarit())