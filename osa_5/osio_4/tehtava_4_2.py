def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(nimi + ":")
        if len(opiskelijat[nimi]) == 0:
            print(" ei suorituksia")
        else:
            print(f" suorituksia {len(opiskelijat[nimi])} kurssilta:")
            arvosana_summa = 0
            for kurssi in opiskelijat[nimi]:
                print(f"  {kurssi[0]} {kurssi[1]}")
                arvosana_summa += kurssi[1]
            print(f" keskiarvo {arvosana_summa / len(opiskelijat[nimi])}")
    else:
        print("ei löytynyt ketään nimellä", nimi)

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    if nimi in opiskelijat:
        opiskelijat[nimi].append(suoritus)

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    tulosta(opiskelijat, "Pekka")