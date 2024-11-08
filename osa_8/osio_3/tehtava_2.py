
class Muistilista:

    otsikko:str
    merkinnat:list

    def __init__(self, otsikko:str, merkinnat:str):
        self.otsikko = otsikko
        self.merkinnat = merkinnat

class Asiakas:

    tunniste:str
    saldo:float
    alennusprosentti:int

    def __init__(self,tunniste:str, saldo:float, alennusprosentti:int):
        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti

class Kaapeli:

    malli:str
    pituus:float
    maksiminopeus:int
    kaksisuuntainen:bool

    def __init__(self, malli:str, pituus:float, maksiminopeus:int, kaksisuuntainen:bool):
        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen