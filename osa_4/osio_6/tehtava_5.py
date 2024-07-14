def pisin_naapurijono(lista):
    pisin = 1
    jono = 1
    for i in range(0,len(lista),1):
        if i + 1 < len(lista):
            if lista[i] - lista[i + 1] == 1 or lista[i] - lista[i + 1] == -1:
                jono += 1
            else:
                jono = 1
        if jono > pisin:
            pisin = jono
    return pisin

if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))