def lue_tiedosto(tiedostonimi: str) -> dict:
    # Luetaan annettu tiedosto ja palautetaan tiedoista luotu sanakirja
    tiedot = {}
    with open("osa_6/osio_1/" + tiedostonimi) as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            lista = rivi.split(";")
            if lista[0] == "opnro":
                continue
            tiedot[lista[0]] = lista[1:]
    return tiedot

def laske_tehtavamaarat(tehtavat: dict) -> dict:
    # Lasketaan tehtyjen tehtävien määrät ja palautetaan niistä luotu sanakirja
    maarat = {}
    for id, tehdyt in tehtavat.items():
        yhteensa = 0
        for maara in tehdyt:
            yhteensa += int(maara)
        maarat[id] = yhteensa
    return maarat

def laske_tehtava_pisteet(tehtava_maara: int, max_tehtavamaara: int) -> int:
    # Tehtyjen tehtävien muunto pisteiksi
    prosentit = tehtava_maara * 100 // max_tehtavamaara
    pisteet = 10
    if prosentit == 100:
        return 10
    else:
        for i in range(100,0,-10):
            if prosentit < i:
                pisteet -= 1
    return pisteet

def laske_arvosanat(kokeet: dict, tehtavamaarat: dict, max_tehtavamaara: int = 40) -> dict:
    # Luodaan arvosanat suorituksista ja palautetaan niistä sanakirja
    arvosanat = {}
    for id, tulokset in kokeet.items():
        arvosana = 0
        koepisteet = 0
        for pisteet in tulokset:
            koepisteet += int(pisteet)
        tehtava_pisteet = laske_tehtava_pisteet(tehtavamaarat[id], max_tehtavamaara)
        pisteet = koepisteet + tehtava_pisteet
        if pisteet <= 14:
            arvosana = 0
        elif pisteet >= 15 and pisteet <= 17:
            arvosana = 1
        elif pisteet >= 18 and pisteet <= 20:
            arvosana = 2
        elif pisteet >= 21 and pisteet <= 23:
            arvosana = 3
        elif pisteet >= 24 and pisteet <= 27:
            arvosana = 4
        elif pisteet >= 28 and pisteet <= 30:
            arvosana = 5
        arvosanat[id] = arvosana
    return arvosanat

def tulosta(oppilaat: dict,teht_maarat: dict, kokeet: dict, arvosanat: dict):
    # Luodaan taulukkomuotoinen tulostus
    otsikot = ["nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"]
    otsikko = ""
    for i in range(len(otsikot)): 
        if i == 0:
            otsikko += f"{otsikot[i]:30}"
        else:
            otsikko += f"{otsikot[i]:10}"
    print(otsikko)
    for id, tiedot in oppilaat.items():
        nimi = tiedot[0] + " " + tiedot[1]
        pisteet = laske_tehtava_pisteet(teht_maarat[id],40)
        koepisteet = 0
        for koepiste in kokeet[id]:
            koepisteet += int(koepiste)
        yhteispisteet = koepisteet + pisteet
        print(f"{nimi:30}{teht_maarat[id]:<10}{pisteet:<10}{koepisteet:<10}{yhteispisteet:<10}{arvosanat[id]}")

def main():
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koetiedot = input("Koepisteet: ")

    oppilaat = lue_tiedosto(opiskelijatiedot)
    tehtavat = lue_tiedosto(tehtavatiedot)
    kokeet = lue_tiedosto(koetiedot)

    tehtavamaarat = laske_tehtavamaarat(tehtavat)
    arvosanat = laske_arvosanat(kokeet, tehtavamaarat)

    # Tulostetaan
    tulosta(oppilaat,tehtavamaarat,kokeet,arvosanat)

main()