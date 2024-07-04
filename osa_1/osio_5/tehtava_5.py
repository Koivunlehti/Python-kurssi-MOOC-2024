number_1 = int(input("Anna luku 1: "))
number_2 = int(input("Anna luku 2: "))
Command = input("Komento: ")

if Command == "summa":
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
if Command == "erotus":
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
if Command == "tulo":
    print(f"{number_1} * {number_2} = {number_1 * number_2}")