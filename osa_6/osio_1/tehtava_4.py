def lue_tiedosto(tiedostonimi: str):
    tiedot = {}
    with open("osa_6/osio_1/" + tiedostonimi) as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            lista = rivi.split(";")
            if lista[0] == "opnro":
                continue
            tiedot[lista[0]] = lista[1:]
    return tiedot

def laske_tehtavamaarat(tehtavat):
    maarat = {}
    for id, tehdyt in tehtavat.items():
        yhteensa = 0
        for maara in tehdyt:
            yhteensa += int(maara)
        maarat[id] = yhteensa
    return maarat


opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")

oppilaat = lue_tiedosto(opiskelijatiedot)
tehtavat = lue_tiedosto(tehtavatiedot)
tehtavamaarat = laske_tehtavamaarat(tehtavat)

for id, oppilas in oppilaat.items():
    print(f"{oppilas[0]} {oppilas[1]} {tehtavamaarat[id]}")