money = float(input("Lahjan suuruus? "))

if money >= 5000 and money < 25000:
    print(f"Vero: {100 + (money - 5000) * 0.08}")
elif money >= 25000 and money < 55000:
    print(f"Vero: {1700 + (money - 25000) * 0.10}")
elif money >= 55000 and money < 200000:
    print(f"Vero: {4700 + (money - 55000) * 0.12}")
elif money >= 200000 and money < 1000000:
    print(f"Vero: {22100 + (money - 200000) * 0.15}")
elif money >= 1000000:
    print(f"Vero: {142100 + (money - 1000000) * 0.17}")
else:
    print("Ei veroa!")
