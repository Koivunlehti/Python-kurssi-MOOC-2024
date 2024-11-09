class Maksukortti:
    def __init__(self, alkusaldo: float) -> None:
        self.saldo = alkusaldo

    def __str__(self) -> str:
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"
     
    def syo_edullisesti(self) -> None:
        if self.saldo - 2.60 >= 0:
            self.saldo -= 2.60

    def syo_maukkaasti(self) -> None:
        if self.saldo - 4.60 >= 0:
            self.saldo -= 4.60
    
    def lataa_rahaa(self, maara:float) -> None:
        if maara < 0:
            raise ValueError("Kortille ei saa ladata negatiivista summaa")
        self.saldo += maara

if __name__ == "__main__":
    kortti = Maksukortti(10)
    print(kortti)
    kortti.lataa_rahaa(15)
    print(kortti)
    kortti.lataa_rahaa(10)
    print(kortti)
    kortti.lataa_rahaa(200)
    print(kortti)

    print()
    
    kortti = Maksukortti(10)
    kortti.lataa_rahaa(-10)