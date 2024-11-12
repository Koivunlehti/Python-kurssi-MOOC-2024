class Raha:
    def __init__(self,eurot:int, sentit:int) -> None:
        self.eurot = eurot
        self.sentit = sentit
    
    def __str__(self) -> str:
        return f"{self.eurot}.{'0' if self.sentit < 10 else ''}{self.sentit} eur"

    def __eq__(self, toinen: 'Raha') -> bool:
        return True if self.eurot == toinen.eurot and self.sentit == toinen.sentit else False

    def __gt__(self, toinen: 'Raha') -> bool:
        return True if self.eurot + self.sentit > toinen.eurot + toinen.sentit else False
    
    def __lt__(self, toinen: 'Raha') -> bool:
        return True if self.eurot + self.sentit < toinen.eurot + toinen.sentit else False
    
    def __ne__(self, toinen: 'Raha') -> bool:
        return False if self.eurot == toinen.eurot and self.sentit == toinen.sentit else True
    
if __name__ == "__main__":
    e1 = Raha(4, 10)
    e2 = Raha(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)