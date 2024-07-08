leap_year = int(input("Vuosi: "))
next_leap_year = leap_year + 1

while True:
    if next_leap_year % 4 == 0:
        if next_leap_year % 100 == 0:
            if next_leap_year % 400 == 0:
                break
        else:
            break
    next_leap_year += 1

print(f"Vuotta {leap_year} seuraava karkausvuosi on {next_leap_year}")