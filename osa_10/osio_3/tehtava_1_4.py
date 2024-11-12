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
    
    def __add__(self,toinen:'Raha') -> 'Raha':
        eurot = self.eurot + toinen.eurot
        sentit = self.sentit + toinen.sentit
        if sentit >= 100:
            eurot += 1
            sentit -= 100
        return Raha(eurot,sentit)

    def __sub__(self,toinen:'Raha') -> 'Raha':
        eurot = self.eurot - toinen.eurot
        sentit = self.sentit - toinen.sentit
        if sentit < 0:
            eurot -= 1
            sentit += 100
        if eurot < 0:
            raise ValueError("negatiivinen tulos ei sallittu")
        return Raha(eurot,sentit)

if __name__ == "__main__":
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1