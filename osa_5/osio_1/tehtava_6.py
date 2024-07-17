def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    for numero in range(1, len(sudoku) + 1):
        loytyi = 0
        for i in range(rivi_nro, rivi_nro + 3):
            for j in range(sarake_nro, sarake_nro + 3):
                if j <= len(sudoku) or i <= len(sudoku):
                    if sudoku[i][j] == numero:
                        loytyi += 1
        
        if loytyi > 1:
            return False
    
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(nelio_oikein(sudoku, 0, 0))
    print(nelio_oikein(sudoku, 1, 2))