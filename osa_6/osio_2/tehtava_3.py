def lue_tiedostosta() -> list:
    tiedot = []
    with open("osa_6/osio_2/laskut.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            tiedot.append(rivi.split(";"))

    return tiedot

def kirjoita_tiedostoon(nimi: str, tiedot: list):
    with open("osa_6/osio_2/" + nimi, "w") as tiedosto:
        for rivi in tiedot:
            tiedosto.write(rivi[0] +";"+ rivi[1] +";"+ rivi[2] + "\n")

def suodata_laskut():
    laskut = lue_tiedostosta()
    oikein = []
    vaarin = []
    for lasku in laskut:
        if lasku[1].find("+") != -1:
            luvut = lasku[1].split("+")
            if int(luvut[0]) + int(luvut[1]) == int(lasku[2]):
                oikein.append(lasku)
            else:
                vaarin.append(lasku)
        elif lasku[1].find("-") != -1:
            luvut = lasku[1].split("-")
            if int(luvut[0]) - int(luvut[1]) == int(lasku[2]):
                oikein.append(lasku)
            else:
                vaarin.append(lasku)
    
    kirjoita_tiedostoon("oikein.csv", oikein)
    kirjoita_tiedostoon("vaarin.csv", vaarin)

if __name__ == "__main__":
    suodata_laskut()
    suodata_laskut()
    suodata_laskut()
    suodata_laskut()