def tallenna_henkilo(henkilo: tuple):
    with open("osa_6/osio_2/henkilot.csv", "a") as tiedosto:
        tiedosto.write(f"{henkilo[0]};{henkilo[1]};{henkilo[2]}\n")

if __name__ == "__main__":
    tallenna_henkilo(("Essi Esimerkki", 32, 168.5))