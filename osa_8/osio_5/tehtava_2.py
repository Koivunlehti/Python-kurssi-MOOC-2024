class Kello:
    def __init__(self, tunnit:int, minuutit:int, sekunnit:int) -> None:
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit

    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0
                self.tunnit += 1
                if self.tunnit == 24:
                    self.tunnit = 0

    def aseta(self,tunnit,minuutit):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0

    def __str__(self) -> str:
        tunnit = f"{'0' if self.tunnit < 10 else ''}{self.tunnit}"
        minuutit = f"{'0' if self.minuutit < 10 else ''}{self.minuutit}"
        sekunnit = f"{'0' if self.sekunnit < 10 else ''}{self.sekunnit}"
        return f"{tunnit}:{minuutit}:{sekunnit}"
    
if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)