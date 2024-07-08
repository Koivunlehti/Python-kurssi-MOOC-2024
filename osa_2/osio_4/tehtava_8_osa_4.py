print("Syötä kokonaislukuja, 0 lopettaa:")

counter = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Luku: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        break
    
    counter += 1
    sum += number

print("Lukuja yhteensä", counter)
print("Lukuja summa", sum)
print("Lukujen keskiarvo", sum / counter)
print("Positiivisia", positive)
print("Negatiivisia", negative)