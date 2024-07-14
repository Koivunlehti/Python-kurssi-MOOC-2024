def uniikit(lista):
    uusi_lista = []
    for luku in lista:
        if luku not in uusi_lista:
            uusi_lista.append(luku)
    return sorted(uusi_lista)

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))