print("Henkilö 1:")
name_1 = input("Nimi: ")
age_1 = int(input("ikä: "))
print("Henkilö 2:")
name_2 = input("Nimi: ")
age_2 = int(input("ikä: "))

if age_1 > age_2:
    print(f"Vanhempi on {name_1}")
elif age_1 < age_2:
    print(f"Vanhempi on {name_2}")
else:
    print(f"{name_1} ja {name_2} ovat yhtä vanhoja")