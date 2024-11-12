class Raha:
    def __init__(self,eurot:int, sentit:int) -> None:
        self.__eurot = eurot
        self.__sentit = sentit
    
    def __str__(self) -> str:
        return f"{self.__eurot}.{'0' if self.__sentit < 10 else ''}{self.__sentit} eur"

    def __eq__(self, toinen: 'Raha') -> bool:
        return True if self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit else False

    def __gt__(self, toinen: 'Raha') -> bool:
        return True if self.__eurot + self.__sentit > toinen.__eurot + toinen.__sentit else False
    
    def __lt__(self, toinen: 'Raha') -> bool:
        return True if self.__eurot + self.__sentit < toinen.__eurot + toinen.__sentit else False
    
    def __ne__(self, toinen: 'Raha') -> bool:
        return False if self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit else True
    
    def __add__(self,toinen:'Raha') -> 'Raha':
        eurot = self.__eurot + toinen.__eurot
        sentit = self.__sentit + toinen.__sentit
        if sentit >= 100:
            eurot += 1
            sentit -= 100
        return Raha(eurot,sentit)

    def __sub__(self,toinen:'Raha') -> 'Raha':
        eurot = self.__eurot - toinen.__eurot
        sentit = self.__sentit - toinen.__sentit
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

    print(e1)
    e1.eurot = 1000
    print(e1)