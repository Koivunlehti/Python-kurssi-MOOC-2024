lista = []

while True:
    print(f"Lista on nyt {lista}")
    toiminto = input("(l)isää, (p)oista vai e(x)it: ")
    if toiminto.lower() == "x":
        break
    elif toiminto.lower() == "l":
        if len(lista) == 0:
            lista.append(1)
        else:
            lista.append(lista[len(lista) - 1] + 1)
    elif toiminto.lower() == "p":
        if len(lista) > 0:
            lista.pop(len(lista)-1)
print("Moi!")