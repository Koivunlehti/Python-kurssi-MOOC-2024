class Henkilo:
    def __init__(self, nimi:str, ika:int, pituus:int, paino:int) -> None:
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def punnitse(self, henkilo: Henkilo):
        return henkilo.paino
    
if __name__ == "__main__":
    haagan_neuvola = Kasvatuslaitos()

    eero = Henkilo("Eero", 1, 110, 7)
    pekka = Henkilo("Pekka", 33, 176, 85)

    print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
    print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")