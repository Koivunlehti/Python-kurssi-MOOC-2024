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
        return f"{len(self.__tavarat)} tavaraa ({self.__yhteispaino()} kg)"

if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    matkalaukku = Matkalaukku(5)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(kirja)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(puhelin)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(tiiliskivi)
    print(matkalaukku)