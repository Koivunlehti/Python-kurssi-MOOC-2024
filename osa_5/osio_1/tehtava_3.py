def kumpi_voitti(pelilauta:list):
    pelaaja_1 = 0
    pelaaja_2 = 0
    
    for i in range(len(pelilauta)):
        for j in range(len(pelilauta[i])):
            if pelilauta[i][j] == 1:
                pelaaja_1 += 1
            elif pelilauta[i][j] == 2:
                pelaaja_2 += 1
    
    if pelaaja_1 > pelaaja_2:
        return 1
    elif pelaaja_2 > pelaaja_1:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    pelilauta = [[0,1,2,1,0,2],
                 [2,1,0,2,1,1],
                 [2,0,1,2,2,0],
                 [1,1,0,2,1,0],
                 [2,1,0,0,0,1],
                 [2,0,0,2,2,0]]
    print(kumpi_voitti(pelilauta))
