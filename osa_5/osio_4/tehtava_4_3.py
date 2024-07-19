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
        if suoritus[1] > 0:
            olemassa_index = -1
            for i in range(len(opiskelijat[nimi])):
                if opiskelijat[nimi][i][0] == suoritus[0]:
                    olemassa_index = i
                    break
                
            if olemassa_index != -1:
                if opiskelijat[nimi][i][1] < suoritus[1]:
                    opiskelijat[nimi].pop(i)
                    opiskelijat[nimi].append(suoritus)
            else:
                opiskelijat[nimi].append(suoritus)

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
    tulosta(opiskelijat, "Pekka")