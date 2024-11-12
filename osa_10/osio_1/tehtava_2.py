class Tietokonepeli:
    def __init__(self, nimi:str, kehittaja:str, vuosi:int) -> None:
        self.nimi = nimi
        self.kehittaja = kehittaja
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self) -> None:
        self.pelit:list[Tietokonepeli] = []
    
    def lisaa_peli(self, peli:Tietokonepeli):
        self.pelit.append(peli)

    def anna_pelit(self) -> list[Tietokonepeli]:
        return self.pelit

class Pelimuseo(Pelivarasto):
    def __init__(self) -> None:
        super().__init__()
    
    def anna_pelit(self) -> list[Tietokonepeli]:
        pelit:list[Tietokonepeli] = []
        for peli in self.pelit:
            if peli.vuosi < 1990:
                pelit.append(peli)
        return pelit


if __name__ == "__main__":
    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("Pacman", "Namco", 1980))
    museo.lisaa_peli(Tietokonepeli("GTA 2", "Rockstar", 1999))
    museo.lisaa_peli(Tietokonepeli("Bubble Bobble", "Taito", 1986))
    for peli in museo.anna_pelit():
        print(peli.nimi)