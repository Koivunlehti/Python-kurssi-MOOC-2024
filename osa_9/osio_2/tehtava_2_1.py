class Lahja:
    def __init__(self, nimi:str, paino:int) -> None:
        self.nimi = nimi
        self.paino = paino
    
    def __str__(self) -> str:
        return f"{self.nimi} ({self.paino} kg)"

if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)

    print("Lahjan nimi:", kirja.nimi)
    print("Lahjan paino:" ,kirja.paino)
    print("Lahja:", kirja)