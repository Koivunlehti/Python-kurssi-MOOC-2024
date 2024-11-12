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

    def __add__(self, lisaa:int) -> 'Paivays':
        paiva = self.paiva
        kuukausi = self.kuukausi
        vuosi = self.vuosi
        
        for i in range(lisaa):
            paiva += 1
            if paiva > 30:
                kuukausi += 1
                paiva = 1
                if kuukausi > 12:
                    vuosi += 1
                    kuukausi = 1
        
        return Paivays(paiva, kuukausi, vuosi)

    def __sub__(self, toinen:'Paivays') -> 'Paivays':
        paivat_1 = self.vuosi * 360 + (self.kuukausi - 1) * 30 + self.paiva
        paivat_2 = toinen.vuosi * 360 + (toinen.kuukausi - 1) * 30 + toinen.paiva
        paivien_maara = paivat_1 - paivat_2
        return paivien_maara if paivien_maara > 0 else paivien_maara * -1

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)