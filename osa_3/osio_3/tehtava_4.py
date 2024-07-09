number = int(input("Anna luku: "))

counter = 1
add = 1
while counter <= number:
    if counter + add > number:
        print(number)
    else:
        print(counter + add)
    add *= -1
    counter += 1