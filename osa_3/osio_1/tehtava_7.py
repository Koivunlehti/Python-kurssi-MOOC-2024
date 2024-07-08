limit = int(input("Mihin asti: "))

counter = 1
sum = 0
calculations = ""

while sum < limit:
    sum += counter
    calculations += str(counter)
    if sum < limit:
        calculations += " + "
    counter += 1

print(f"Laskettiin {calculations} = {sum}")