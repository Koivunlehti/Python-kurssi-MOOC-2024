year = int(input("Anna vuosi: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Vuosi on karkausvuosi.")
        else:
            print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")