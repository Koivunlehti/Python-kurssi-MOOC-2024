word = input("merkkijono: ")
chars = input("Anna osajono: ")

counter = 0
index = 0

while True:
    index = word.find(chars,index)
    if index != -1:
        counter += 1
        if counter == 2:
           break
        index += len(chars)
    else:
        break
if counter >= 2:
    print(f"Osajonon toinen esiintymä on kohdassa {index}.")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")



