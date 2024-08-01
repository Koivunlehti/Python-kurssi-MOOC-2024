from math import sqrt

def hypotenuusa(kateetti1: float, kateetti2: float) -> float:
    return sqrt(kateetti1 ** 2 + kateetti2 ** 2)

if __name__ == "__main__":
    print(hypotenuusa(3,4))
    print(hypotenuusa(5,12))
    print(hypotenuusa(1,1))