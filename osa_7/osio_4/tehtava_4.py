import csv
from datetime import time, timedelta

def viralliset_pisteet() -> list:
    opiskelijat = {}
    with open("osa_7/osio_4/tentin_aloitus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            aika = rivi[1].split(":")
            aika = time(int(aika[0]),int(aika[1]))
            opiskelijat[rivi[0]] = {"aloitusaika":aika, "palautus":{}}

    with open("osa_7/osio_4/palautus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            nimi = rivi[0]
            tehtava = rivi[1]
            pisteet = rivi[2]
            if tehtava not in opiskelijat[nimi]["palautus"]:
                aika = rivi[3].split(":")
                aika = time(int(aika[0]),int(aika[1]))
                opiskelijat[nimi]["palautus"][tehtava] = [pisteet,aika]
            else:
                if pisteet > opiskelijat[nimi]["palautus"][tehtava][0]:
                    opiskelijat[nimi]["palautus"][tehtava] = [pisteet, aika]

    opiskelijat_tulokset = {}

    for opiskelija, tiedot in opiskelijat.items():
        pisteet = 0
        for tehtava, tehtava_tiedot in tiedot["palautus"].items():
            aloitus = timedelta(hours = tiedot["aloitusaika"].hour, minutes = tiedot["aloitusaika"].minute)
            palautus = timedelta(hours = tehtava_tiedot[1].hour, minutes = tehtava_tiedot[1].minute)   
            ero = palautus - aloitus
            if ero < timedelta(hours=3):
                pisteet += int(tehtava_tiedot[0])
        opiskelijat_tulokset[opiskelija] = pisteet

    return opiskelijat_tulokset

if __name__ == "__main__":
    print(viralliset_pisteet())