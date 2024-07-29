import math

def hae_asematiedot(tiedosto: str) -> dict:
    with open("osa_6/osio_1/" + tiedosto) as sisalto:
        tiedot = {}
        for rivi in sisalto:
            tieto = rivi.split(";")
            if tieto[0] != "Longitude":
                tiedot[tieto[3]] = (tieto[0],tieto[1])
    return tiedot

def etaisyys(asemat: dict, asema1: str, asema2: str):
    x_kilometreina = (float(asemat[asema1][0]) - float(asemat[asema2][0])) * 55.26
    y_kilometreina = (float(asemat[asema1][1]) - float(asemat[asema2][1])) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys

def suurin_etaisyys(asemat: dict):
    suurin = ("","",0.0)
    
    for nimi in asemat:
        for toinen_nimi in asemat:
            if toinen_nimi != nimi:
                asemien_etaisyys = etaisyys(asemat,nimi,toinen_nimi)
                if asemien_etaisyys > suurin[2]:
                    suurin = (nimi,toinen_nimi,asemien_etaisyys)
    
    return suurin

if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)