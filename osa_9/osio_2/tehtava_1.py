class Lemmikki:
    def __init__(self, nimi:str, rotu:str) -> None:
        self.nimi = nimi
        self.rotu = rotu

class Henkilo:
    def __init__(self, nimi:str, lemmikki:Lemmikki) -> None:
        self.nimi = nimi
        self.lemmikki = lemmikki
    
    def __str__(self) -> str:
        return f"{self.nimi}, kaverina {self.lemmikki.nimi}, joka on {self.lemmikki.rotu}"

if __name__ == "__main__":
    hulda = Lemmikki("Hulda", "sekarotuinen koira")
    leevi = Henkilo("Leevi", hulda)

    print(leevi)