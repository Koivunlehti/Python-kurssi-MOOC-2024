class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista:list):
        luku = lista[0]
        maara = lista.count(lista[0])
        for alkio in lista:
            if maara < lista.count(alkio):
                maara = lista.count(alkio)
                luku = alkio

        return luku

    @classmethod
    def tuplia(cls, lista:list):
        esiintymat = {}
        for alkio in lista:
            if alkio not in esiintymat:
                esiintymat[alkio] = 1
            else:
                esiintymat[alkio] += 1
                
        tuplien_maara = 0
        for avain, arvo in esiintymat.items():
            if arvo > 1:
                tuplien_maara += 1
        
        return tuplien_maara

if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))