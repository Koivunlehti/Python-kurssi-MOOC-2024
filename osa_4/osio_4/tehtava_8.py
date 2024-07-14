def summa(lista_1, lista_2):
    summat = []
    for i in range(0,len(lista_1)):
        summat.append(lista_1[i] + lista_2[i])
    return summat

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))