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

if __name__ == "__main__":
    kortti = Maksukortti(10)
    print("Rahaa", kortti.saldo)
    tulos = kortti.ota_rahaa(8)
    print("Onnistuiko otto:", tulos)
    print("Rahaa", kortti.saldo)
    tulos = kortti.ota_rahaa(4)
    print("Onnistuiko otto:", tulos)
    print("Rahaa", kortti.saldo)