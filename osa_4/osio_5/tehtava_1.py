def muotoile(lista):
    uusi_lista = []
    for luku in lista:
        uusi_lista.append(f"{luku:.2f}")
    return uusi_lista

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)