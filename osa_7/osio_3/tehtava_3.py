from datetime import datetime, timedelta

def tallenna(tiedostonimi: str,alku_pvm: datetime, paivien_maara: int, minuutit_yht: int, kaikki_minuutit: list):
    with open("osa_7/osio_3/" + tiedostonimi,"w") as tiedosto:
        tiedosto.write(f"Ajanjakso: {alku_pvm.strftime('%d.%m.%Y')}-{(alku_pvm + timedelta(paivien_maara - 1)).strftime('%d.%m.%Y')}\n")
        tiedosto.write(f"Yht. minuutteja: {minuutit_yht}\n")
        tiedosto.write(f"Keskim. minuutteja: {780 / len(kaikki_minuutit)}\n")
        for rivi in kaikki_minuutit:
            tiedosto.write(rivi + "\n")

    print (f"Tiedot tallennettu tiedostoon {tiedostonimi}")

def main():
    tiedosto = input("Tiedosto: ")
    alku = input("Aloituspäivä: ")
    alku = alku.split(".")
    aloituspaiva = datetime(int(alku[2]),int(alku[1]),int(alku[0]))
    paivien_maara = int(input("Montako päivää: "))

    print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")
    
    paivays = aloituspaiva
    kaikki_minuutit = []
    minuutit_yht = 0
    for i in range(paivien_maara):
        minuutit = input(f"Ruutuaika {paivays.strftime('%d.%m.%Y')}: ")
        minuutit_yht += int(minuutit.split(" ")[0]) + int(minuutit.split(" ")[1]) + int(minuutit.split(" ")[2])
        minuutit = minuutit.replace(" ", "/")
        kaikki_minuutit.append(f"{paivays.day}.{paivays.month}.{paivays.year}: {minuutit}")
        
        paivays += timedelta(1)
    
    tallenna(tiedosto, aloituspaiva, paivien_maara, minuutit_yht, kaikki_minuutit)

main()