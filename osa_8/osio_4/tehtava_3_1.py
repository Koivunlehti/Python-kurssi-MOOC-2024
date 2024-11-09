class Lukutilasto:
    def __init__(self):
        self.lukuja = 0

    def lisaa_luku(self, luku:int) -> None:
        self.lukuja += 1

    def lukujen_maara(self) -> int:
        return self.lukuja

if __name__ == "__main__":
    tilasto = Lukutilasto()
    tilasto.lisaa_luku(3)
    tilasto.lisaa_luku(5)
    tilasto.lisaa_luku(1)
    tilasto.lisaa_luku(2)
    print("Lukujen määrä:", tilasto.lukujen_maara())