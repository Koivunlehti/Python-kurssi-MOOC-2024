def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)

def nelio(koko, merkki):
    laskuri = 0
    while laskuri < koko:
        viiva(koko, merkki)
        laskuri += 1

if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")