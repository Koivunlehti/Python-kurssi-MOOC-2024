def tallenna_tiedostoon(sanapari: tuple):
    with open("osa_6/osio_2/sanakirja.txt","a",encoding="UTF-8") as tiedosto:
        tiedosto.write(f"{sanapari[0]}:{sanapari[1]}\n")

def lue_tiedostosta() -> dict:
    sanat = {}
    with open("osa_6/osio_2/sanakirja.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            rivi = rivi.split(":")
            sanat[rivi[0]] = rivi[1]
    return sanat

def hae_sana(sanat:dict, hakusana: str):
    for sana_suomi, sana_englanti in sanat.items():
        if sana_suomi.find(hakusana) != -1 or sana_englanti.find(hakusana) != -1:
            print(f"{sana_suomi} - {sana_englanti}")

def main():
    sanat = lue_tiedostosta()
    while True:
        print("1 - Lisää sana, 2 - Hae sanaa, 3 - poistu")
        valinta = input("Valinta: ")

        if valinta == "1":
            sana1 = input("Anna sana suomeksi: ")
            sana2 = input("Anna sana englanniksi: ")
            tallenna_tiedostoon((sana1, sana2))
            sanat = lue_tiedostosta()
            print("Sanapari lisätty")
            
        elif valinta == "2":
            hakusana = input("Anna sana: ")
            hae_sana(sanat, hakusana)

        elif valinta == "3":
            print("Moi!")
            break

main()