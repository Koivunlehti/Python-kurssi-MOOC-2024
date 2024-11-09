class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        self.arvo -= 1


if __name__ == "__main__":
    laskuri = VahenevaLaskuri(10)
    laskuri.tulosta_arvo()
    laskuri.vahenna()
    laskuri.tulosta_arvo()
    laskuri.vahenna()
    laskuri.tulosta_arvo()