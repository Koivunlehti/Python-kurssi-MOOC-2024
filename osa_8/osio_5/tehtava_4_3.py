class Sarja:
    def __init__(self, nimi:str, kaudet:int, genret:list) -> None:
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvosanat = []
        self.arvosanat_keskiarvo = 0.0
    
    def __str__(self) -> str:
        tuloste = f"{self.nimi} ({self.kaudet} esityskautta)\n"
        tuloste += f"genret: {', '.join(self.genret)}\n"
        if len(self.arvosanat) > 0:
            tuloste += f"arvosteluja {len(self.arvosanat)}, "
            tuloste += f"keskiarvo {self.arvosanat_keskiarvo:.1f}" 
        else:
            tuloste += "ei arvosteluja"
        return tuloste

    def arvostele(self, arvosana:int):
        if arvosana >= 0 and arvosana <= 5:
            self.arvosanat.append(arvosana)
            self.arvosanat_keskiarvo = sum(self.arvosanat) / len(self.arvosanat)

def arvosana_vahintaan(arvosana:float, sarjat:list[Sarja]):
    loydetyt = []
    for sarja in sarjat:
        if sarja.arvosanat_keskiarvo >= arvosana:
            loydetyt.append(sarja)
    return loydetyt

def sisaltaa_genren(genre:str, sarjat:list[Sarja]):
    loydetyt = []
    for sarja in sarjat:
        if genre in sarja.genret:
            loydetyt.append(sarja)
    return loydetyt


if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)
    print()
    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)