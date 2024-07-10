def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)

def kolmio(koko):
    laskuri = 1
    while laskuri <= koko:
        viiva(laskuri, "#")
        laskuri += 1

if __name__ == "__main__":
    kolmio(6)
    print()
    kolmio(3)