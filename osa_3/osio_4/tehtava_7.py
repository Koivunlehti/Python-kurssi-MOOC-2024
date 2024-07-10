def nelio(merkkijono, koko):
    laskuri = 0
    index = 0
    while laskuri < koko:
        laskuri_2 = 0
        while laskuri_2 < koko:
            print(merkkijono[index], end="")
            laskuri_2 += 1
            index += 1
            if index >= len(merkkijono):
                index = 0
        print()
        laskuri += 1

if __name__ == "__main__":
    nelio("ab", 3)
    print()
    nelio("aybabtu", 5)