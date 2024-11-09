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

# Pääohjelma
tilasto = Lukutilasto()
print("Anna lukuja:")

while True:
    luku = int(input())
    if luku >= 0:
        tilasto.lisaa_luku(luku)
    else:
        break

print(f"Summa: {tilasto.summa()}")
print(f"Keskiarvo: {tilasto.keskiarvo()}")