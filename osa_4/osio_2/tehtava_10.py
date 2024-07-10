def eka_sana(lause):
    return lause[0:lause.find(" ")]

def toka_sana(lause:str):
    alku = lause.find(" ") + 1
    loppu = lause.find(" ", alku)
    return lause[alku:loppu]

def vika_sana(lause):
    alku = 0
    index = 0
    while index < len(lause):
        if lause[index] == " ":
            alku = index
        index += 1
    return lause[alku + 1:len(lause)]

if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))
