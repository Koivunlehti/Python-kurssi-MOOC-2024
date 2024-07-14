def kaikki_vaarinpain(lista):
    uusi_lista = []
    for i in range(len(lista) - 1, -1, -1):
        uusi_lista.append(lista[i][::-1])
    return uusi_lista

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)