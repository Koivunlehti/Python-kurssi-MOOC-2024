class Auto:
    def __init__(self) -> None:
        self.__polttoaine = 0
        self.__ajettu = 0

    def tankkaa(self) -> None:
        self.__polttoaine = 60

    def aja(self, km:int) -> None:
        if km <= self.__polttoaine:
            self.__ajettu += km
            self.__polttoaine -= km
        else:
            self.__ajettu += self.__polttoaine
            self.__polttoaine = 0

    def __str__(self) -> str:
        return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__polttoaine} litraa"

if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)