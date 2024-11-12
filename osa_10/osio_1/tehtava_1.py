class Tietokone:
    def __init__(self, malli:str, nopeus:int) -> None:
        self.malli = malli
        self.nopeus = nopeus

class KannettavaTietokone(Tietokone):
    def __init__(self, malli: str, nopeus: int, paino:int) -> None:
        super().__init__(malli, nopeus)
        self.paino = paino
    
    def __str__(self) -> str:
        return f"{self.malli}, {self.nopeus} MHz, {self.paino} kg"

if __name__ == "__main__":
    ipm = KannettavaTietokone("IPM MikroMauri", 1500, 2)
    print(ipm)