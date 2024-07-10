def luvuista_suurin(luku_1, luku_2, luku_3):
    if luku_1 > luku_2 and luku_1 > luku_3:
        return luku_1
    elif luku_2 > luku_1 and luku_2 > luku_3:
        return luku_2
    else:
        return luku_3

if __name__ == "__main__":
    print(luvuista_suurin(3, 4, 1))
    print(luvuista_suurin(99, -4, 7))
    print(luvuista_suurin(0, 0, 0))