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

    def lyhin(self) -> None | str:
        if len(self.henkilot) > 0:
            lyhin = self.henkilot[0]
            for henkilo in self.henkilot:
                if henkilo.pituus < lyhin.pituus:
                    lyhin = henkilo
            return lyhin.nimi
        else:
            return None 

    def poista_lyhin(self) -> None | Henkilo:
        if len(self.henkilot) > 0:
            lyhin_henkilo = self.lyhin()
            poista_index = -1
            for i in range(len(self.henkilot)):
                if self.henkilot[i].nimi == lyhin_henkilo:
                    poista_index = i
                    break
            poistettu_henkilo = self.henkilot.pop(poista_index)
            self.pituudet_yht -= poistettu_henkilo.pituus
            return poistettu_henkilo
        else:
            return None

if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()