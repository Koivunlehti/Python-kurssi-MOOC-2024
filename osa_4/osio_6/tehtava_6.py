def lue_kayttajalta():
    # Luetaan käyttäjän syötteet
    syotteet = []
    while True:
        syote = input("Koepisteet ja harjoitusten määrä: ")
        if syote != "":
            syotteet.append(syote)
        else:
            break
    return syotteet

def tilasto(tiedot):
    # Tulostetaan tilastot
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {laske_keskiarvo(tiedot):.1f}")
    arvosanat = luo_arvosanat(tiedot)
    print(f"Hyvaksymisprosentti: {laske_hyvaksymisprosentti(arvosanat):.1f}")
    tulosta_arvosanajakauma(arvosanat)

def laske_tehtava_pisteet(tehtava_maara):
    # Tehtyjen tehtävien muunto pisteiksi
    return tehtava_maara // 10

def laske_keskiarvo(tiedot):
    # Koe- ja tehtäväpisteiden keskiarvo
    summa = 0
    for tietue in tiedot:
        summa += int(tietue.split(" ")[0])
        summa += laske_tehtava_pisteet(int(tietue.split(" ")[1]))
    return summa / len(tiedot)

def laske_hyvaksymisprosentti(arvosanat):
    # Hyväksytysti suoritettujen osuus kaikista suorituksista
    hyvaksytyt = 0
    for arvosana in arvosanat:
        if arvosana > 0:
            hyvaksytyt += 1
    return hyvaksytyt * 100 / len(arvosanat)

def luo_arvosanat(tiedot):
    # Luodaan arvosanat suorituksista
    arvosanat = []
    for tietue in tiedot:
        arvosana = 0
        koepisteet = int(tietue.split(" ")[0])
        tehtava_pisteet = laske_tehtava_pisteet(int(tietue.split(" ")[1]))
        pisteet = koepisteet + tehtava_pisteet
        if koepisteet < 10:
            arvosana = 0
        else:
            if pisteet >= 10 and pisteet <= 14:
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
        arvosanat.append(arvosana)
    return arvosanat

def tulosta_arvosanajakauma(arvosanat):
    # Tulostetaan taulukko eri arvosanojen määristä
    maarat = [0,0,0,0,0,0]
    for arvosana in arvosanat:
        maarat[arvosana] += 1 
    print("Arvosanajakauma:")
    for i in range(len(maarat) - 1, -1,-1):
        print(f"  {i}:", "*" * maarat[i])
    
def main():
    syotteet = lue_kayttajalta() # Koepisteet 0-20, tehtävät 0-100
    #syotteet = ["15 87", "10 55", "11 40", "4 17"]
    tilasto(syotteet)

main()