def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)

def risunelio(koko):
    laskuri = 0
    while laskuri < koko:
        viiva(koko,"#")
        laskuri += 1

if __name__ == "__main__":
    risunelio(5)
    print()
    risunelio(3)