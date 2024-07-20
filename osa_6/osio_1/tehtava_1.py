def suurin():
    with open("osa_6/osio_1/luvut.txt") as tiedosto:
        suurin = int(tiedosto.readline())
        for rivi in tiedosto:
            if int(rivi) > suurin:
                suurin = int(rivi)
        
    return suurin

if __name__ == "__main__":
    print("Suurin luku:",suurin())