def viiva(leveys, merkkijono):
    if merkkijono == "":
        print("*" * leveys)
    else:
        print(merkkijono[0] * leveys)

def kolmio(koko, merkki):
    laskuri = 1
    while laskuri <= koko:
        viiva(laskuri, merkki)
        laskuri += 1

def suorakulmio(korkeus,leveys, merkki):
    laskuri = 0
    while laskuri < korkeus:
        viiva(leveys, merkki)
        laskuri += 1

def kuvio(kolmio_koko, kolmio_merkki, suorakulmio_koko, suorakulmio_merkki):
    kolmio(kolmio_koko, kolmio_merkki)
    suorakulmio(suorakulmio_koko, kolmio_koko, suorakulmio_merkki)

if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")