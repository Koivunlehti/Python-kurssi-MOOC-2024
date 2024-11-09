class Sarja:
    def __init__(self, nimi:str, kaudet:int, genret:list) -> None:
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
    
    def __str__(self) -> str:
        tuloste = f"{self.nimi} ({self.kaudet} esityskautta)\n"
        tuloste += f"genret: {', '.join(self.genret)}\n"
        tuloste += "ei arvosteluja"
        return tuloste

if __name__ == "__main__":
    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)