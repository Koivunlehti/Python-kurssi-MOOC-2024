class Kauppalista:

    def __init__(self, ostokset:list = []):
        self.ostokset = ostokset

    def tuotteita(self):
        return len(self.ostokset)

    def tuote(self,index):
        for avain in self.ostokset[index - 1]:
            return avain
    
    def maara(self,index):
        for avain,arvo in self.ostokset[index - 1].items():
            return arvo

    def lisaa(self, tuote:str, maara:int):
        self.ostokset.append( { tuote : maara } )



def tuotteita_yhteensa(lista:Kauppalista) -> int:
    yhteensa = 0
    for i in range(1, lista.tuotteita() + 1):
        yhteensa += lista.maara(i)
    return yhteensa

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    print(tuotteita_yhteensa(lista))