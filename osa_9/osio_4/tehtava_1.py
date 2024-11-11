class Pankkitili:
    def __init__(self,tilinomistaja:str, tilinumero:str, saldo:float) -> None:
        self.__tilinomistaja = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo

    def talleta(self, summa:float):
        self.__saldo += summa
        self.__palvelumaksu()

    def nosta(self, summa: float):
        self.__saldo -= summa
        self.__palvelumaksu()
    
    def __palvelumaksu(self):
        self.__saldo = 99 / 100 * self.__saldo

    def __str__(self) -> str:
        return f"Tili: {self.__tilinumero}, Omistaja: {self.__tilinomistaja}, Saldo: {self.__saldo}€"

if __name__ == "__main__":
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)