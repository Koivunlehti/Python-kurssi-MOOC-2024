def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)

def risulaatikko(korkeus):
    laskuri = 0
    while laskuri < korkeus:
        viiva(10,"#")
        laskuri += 1


if __name__ == "__main__":
    risulaatikko(5)
    print()
    risulaatikko(2)