def rivien_summat(matriisi:list) -> list:
    for rivi in matriisi:
        rivi.append(sum(rivi))
    return matriisi

if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)