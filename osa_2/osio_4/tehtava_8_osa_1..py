print("Syötä kokonaislukuja, 0 lopettaa:")

counter = 0

while True:
    number = int(input("Luku: "))
    if number == 0:
        break
    counter += 1

print("Lukuja yhteensä", counter)