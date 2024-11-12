class Paivays:
    def __init__(self, paiva:int, kuukausi:int, vuosi:int) -> None:
        self.paiva = paiva
        self.kuukausi = kuukausi
        self.vuosi = vuosi

    def __str__(self) -> str:
        return f"{self.paiva}.{self.kuukausi}.{self.vuosi}"

    def __eq__(self, toinen: 'Paivays') -> bool:
        return True if self.paiva == toinen.paiva and self.kuukausi == toinen.kuukausi and self.vuosi == toinen.vuosi else False

    def __ne__(self, toinen: 'Paivays') -> bool:
        return not self == toinen

    def __gt__(self, toinen: 'Paivays') -> bool:
        if self.vuosi == toinen.vuosi:
            if self.kuukausi == toinen.kuukausi:
                if self.paiva == toinen.paiva:
                    return False
                elif self.paiva > toinen:
                    return True
                else:
                    return False
            elif self.kuukausi > toinen.kuukausi:
                return True
            else:
                return False
        elif self.vuosi > toinen.vuosi:
            return True
        else:
            return False 
    
    def __lt__(self, toinen: 'Paivays') -> bool:
        if self.vuosi == toinen.vuosi:
            if self.kuukausi == toinen.kuukausi:
                if self.paiva == toinen.paiva:
                    return False
                elif self.paiva < toinen:
                    return True
                else:
                    return False
            elif self.kuukausi < toinen.kuukausi:
                return True
            else:
                return False
        elif self.vuosi < toinen.vuosi:
            return True
        else:
            return False 

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(28, 12, 1985)
    p3 = Paivays(28, 12, 1985)

    print(p1)
    print(p2)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 == p3)
    print(p1 < p2)
    print(p1 > p2)