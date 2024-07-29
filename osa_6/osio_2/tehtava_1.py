def kirjoita_tiedostoon(tiedosto: str, nimi: str):
    with open("osa_6/osio_2/" + tiedosto,"w", encoding="UTF-8") as tiedosto:
        tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")

def main():
    nimi = input("Kenelle teos omistetaan: ")
    tiedosto = input("Mihin kirjoitetaan: ")
    kirjoita_tiedostoon(tiedosto, nimi)

main()