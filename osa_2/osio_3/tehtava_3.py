points = int(input("Anna pisteet [0-100]: "))

result = ""

if points < 0 or points > 100:
    result = "mahdotonta!"
elif points >= 0 and points <= 49:
    result = "hylätty"
elif points >= 50 and points <= 59:
    result = "1"
elif points >= 60 and points <= 69:
    result = "2"
elif points >= 70 and points <= 79:
    result = "3"
elif points >= 80 and points <= 89:
    result = "4"
elif points >= 90 and points <= 100:
    result = "5"

print(f"Arvosana {result}")