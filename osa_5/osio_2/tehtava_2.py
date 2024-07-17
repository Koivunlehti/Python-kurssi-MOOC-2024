def poista_pienin(luvut:list):
    pienin = luvut[0]
    for luku in luvut:
        if luku < pienin:
            pienin = luku
    luvut.remove(pienin)

if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)