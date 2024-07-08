from math import sqrt

while True:
    number = int(input("Syötä luku: "))
    if number > 0:
        print(sqrt(number))
    elif number < 0:
        print("Epäkelpo luku")
    else:
        print("Lopetetaan...")
        break