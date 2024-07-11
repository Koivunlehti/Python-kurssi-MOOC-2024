lista = []
laskuri = 0
while True:
    sana = input("sana: ")
    if sana in lista:
        break
    else:
        lista.append(sana)
        laskuri += 1
print(f"Annoit {laskuri} eri sanaa")