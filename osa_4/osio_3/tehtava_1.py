luvut = [1,2,3,4,5]

while True:
    index = int(input("Anna indeksi: "))
    if index == -1:
        break
    else:
        arvo = int(input("Anna arvo: "))
        luvut[index] = arvo
        print(luvut)