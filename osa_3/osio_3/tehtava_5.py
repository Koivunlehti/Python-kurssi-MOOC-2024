number = int(input("Anna luku: "))

counter = 1
counter_2 = number

while True:
    if counter >= counter_2 and number % 2 == 0:
        break
    print(counter)
    if counter >= counter_2:
        break
    print(counter_2)
    counter += 1
    counter_2 -= 1