class Henkilo:
    def __init__(self, nimi:str, ika:int, pituus:int, paino:int) -> None:
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def __init__(self) -> None:
        self.punnitukset_maara = 0

    def punnitse(self, henkilo: Henkilo) -> int:
        self.punnitukset_maara += 1
        return henkilo.paino
    
    def syota(self, henkilo:Henkilo) -> None:
        henkilo.paino += 1
    
    def punnitukset(self) -> int:
        return self.punnitukset_maara
    
if __name__ == "__main__":
    haagan_neuvola = Kasvatuslaitos()

    eero = Henkilo("Eero", 1, 110, 7)
    pekka = Henkilo("Pekka", 33, 176, 85)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")