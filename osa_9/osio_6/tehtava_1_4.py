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

if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    matkalaukku = Matkalaukku(10)
    matkalaukku.lisaa_tavara(kirja)
    matkalaukku.lisaa_tavara(puhelin)
    matkalaukku.lisaa_tavara(tiiliskivi)

    print("Matkalaukussa on seuraavat tavarat:")
    matkalaukku.tulosta_tavarat()
    paino_yht = matkalaukku.paino()
    print(f"Yhteispaino: {paino_yht} kg")