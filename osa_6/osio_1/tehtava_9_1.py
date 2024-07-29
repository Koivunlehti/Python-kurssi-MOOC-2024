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

if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    e = etaisyys(asemat, "Kaivopuisto", "Laivasillankatu")
    print(e)
    e = etaisyys(asemat, "Kapteeninpuistikko", "Kaivopuisto")
    print(e)