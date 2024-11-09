class Sarja:
    def __init__(self, nimi:str, kaudet:int, genret:list) -> None:
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvosanat = []
    
    def __str__(self) -> str:
        tuloste = f"{self.nimi} ({self.kaudet} esityskautta)\n"
        tuloste += f"genret: {', '.join(self.genret)}\n"
        if len(self.arvosanat) > 0:
            tuloste += f"arvosteluja {len(self.arvosanat)}, "
            tuloste += f"keskiarvo {sum(self.arvosanat) / len(self.arvosanat):.1f}" 
        else:
            tuloste += "ei arvosteluja"
        return tuloste

    def arvostele(self, arvosana:int):
        if arvosana >= 0 and arvosana <= 5:
            self.arvosanat.append(arvosana)

if __name__ == "__main__":
    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.arvostele(4)
    dexter.arvostele(5)
    dexter.arvostele(5)
    dexter.arvostele(3)
    dexter.arvostele(0)
    print(dexter)