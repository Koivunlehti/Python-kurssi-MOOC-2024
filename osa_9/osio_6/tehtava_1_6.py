class Tavara:
    def __init__(self, nimi:str, paino:int) -> None:
        self.__nimi = nimi
        self.__paino = paino
    
    def nimi(self) -> str:
        return self.__nimi
    
    def paino(self) -> int:
        return self.__paino

    def __str__(self) -> str:
        return f"{self.__nimi} ({self.__paino} kg)"

class Matkalaukku:
    def __init__(self, max_paino:int) -> None:
        self.__max_paino = max_paino
        self.__tavarat:list[Tavara] = []

    def lisaa_tavara(self, tavara:Tavara) -> None:
        if self.__yhteispaino() + tavara.paino() <= self.__max_paino:
            self.__tavarat.append(tavara)

    def __yhteispaino(self) -> int:
        yht_paino = 0
        for tavara in self.__tavarat:
            yht_paino += tavara.paino()
        return yht_paino

    def __str__(self) -> str:
        return f"{len(self.__tavarat)} tavara{'a' if len(self.__tavarat) != 1 else ''} ({self.__yhteispaino()} kg)"

    def tulosta_tavarat(self) -> None:
        for tavara in self.__tavarat:
            print(tavara)
    
    def paino(self) -> int:
        return self.__yhteispaino() 

    def raskain_tavara(self) -> None | Tavara:
        if len(self.__tavarat) > 0:
            raskain = self.__tavarat[0]
            for tavara in self.__tavarat:
                if tavara.paino() > raskain.paino():
                    raskain = tavara
            return raskain
        else:
            return None

class Lastiruuma:
    def __init__(self, max_paino:int) -> None:
        self.__max_paino = max_paino
        self.__rahti:list[Matkalaukku] = []
    
    def lisaa_matkalaukku(self, matkalaukku:Matkalaukku):
        if self.__yhteispaino() + matkalaukku.paino() <= self.__max_paino:
            self.__rahti.append(matkalaukku)
    
    def __yhteispaino(self) -> int:
        yht_paino = 0
        for laukku in self.__rahti:
            yht_paino += laukku.paino()
        return yht_paino

    def __str__(self) -> str:
        return f"{len(self.__rahti)} matkalaukkua, tilaa {self.__max_paino - self.__yhteispaino()} kg"

if __name__ == "__main__":
    lastiruuma = Lastiruuma(1000)
    print(lastiruuma)

    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma.lisaa_matkalaukku(adan_laukku)
    print(lastiruuma)

    lastiruuma.lisaa_matkalaukku(pekan_laukku)
    print(lastiruuma)