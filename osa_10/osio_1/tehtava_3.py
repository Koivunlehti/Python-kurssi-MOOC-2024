class Suorakulmio:
    def __init__(self, korkeus:int, leveys:int) -> None:
        self.korkeus = korkeus
        self.leveys = leveys
    
    def pinta_ala(self) -> int:
        return self.korkeus * self.leveys

    def __str__(self) -> str:
        return f"suorakulmio {self.korkeus}x{self.leveys}"

class Nelio(Suorakulmio):
    def __init__(self, korkeus: int) -> None:
        super().__init__(korkeus, korkeus)

if __name__ == "__main__":
    nelio = Nelio(4)
    print(nelio)
    print("pinta-ala:", nelio.pinta_ala())