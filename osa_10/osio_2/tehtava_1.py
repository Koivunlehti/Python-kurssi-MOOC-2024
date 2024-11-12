class SuperSankari:
    def __init__(self, nimi:str, kyvyt:str) -> None:
        self._nimi = nimi
        self._kyvyt = kyvyt

    def __str__(self) -> str:
        return f"{self._nimi}, superkyvyt: {self._kyvyt}"

class SuperRyhma:
    def __init__(self, nimi:str, kotipaikka:str) -> None:
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet:list[SuperSankari] = []

    @property
    def nimi(self):
        return self._nimi
    
    @property
    def kotipaikka(self):
        return self._kotipaikka
    
    def lisaa_jasen(self,sankari:SuperSankari):
        self._jasenet.append(sankari)
    
    def tulosta_ryhma(self):
        print(f"{self._nimi}, {self._kotipaikka}")
        print("Jäsenet:")
        for jasen in self._jasenet:
            print(jasen)

if __name__ == "__main__":
    supermiekkonen = SuperSankari("Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()