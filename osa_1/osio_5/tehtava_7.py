hourly_pay = float(input("Tuntipalkka: "))
working_hours = int(input("Työtunnit: "))
week_day = input("Viikonpäivä: ")

if week_day == "sunnuntai":
    hourly_pay *= 2
print(f"Palkka {hourly_pay * working_hours} euroa")