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

    def syo_edullisesti(self, maksu: float):
        if maksu >= 2.50:
            self.edulliset += 1
            self.rahaa += 2.50
            return maksu - 2.50
        else:
            return maksu

    def syo_maukkaasti(self, maksu: float):
        if maksu >= 4.30:
            self.maukkaat += 1
            self.rahaa += 4.30
            return maksu - 4.30
        else:
            return maksu

if __name__ == "__main__":
    exactum = Kassapaate()

    vaihtorahaa = exactum.syo_edullisesti(10)
    print("Vaihtorahaa jäi", vaihtorahaa)

    vaihtorahaa = exactum.syo_edullisesti(5)
    print("Vaihtorahaa jäi", vaihtorahaa)

    vaihtorahaa = exactum.syo_maukkaasti(4.3)
    print("Vaihtorahaa jäi", vaihtorahaa)

    print("Kassassa rahaa", exactum.rahaa)
    print("Edullisia lounaita myyty", exactum.edulliset)
    print("Maukkaita lounaita myyty", exactum.maukkaat)