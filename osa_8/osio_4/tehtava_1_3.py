class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        if self.arvo - 1 >= 0:
            self.arvo -= 1

    def nollaa(self):
        self.arvo = 0

if __name__ == "__main__":
    laskuri = VahenevaLaskuri(100)
    laskuri.tulosta_arvo()
    laskuri.nollaa()
    laskuri.tulosta_arvo()