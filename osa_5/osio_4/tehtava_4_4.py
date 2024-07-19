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

def kooste(opiskelijat: dict):
    
    eniten_suorituksia = ["",0]
    paras_keskiarvo = ["",0]
    for nimi, suoritukset in opiskelijat.items():
        if eniten_suorituksia[1] < len(suoritukset):
            eniten_suorituksia = [nimi,len(suoritukset)]
        arvosana_summa = 0
        for kurssi in suoritukset:
            arvosana_summa += kurssi[1]
        if paras_keskiarvo[1] < arvosana_summa / len(suoritukset):
            paras_keskiarvo = [nimi, arvosana_summa / len(suoritukset)]

    print("opiskelijoita", len(opiskelijat))
    print(f"eniten suorituksia {eniten_suorituksia[1]} {eniten_suorituksia[0]}")
    print(f"paras keskiarvo {paras_keskiarvo[1]} {paras_keskiarvo[0]}")

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)