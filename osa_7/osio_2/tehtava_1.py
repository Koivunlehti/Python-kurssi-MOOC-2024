from random import shuffle

def lottonumerot(maara: int, alaraja: int, ylaraja: int) -> list:
    numerot = list(range(alaraja, ylaraja + 1))
    shuffle(numerot)
    numerot = numerot[:7]
    numerot.sort()
    return numerot

if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)