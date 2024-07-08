limit = int(input("Mihin asti: "))
multiplier = int(input("Mikä kerroin: "))
counter = 1
result = 1

while result <= limit:
    print(result)
    result = multiplier ** counter
    counter += 1