def kertomat(n: int):
    sanakirja = {}
    for i in range(1, n + 1):
        luvun_kertoma = i
        for j in range(i-1, 0, -1):
            luvun_kertoma *= j
        sanakirja[i] = luvun_kertoma
    return sanakirja

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])