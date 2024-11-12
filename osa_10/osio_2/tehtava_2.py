class Taikajuoma:
    def __init__(self, nimi:str) -> None:
        self._nimi = nimi
        self._ainekset:dict = {}

    def lisaa_aines(self, ainesosa:str, maara:float) -> None:
        self._ainekset[ainesosa] = maara

    def tulosta_resepti(self) -> None:
        print(self._nimi)
        for aines, maara in self._ainekset.items():
            print(f"{aines} {maara} grammaa")

class SalainenTaikajuoma(Taikajuoma):
    def __init__(self, nimi:str, salasana:str) -> None:
        super().__init__(nimi)
        self._salasana = salasana

    def __tarkista_salasana(self,salasana):
        if self._salasana == salasana:
            return True
        else:
            raise ValueError("Väärä salasana!")

    def lisaa_aines(self, ainesosa: str, maara: float, salasana:str) -> None:
        if self.__tarkista_salasana(salasana):
            super().lisaa_aines(ainesosa,maara)

    def tulosta_resepti(self, salasana:str) -> None:
        if self.__tarkista_salasana(salasana):
            return super().tulosta_resepti()

if __name__ == "__main__":
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "hokkuspokkus")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
    kutistus.tulosta_resepti("hokkuspokkus")

    kutistus.tulosta_resepti("pokkushokkus") # VÄÄRÄ SALASANA!