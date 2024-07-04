temperature = int(input("Anna lämpötila (F): "))

celsius = (temperature - 32) / 1.8

print(f"{temperature} fahrenheit-astetta on {celsius} celsius-astetta")

if celsius < 0:
    print("Paleltaa!")