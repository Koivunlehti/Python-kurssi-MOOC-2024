class Kaupunki:
    postinumerot = {"Helsinki":"00100", 
                    "Turku":"20100", 
                    "Tampere":"33100", 
                    "Jyväskylä":"40100",
                    "Oulu":"90100"}

    def __init__(self, nimi:str) -> None:
        self.nimi = nimi

if __name__ == "__main__":
    k1 = Kaupunki("Turku")
    k2 = Kaupunki("Jyväskylä")
    k3 = Kaupunki("Oulu")

    print(Kaupunki.postinumerot[k1.nimi])
    print(Kaupunki.postinumerot[k2.nimi])
    print(Kaupunki.postinumerot[k3.nimi])