print("Syötä kokonaislukuja, 0 lopettaa:")

counter = 0
sum = 0

while True:
    number = int(input("Luku: "))
    if number == 0:
        break
    counter += 1
    sum += number

print("Lukuja yhteensä", counter)
print("Lukuja summa", sum)