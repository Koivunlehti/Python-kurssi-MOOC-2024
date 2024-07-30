def lue_tiedosto_csv(tiedostonimi: str) -> dict:
    # Luetaan annettu tiedosto ja palautetaan tiedoista luotu sanakirja
    tiedot = {}
    with open("osa_6/osio_2/" + tiedostonimi) as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            lista = rivi.split(";")
            if lista[0] == "opnro":
                continue
            tiedot[lista[0]] = lista[1:]
    return tiedot

def lue_kurssin_tiedot(tiedostonimi: str) -> list:
    kurssi = []
    with open("osa_6/osio_2/" + tiedostonimi) as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            rivi = rivi.split(": ")
            kurssi.append(rivi[1])
    return kurssi

def kirjoita_tiedostoon_txt(tiedostonimi: str, tiedot: list):
    with open("osa_6/osio_2/" + tiedostonimi, "w", encoding="UTF-8") as tiedosto:
        for tieto in tiedot:
            tiedosto.write(tieto + "\n")

def kirjoita_tiedostoon_csv(tiedostonimi: str, tiedot: list):
    with open("osa_6/osio_2/" + tiedostonimi, "w", encoding="UTF-8") as tiedosto:
        for tieto in tiedot:
            tiedosto.write(f"{tieto[0]};{tieto[1]};{tieto[2]}\n")

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

def tulosta(oppilaat: dict,teht_maarat: dict, kokeet: dict, arvosanat: dict, kurssi: list):
    # Muuttujat tiedostojen sisältöjä varten
    sisalto_txt = [f"{kurssi[0]}, {kurssi[1]} opintopistettä"]
    sisalto_txt.append("=" * len(sisalto_txt[0]))
    sisalto_csv = []

    # Luodaan tiedostojen sisällöt:
    # .txt sarakkeiden otsikot
    otsikot = ["nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"]
    otsikko = ""
    for i in range(len(otsikot)): 
        if i == 0:
            otsikko += f"{otsikot[i]:30}"
        else:
            otsikko += f"{otsikot[i]:10}"
    sisalto_txt.append(otsikko)

    # Kerätään .txt ja .csv sisällöt
    for id, tiedot in oppilaat.items():
        nimi = tiedot[0] + " " + tiedot[1]
        pisteet = laske_tehtava_pisteet(teht_maarat[id],40)
        koepisteet = 0
        for koepiste in kokeet[id]:
            koepisteet += int(koepiste)
        yhteispisteet = koepisteet + pisteet
        sisalto_txt.append(f"{nimi:30}{teht_maarat[id]:<10}{pisteet:<10}{koepisteet:<10}{yhteispisteet:<10}{arvosanat[id]}")
        sisalto_csv.append((id,f"{tiedot[0]} {tiedot[1]}", arvosanat[id]))

    # Kirjoitetaan tiedostoon
    kirjoita_tiedostoon_txt("tulos.txt", sisalto_txt)
    kirjoita_tiedostoon_csv("tulos.csv", sisalto_csv)

    print("Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv")

def main():
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koetiedot = input("Koepisteet: ")
    kurssitiedot = input("Kurssin tiedot: ")

    oppilaat = lue_tiedosto_csv(opiskelijatiedot)
    tehtavat = lue_tiedosto_csv(tehtavatiedot)
    kokeet = lue_tiedosto_csv(koetiedot)
    kurssi = lue_kurssin_tiedot(kurssitiedot)

    tehtavamaarat = laske_tehtavamaarat(tehtavat)
    arvosanat = laske_arvosanat(kokeet, tehtavamaarat)

    # Tulostetaan tiedot
    tulosta(oppilaat,tehtavamaarat,kokeet,arvosanat,kurssi)

main()