luvut = []
maara = int(input("Kuinka monta lukua: "))

laskuri = 1
while laskuri <= maara:
    luvut.append(int(input(f"Anna luku {laskuri}: ")))
    laskuri += 1
print(luvut)