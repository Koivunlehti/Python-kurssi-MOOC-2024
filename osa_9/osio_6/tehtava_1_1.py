class Tavara:
    def __init__(self, nimi:str, paino:int) -> None:
        self.__nimi = nimi
        self.__paino = paino
    
    def nimi(self) -> None:
        return self.__nimi
    
    def paino(self) -> None:
        return self.__paino

    def __str__(self) -> str:
        return f"{self.__nimi} ({self.__paino} kg)"
    
if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)

    print("Kirjan nimi:", kirja.nimi())
    print("Kirjan paino:", kirja.paino())

    print("Kirja:", kirja)
    print("Puhelin:", puhelin)