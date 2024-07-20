def lue_hedelmat():
    with open("osa_6/osio_1/hedelmat.csv") as tiedosto:
        hedelmat = {}
        for rivi in tiedosto:
            tiedot = rivi.replace("\n","").split(";")
            hedelmat[tiedot[0]] = float(tiedot[1])
        return hedelmat

if __name__ == "__main__":
    print(lue_hedelmat())