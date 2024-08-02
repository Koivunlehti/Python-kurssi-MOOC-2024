from random import shuffle

def lue_tiedostosta():
    sanoja = []
    with open("osa_7/osio_2/sanat.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            if rivi not in sanoja:
                sanoja.append(rivi)
    return sanoja

def sanat(n: int, alku: str) -> list:
    sanoja = lue_tiedostosta()
    sopivat = []
    for i in range(len(sanoja)):
        if sanoja[i].startswith(alku):
            sopivat.append(sanoja[i])
    
    if len(sopivat) < n:
        raise ValueError("Ei tarpeeksi sanoja")
    else:
        shuffle(sopivat)
    
    return sopivat[:n]


if __name__ == "__main__":
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)
