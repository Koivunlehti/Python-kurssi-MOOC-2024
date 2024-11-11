class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if self.saldo - maara >= 0:
            self.saldo -= maara
            return True
        else:
            return False

class Kassapaate:
    def __init__(self):
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0
        self.edullinen_hinta = 2.50
        self.maukas_hinta = 4.30

    def syo_edullisesti(self, maksu: float):
        if maksu >= self.edullinen_hinta:
            self.edulliset += 1
            self.rahaa += self.edullinen_hinta
            return maksu - self.edullinen_hinta
        else:
            return maksu

    def syo_maukkaasti(self, maksu: float):
        if maksu >= self.maukas_hinta:
            self.maukkaat += 1
            self.rahaa += self.maukas_hinta
            return maksu - self.maukas_hinta
        else:
            return maksu
        
    def syo_edullisesti_kortilla(self, kortti: Maksukortti):
        if kortti.ota_rahaa(self.edullinen_hinta):
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti: Maksukortti):
        if kortti.ota_rahaa(self.maukas_hinta):
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        kortti.lataa_rahaa(summa)
        self.rahaa += summa

if __name__ == "__main__":
    exactum = Kassapaate()

    antin_kortti = Maksukortti(2)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)

    exactum.lataa_rahaa_kortille(antin_kortti, 100)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    print("Kassassa rahaa", exactum.rahaa)
    print("Edullisia lounaita myyty", exactum.edulliset)
    print("Maukkaita lounaita myyty", exactum.maukkaat)