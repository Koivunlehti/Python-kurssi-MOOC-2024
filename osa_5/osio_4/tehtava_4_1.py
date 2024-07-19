def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = "ei suorituksia"

def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(nimi + ":")
        print(" ei suorituksia")
    else:
        print("ei löytynyt ketään nimellä", nimi)
    pass


if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Pekka")
    tulosta(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Jukka")