def lyhin(lista):
    lyhin = lista[0]
    for sana in lista:
        if len(sana) < len(lyhin):
            lyhin = sana
    return lyhin

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = lyhin(lista)
    print(tulos)

    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

    tulos = lyhin(lista)
    print(tulos)