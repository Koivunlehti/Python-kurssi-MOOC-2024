def lue_tiedostosta() -> list:
    tiedot = []
    with open("osa_6/osio_2/sanat.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            tiedot.append(rivi.lower())

    return tiedot

def hae_sanat(hakusana: str):
    hakusana = hakusana.lower()
    sanat = lue_tiedostosta()
    loydetyt = []

    for sana in sanat:
        if hakusana.find(".") != -1:
            if len(hakusana) == len(sana):
                sopiva = True
                for i in range(len(sana)):
                    if hakusana[i] != sana[i] and hakusana[i] != ".":
                        sopiva = False
                if sopiva:
                    loydetyt.append(sana)
        if hakusana.find("*") != -1:
            if hakusana.find("*") == 0:
                if sana.endswith(hakusana[1:]):
                    loydetyt.append(sana)
            elif hakusana.find("*") == len(hakusana) - 1:
                if sana.startswith(hakusana[0:len(hakusana)-2]):
                    loydetyt.append(sana)
        else:
            if sana == hakusana:
                loydetyt.append(sana)
    return loydetyt

if __name__ == "__main__":
    print(hae_sanat("cat"))
    print(hae_sanat("home"))
    print(hae_sanat("ca."))
    print(hae_sanat("p.ng"))
    print(hae_sanat(".a.e"))
    print(hae_sanat("*vokes"))
    print(hae_sanat("re*"))
    