class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0
    
    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0

    def __str__(self) -> str:
        return f"{'0' if self.minuutit < 10 else ''}{self.minuutit}:{'0' if self.sekunnit < 10 else ''}{self.sekunnit}"

if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()