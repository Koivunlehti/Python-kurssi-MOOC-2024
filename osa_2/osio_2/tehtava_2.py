number_1 = int(input("Anna ensimäinen luku: "))
number_2 = int(input("Anna toinen luku: "))

if number_1 > number_2:
    print(f"Suurempi luku {number_1}")
elif number_1 < number_2:
    print(f"Suurempi luku {number_2}")
else:
    print("Luvut ovat yhtä suuret!")