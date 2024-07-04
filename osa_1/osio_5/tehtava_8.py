points = int(input("Kuinka paljon pisteitä? "))

if points < 100:
    points += points / 100 * 10
else:
    points += points / 100 * 15

print(f"Pisteitä on nyt {points}")