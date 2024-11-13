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
        return f"{self.__nimi}, {self.__numerot if len(self.__numerot) > 0 else 'ei numeroa'}, {self.__osoite if self.__osoite != '' else 'ei osoitetta'}"
        

class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi:str, osoite:str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        
        self.__henkilot[nimi].lisaa_osoite(osoite)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None

        return self.__henkilot[nimi].numerot()
    
    def hae_osoite(self, nimi:str):
        if not nimi in self.__henkilot:
            return None
        
        return self.__henkilot[nimi].osoite()

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
        print("4 osoitteen lisäys")
        
    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        osoite = self.__luettelo.hae_osoite(nimi)
        if numerot == None or len(numerot) == 0:
            print("numero ei tiedossa")
        else:
            for numero in numerot:
                print(numero)
        
        if osoite == None:
            print("osoite ei tiedossa")
        else:
            print(osoite)

    def haku_numerolla(self):
        numero = input("numero: ")
        nimi = self.__luettelo.hae_nimi(numero)
        osoite = self.__luettelo.hae_osoite(nimi)
        if nimi == None:
            print("tuntematon numero")
        else:
            print(nimi)
            if osoite == None or osoite == "":
                print("osoite ei tiedossa")
            else:
                print(osoite)

    def lisaa_osoite(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

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
            elif komento == "4":
                self.lisaa_osoite()
            else:
                self.ohje()

if __name__ == "__main__":
    sovellus = PuhelinluetteloSovellus()
    sovellus.suorita()