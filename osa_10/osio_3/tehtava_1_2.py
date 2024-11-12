class Raha:
    def __init__(self,eurot:int, sentit:int) -> None:
        self.eurot = eurot
        self.sentit = sentit
    
    def __str__(self) -> str:
        return f"{self.eurot}.{'0' if self.sentit < 10 else ''}{self.sentit} eur"

    def __eq__(self, toinen: 'Raha') -> bool:
        return True if self.eurot == toinen.eurot and self.sentit == toinen.sentit else False

if __name__ == "__main__":
    e1 = Raha(4, 10)
    e2 = Raha(2, 5)
    e3 = Raha(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)