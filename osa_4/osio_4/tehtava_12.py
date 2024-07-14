def pisimmat(lista):
    pisimmat_sanat = []
    for sana in lista:
        if len(pisimmat_sanat) > 0:
            if len(sana) > len(pisimmat_sanat[0]):
                pisimmat_sanat = []
                pisimmat_sanat.append(sana)
            elif len(sana) == len(pisimmat_sanat[0]):
                pisimmat_sanat.append(sana)
        else:
            pisimmat_sanat.append(sana)
    return pisimmat_sanat

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimmat(lista)
    print(tulos)

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos)