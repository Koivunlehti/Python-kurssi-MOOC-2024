def kaanna(sanakirja: dict):
    avaimet = []
    arvot = []
    
    for avain, arvo in sanakirja.items():
        avaimet.append(avain)
        arvot.append(arvo)

    sanakirja.clear()

    for i in range(len(avaimet)):
        sanakirja[arvot[i]] = avaimet[i]

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)