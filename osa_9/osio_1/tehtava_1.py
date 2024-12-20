class Auto:
    def __init__(self, merkki:str, huippunopeus:int) -> None:
        self.merkki = merkki
        self.huippunopeus = huippunopeus

def nopein_auto(autot:list[Auto]):
    nopein = autot[0]
    for auto in autot:
        if auto.huippunopeus > nopein.huippunopeus:
            nopein = auto
    return nopein.merkki

if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Ferrari", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))
