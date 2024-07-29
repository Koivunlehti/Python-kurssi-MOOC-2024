def lue_tiedosto() -> list:
    merkinnat = []
    with open("osa_6/osio_2/paivakirja.txt", encoding="UTF-8") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            merkinnat.append(rivi)

    return merkinnat

def tallenna_tiedostoon(tieto: list):
    with open("osa_6/osio_2/paivakirja.txt","a",encoding="UTF-8") as tiedosto:
        tiedosto.writelines(tieto + "\n")
    print("Päiväkirja tallennettu")

def main():
    merkinnat = lue_tiedosto()
    while True:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        valinta = input("Valinta: ")
        if valinta == "0":
            break
        elif valinta == "1":
            merkinta = input("Anna merkintä: ")
            merkinnat.append(merkinta)
            tallenna_tiedostoon(merkinta)
            print()
        elif valinta == "2":
            print("Merkinnät:")
            for merkinta in merkinnat:
                print(merkinta)
    print("Heippa!")
main()