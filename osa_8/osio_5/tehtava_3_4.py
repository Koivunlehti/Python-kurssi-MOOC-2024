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
    pekan_kortti = Maksukortti(20)
    matin_kortti = Maksukortti(30)
    
    pekan_kortti.syo_maukkaasti()
    matin_kortti.syo_edullisesti()
    print(f"Pekka: {pekan_kortti}")
    print(f"Matti: {matin_kortti}")
    pekan_kortti.lataa_rahaa(20)
    matin_kortti.syo_maukkaasti()
    print(f"Pekka: {pekan_kortti}")
    print(f"Matti: {matin_kortti}")
    pekan_kortti.syo_edullisesti()
    pekan_kortti.syo_edullisesti()
    matin_kortti.lataa_rahaa(50)
    print(f"Pekka: {pekan_kortti}")
    print(f"Matti: {matin_kortti}")