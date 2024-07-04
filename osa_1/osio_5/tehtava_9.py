print("Kerro huominen sääennuste:")
temperature = int(input("Lämpötila: "))
raining = input("Sataako (kyllä/ei): ")

print("Pue housut ja t-paita")
if temperature < 20:
    print("Ota myös pitkähihainen paita")
    if temperature < 10:
        print("Pue päälle takki")
        if temperature < 5:
            print("Suosittelen lämmintä takkia")
            print("Kannattaa ottaa myös hanskat")

if raining == "kyllä":
    print("Muista sateenvarjo!")