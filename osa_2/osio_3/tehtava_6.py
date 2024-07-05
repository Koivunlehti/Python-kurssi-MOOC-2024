letter_1 = input("Anna 1. kirjain: ")
letter_2 = input("Anna 2. kirjain: ")
letter_3 = input("Anna 3. kirjain: ")

if letter_1 < letter_2 < letter_3 or letter_3 < letter_2 < letter_1:
    print(f"Keskimmäinen kirjain on {letter_2}")
elif letter_2 < letter_1 < letter_3 or letter_3 < letter_1 < letter_2:
    print(f"Keskimmäinen kirjain on {letter_1}")
else: 
     print(f"Keskimmäinen kirjain on {letter_3}")