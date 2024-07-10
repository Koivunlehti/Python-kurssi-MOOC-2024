def samat(merkkijono, index_1, index_2):
    if index_1 >= len(merkkijono) or index_2 >= len(merkkijono):
        return False
    if merkkijono[index_1] == merkkijono[index_2]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(samat("koodari", 1, 2))
    print(samat("koodari", 0, 4))
    print(samat("koodari", 0, 10))