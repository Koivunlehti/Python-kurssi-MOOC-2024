def lisaa_numero(puhelinluettelo: dict):
    nimi = input("nimi: ")
    numero = input("numero: ")
    if nimi not in puhelinluettelo:
        puhelinluettelo[nimi] = [numero]
    else:
        puhelinluettelo[nimi].append(numero)

def hae_tieto(puhelinluettelo: dict):
    nimi = input("nimi: ")
    if nimi in puhelinluettelo:
        for numero in puhelinluettelo[nimi]:
            print(numero)
    else:
        print("ei numeroa")

def main():
    puhelinluettelo = {}
    while True:
        komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if komento == "1":
            hae_tieto(puhelinluettelo)
        if komento == "2":
            lisaa_numero(puhelinluettelo)
            print("ok!")
        if komento == "3":
            print("lopetetaan...")
            break

main()