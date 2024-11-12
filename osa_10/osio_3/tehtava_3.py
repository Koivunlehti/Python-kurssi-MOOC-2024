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

    def __iter__(self):
        self.laskuri = 0
        return self
    
    def __next__(self):
        if self.laskuri < len(self.ostokset):
            ostos:dict = self.ostokset[self.laskuri]
            self.laskuri += 1
            for tuote, tuote_maara in ostos.items():
                nimi = tuote
                maara = tuote_maara
            return (nimi,maara)
        else:
            raise StopIteration


if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    for tuote in lista:
        print(f"{tuote[0]}: {tuote[1]} kpl")