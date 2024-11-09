class Lukutilasto:
    def __init__(self):
        self.lukuja = []

    def lisaa_luku(self, luku:int) -> None:
        self.lukuja.append(luku)

    def lukujen_maara(self) -> int:
        return len(self.lukuja)

    def summa(self) -> int:
        return sum(self.lukuja)

    def keskiarvo(self) -> float:
        return sum(self.lukuja) / len(self.lukuja)

if __name__ == "__main__":
    tilasto = Lukutilasto()
    tilasto.lisaa_luku(3)
    tilasto.lisaa_luku(5)
    tilasto.lisaa_luku(1)
    tilasto.lisaa_luku(2)
    print("Lukujen määrä:", tilasto.lukujen_maara())
    print("Summa:", tilasto.summa())
    print("Keskiarvo:", tilasto.keskiarvo())