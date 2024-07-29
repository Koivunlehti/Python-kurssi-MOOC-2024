def hae_tiedostosta(tiedosto: str) -> dict:
    reseptit = {}
    with open("osa_6/osio_1/" + tiedosto) as sisalto:
        nimi = ""
        tiedot = []
        for rivi in sisalto:
            rivi = rivi.replace("\n","")
            if nimi == "":
                nimi = rivi
            else:
                if rivi == "":
                    reseptit[nimi] = tiedot
                    nimi = ""
                    tiedot = []
                else:
                    tiedot.append(rivi)
    reseptit[nimi] = tiedot

    return reseptit

def hae_nimi(tiedosto: str, sana: str) -> list:
    reseptit = hae_tiedostosta(tiedosto)
    loydetyt = []
    for resepti in reseptit:
        if sana.lower() in resepti.lower():
            loydetyt.append(resepti)

    return loydetyt

if __name__ == "__main__":
    loydetyt = hae_nimi("reseptit1.txt", "pulla")

    for resepti in loydetyt:
        print(resepti)