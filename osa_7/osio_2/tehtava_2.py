from string import ascii_lowercase
from random import randint

def luo_salasana(merkkimaara: int):
    salasana = ""
    for i in range(merkkimaara):
        salasana += ascii_lowercase[randint(0,len(ascii_lowercase)-1)]
    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))