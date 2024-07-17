def rivi_oikein(sudoku: list, rivi_nro:int):
    for numero in range(1, len(sudoku[rivi_nro]) + 1):
        loytyi = 0
        for i in range(len(sudoku[rivi_nro])):
            if sudoku[rivi_nro][i] == numero:
                loytyi += 1
        
        if loytyi > 1:
            return False
    
    return True

def sarake_oikein(sudoku: list, sarake_nro:int):
    for numero in range(1, len(sudoku) + 1):
        loytyi = 0
        for i in range(len(sudoku)):
            if sudoku[i][sarake_nro] == numero:
                loytyi += 1
        
        if loytyi > 1:
            return False
    
    return True

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

def sudoku_oikein(sudoku:list):
    for i in range(len(sudoku)):
        if rivi_oikein(sudoku, i) == False:
            return False
        for j in range(len(sudoku[i])):
            if sarake_oikein(sudoku, j) == False:
                return False
    
    for i in range(0, len(sudoku), 3):
        for j in range(0, len(sudoku[i]), 3):
            if nelio_oikein(sudoku, i, j) == False:
                return False
    return True

if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))