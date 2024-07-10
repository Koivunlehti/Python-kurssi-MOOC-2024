def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)


if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")