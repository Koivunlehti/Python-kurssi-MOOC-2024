def tulosta(sudoku: list):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_ ", end="")
            else:
                print(str(sudoku[i][j]) + " ", end="")
            if (j + 1) % 3 == 0:
                print(" ",end="")
        print()
        if (i + 1) % 3 == 0:
            print()

def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int) -> list:
    uusi_sudoku = []
    laskuri = 0 
    for rivi in sudoku:
        uusi_sudoku.append([])
        for sarake in rivi:
            uusi_sudoku[laskuri].append(sarake)
        laskuri += 1
    uusi_sudoku[rivi_nro][sarake_nro] = luku
    return uusi_sudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)