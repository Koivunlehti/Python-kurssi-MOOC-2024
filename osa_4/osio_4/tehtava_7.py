def parilliset(lista):
    parilliset_lista = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset_lista.append(luku)
    return parilliset_lista

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)