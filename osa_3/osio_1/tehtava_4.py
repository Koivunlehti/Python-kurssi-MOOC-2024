limit = int(input("Mihin asti: "))
counter = 1
result = 1

while result <= limit:
    print(result)
    result = 2 ** counter
    counter += 1
