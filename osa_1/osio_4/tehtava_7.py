lunches_per_week = int(input("Montako kertaa viikossa syöt Unicafessa? "))
lunch_price = float(input("Unicafe-lounaan hinta? "))
money_used_per_week = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

per_week = lunches_per_week * lunch_price + money_used_per_week
per_day = per_week / 7

print()
print("Kustannukset keskimäärin:")
print(f"Päivässä {per_day} euroa")
print(f"Viikossa {per_week} euroa")