def laske_alkiot(matriisi:list, alkio:int):
    laskuri = 0
    for rivi in matriisi:
        for arvo in rivi:
            if arvo == alkio:
                laskuri += 1
    return laskuri

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))