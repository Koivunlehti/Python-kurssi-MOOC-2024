class Kurssi:
    def __init__(self, nimi:str, arvosana:int, opintopisteet:int) -> None:
        self.__nimi = nimi
        self.__arvosana = arvosana
        self.__opintopisteet = opintopisteet
    
    def nimi(self) -> str:
        return self.__nimi

    def arvosana(self) -> int:
        return self.__arvosana
    
    def opintopisteet(self) -> int:
        return self.__opintopisteet

    def muuta_arvosana(self, arvosana:int) -> None:
        if arvosana >= self.__arvosana:
            self.__arvosana = arvosana
    
    def muuta_opintopisteet(self, opintopisteet:int) -> None:
        self.__opintopisteet = opintopisteet

    def __str__(self) -> str:
        return f"{self.__nimi} ({self.__opintopisteet} op) arvosana {self.__arvosana}"

class Opintorekisteri:
    def __init__(self) -> None:
        self.__kurssit:dict= {}

    def lisaa_kurssi(self, nimi:str, arvosana:int, opintopisteet:int) -> None:
        if not nimi in self.__kurssit:
            self.__kurssit[nimi] = Kurssi(nimi, arvosana, opintopisteet)
        
        else:
            self.__kurssit[nimi].muuta_arvosana(arvosana)
            self.__kurssit[nimi].muuta_opintopisteet(opintopisteet)
    
    def hae_kurssi(self, nimi:str) -> None | Kurssi:
        if not nimi in self.__kurssit:
            return None
        
        return self.__kurssit[nimi]

    def __laske_opintopisteet(self) -> int:
        pisteet = 0
        for avain, kurssi in self.__kurssit.items():
            pisteet += kurssi.opintopisteet()
        return pisteet
    
    def __laske_keskiarvo(self) -> int:
        keskiarvo = 0
        for avain, kurssi in self.__kurssit.items():
            keskiarvo += kurssi.arvosana()
        keskiarvo = keskiarvo / len(self.__kurssit)
        return keskiarvo

    def __arvosanajakauma(self) -> str:
        jakauma = [0 ,0, 0, 0, 0]
        for avain, kurssi in self.__kurssit.items():
            if kurssi.arvosana() == 1:
                jakauma[0] += 1
            if kurssi.arvosana() == 2:
                jakauma[1] += 1
            if kurssi.arvosana() == 3:
                jakauma[2] += 1
            if kurssi.arvosana() == 4:
                jakauma[3] += 1
            if kurssi.arvosana() == 5:
                jakauma[4] += 1

        tuloste = "arvosanajakauma\n"
        for i in range(len(jakauma) - 1, -1, -1):
            tuloste += f"{i + 1}: {'x' * jakauma[i]}"
            tuloste += '\n' if i > 0 else ''
        return tuloste
    
    def __str__(self) -> str:
        tuloste = f"suorituksia {len(self.__kurssit)} kurssilta, yhteensä {self.__laske_opintopisteet()} opintopistettä\n"
        tuloste += f"keskiarvo {self.__laske_keskiarvo()}\n"
        tuloste += self.__arvosanajakauma()
        return tuloste

class OpintorekisteriSovellus:
    def __init__(self) -> None:
        self.__opintorekisteri = Opintorekisteri()

    def ohjeistus(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
        print()

    def lisaa_suoritus(self):
        nimi = input("kurssi: ")
        arvosana = int(input("arvosana: "))
        opintopisteet = int(input("opintopisteet: "))
        self.__opintorekisteri.lisaa_kurssi(nimi, arvosana, opintopisteet)

    def hae_suoritus(self):
        nimi = input("kurssi: ")
        suoritus = self.__opintorekisteri.hae_kurssi(nimi)

        if suoritus == None:
            print("ei suoritusta")
        else:
            print(suoritus)

    def tilastot(self):
        print(self.__opintorekisteri)

    def suorita(self):
        self.ohjeistus()
        while True:
            komento = input("komento: ")
            if komento == "1":
                self.lisaa_suoritus()
            elif komento == "2":
                self.hae_suoritus()
            elif komento == "3":
                self.tilastot()
            elif komento == "0":
                break
            else:
                print("virheellinen komento!")
            print()

if __name__ == "__main__":
    sovellus = OpintorekisteriSovellus()
    sovellus.suorita()