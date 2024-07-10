def shakkilauta(koko):
    x = 0
    alku = 1

    while x < koko:
        y = 0
        while y < koko:
            print(alku, end="")
            if alku == 1:
                alku = 0
            else:
                alku = 1
            y += 1
        print()
        if koko % 2 == 0:
            if alku == 1:
                alku = 0
            else:
                alku = 1
        x += 1 

if __name__ == "__main__":
    shakkilauta(3)
    print()
    shakkilauta(6)