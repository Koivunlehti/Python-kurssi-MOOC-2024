
def pienin_keskiarvo(h1:dict, h2:dict, h3:dict) -> dict:
    henkilot = [h1,h2,h3]
    keskiarvot = []
    alin_keskiarvo_index = 0

    for henkilo in henkilot:
        keskiarvot.append([henkilo, (henkilo["tulos1"] + henkilo["tulos2"] + henkilo["tulos3"]) / 3])
    for i in range(len(keskiarvot)):
       if keskiarvot[i][1] < keskiarvot[alin_keskiarvo_index][1]:
           alin_keskiarvo_index = i

    return keskiarvot[alin_keskiarvo_index][0]

if __name__ == "__main__":

    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))