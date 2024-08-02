from random import shuffle

def heita(noppa: str) -> int:
    if noppa == "A":
        arvot = [3,6]
    if noppa == "B":
        arvot = [2,5]
    if noppa == "C":
        arvot = [1,4]
    
    shuffle(arvot)
    return arvot[0]

def pelaa(noppa1: str, noppa2: str, kertaa: int) -> tuple:
    noppa1_voitot = 0
    noppa2_voitot = 0
    tasapelit = 0
    for i in range(kertaa):
        noppa1_arvo = heita(noppa1)
        noppa2_arvo = heita(noppa2)

        if noppa1_arvo > noppa2_arvo:
            noppa1_voitot += 1
        elif noppa2_arvo > noppa1_arvo:
            noppa2_voitot += 1
        else:
            tasapelit += 1 
    return noppa1_voitot, noppa2_voitot, tasapelit

if __name__ == "__main__":
    for i in range(20):
        print(heita("A"), " ", end="")
    print()
    for i in range(20):
        print(heita("B"), " ", end="")
    print()
    for i in range(20):
        print(heita("C"), " ", end="")
    print()
    
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)