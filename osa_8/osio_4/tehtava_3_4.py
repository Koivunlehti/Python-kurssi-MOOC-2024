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
parilliset = Lukutilasto()
parittomat = Lukutilasto()

print("Anna lukuja:")
while True:
    luku = int(input())
    if luku >= 0:
        tilasto.lisaa_luku(luku)
        if luku % 2 == 0:
            parilliset.lisaa_luku(luku)
        else:
            parittomat.lisaa_luku(luku)
    else:
        break

print(f"Summa: {tilasto.summa()}")
print(f"Keskiarvo: {tilasto.keskiarvo()}")
print(f"Parillisten summa: {parilliset.summa()}")
print(f"Parittomien summa: {parittomat.summa()}")