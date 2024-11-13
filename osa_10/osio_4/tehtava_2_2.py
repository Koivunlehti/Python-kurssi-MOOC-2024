class Henkilo:
    def __init__(self, nimi:str) -> None:
        self.__nimi = nimi
        self.__numerot:list[str] = []
        self.__osoite:str = ""
    
    def nimi(self) -> str:
        return self.__nimi

    def numerot(self) -> list[str]:
        return self.__numerot

    def osoite(self) -> None | str:
        if self.__osoite != "":
            return self.__osoite
        return None

    def lisaa_numero(self, numero:str):
        self.__numerot.append(numero)

    def lisaa_osoite(self, osoite:str):
        self.__osoite = osoite

    def __repr__(self) -> str:
        return f"{self.__nimi}, {self.__numerot}"
        

class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_numero(numero)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None

        return self.__henkilot[nimi].numerot()
    
    def hae_nimi(self, numero:str):
        for nimi, henkilo in self.__henkilot.items():
            for henkilon_numero in henkilo.numerot():
                if henkilon_numero == numero:
                    return nimi
        return None
    
    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisäys")
        print("2 haku")
        print("3 haku numeron perusteella")
        
    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print("numero ei tiedossa")
            return
        for numero in numerot:
            print(numero)

    def haku_numerolla(self):
        numero = input("numero: ")
        nimi = self.__luettelo.hae_nimi(numero)
        if nimi == None:
            print("tuntematon numero")
        else:
            print(nimi)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.haku_numerolla()
            else:
                self.ohje()

if __name__ == "__main__":
    sovellus = PuhelinluetteloSovellus()
    sovellus.suorita()