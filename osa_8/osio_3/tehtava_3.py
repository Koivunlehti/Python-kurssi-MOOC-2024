class Lemmikki:
    nimi:str
    laji:str
    syntymavuosi:int

    def __init__(self, nimi, laji, syntymavuosi) -> None:
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

def uusi_lemmikki(nimi:str, laji:str, syntymavuosi:int) -> Lemmikki:
    lemmikki = Lemmikki(nimi,laji,syntymavuosi)
    return lemmikki

if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)