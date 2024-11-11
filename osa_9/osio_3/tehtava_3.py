class Havaintoasema:
    def __init__(self, nimi:str) -> None:
        self.__nimi = nimi
        self.__havainnot:list[str] = []
    
    def lisaa_havainto(self, havainto:str) -> None:
        self.__havainnot.append(havainto)

    def viimeisin_havainto(self) -> str:
        return self.__havainnot[len(self.__havainnot) -1]
    
    def havaintojen_maara(self) -> int:
        return len(self.__havainnot)
    
    def __str__(self) -> str:
        return f"{self.__nimi}, {self.havaintojen_maara()} havaintoa"

if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)