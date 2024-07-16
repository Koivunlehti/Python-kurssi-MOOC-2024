def pisin(lista):
    pisin_sana = lista[0]
    for sana in lista:
        if len(pisin_sana) < len(sana):
            pisin_sana = sana
    return pisin_sana

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
