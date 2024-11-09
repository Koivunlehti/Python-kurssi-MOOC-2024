class Maksukortti:
    def __init__(self, alkusaldo: float) -> None:
        self.saldo = alkusaldo

    def __str__(self) -> str:
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"
     
    def syo_edullisesti(self):
        if self.saldo - 2.60 >= 0:
            self.saldo -= 2.60

    def syo_maukkaasti(self):
        if self.saldo - 4.60 >= 0:
            self.saldo -= 4.60

if __name__ == "__main__":
    kortti = Maksukortti(50)
    print(kortti)

    kortti.syo_edullisesti()
    print(kortti)

    kortti.syo_maukkaasti()
    kortti.syo_edullisesti()
    print(kortti)

    print()
    
    kortti = Maksukortti(4)
    print(kortti)

    kortti.syo_edullisesti()
    print(kortti)

    kortti.syo_edullisesti()
    print(kortti)