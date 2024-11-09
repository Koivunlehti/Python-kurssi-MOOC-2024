class Maksukortti:
    def __init__(self, alkusaldo: float) -> None:
        self.saldo = alkusaldo

    def __str__(self) -> str:
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"
    
if __name__ == "__main__":
    kortti = Maksukortti(50)
    print(kortti)