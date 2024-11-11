class Henkilo:
    def __init__(self, nimi:str, pituus:int) -> None:
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self) -> str:
        return f"{self.nimi} ({self.pituus} cm)"

class Huone:
    def __init__(self) -> None:
        self.henkilot:list[Henkilo] = []
        self.pituudet_yht = 0

    def lisaa(self, henkilo:Henkilo):
        self.henkilot.append(henkilo)
        self.pituudet_yht += henkilo.pituus

    def on_tyhja(self):
        return False if len(self.henkilot) > 0 else True

    def tulosta_tiedot(self):
        print(f"Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {self.pituudet_yht} cm")
        for henkilo in self.henkilot:
            print(henkilo)

if __name__ == "__main__":
    huone = Huone()
    print("Huone tyhjä?", huone.on_tyhja())
    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Auli", 186))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Terhi", 185))
    print("Huone tyhjä?", huone.on_tyhja())
    huone.tulosta_tiedot()