import string

def alusta(ohjelma: list):
    # Alustetaan tarvittavat muuttujat
    muuttujat = {}
    for merkki in string.ascii_uppercase:
        muuttujat[merkki] = 0
    
    siirtymat = {}

    # Tarkistetaan mahdolliset siirtymäkohdat
    for i in range(len(ohjelma)):
        if ohjelma[i].find(":") != -1:
            if ohjelma[i].islower():
                siirtymat[ohjelma[i].replace(":","")] = i
    return muuttujat, siirtymat

def suorita(ohjelma: list) -> list:
    muuttujat, siirtymat = alusta(ohjelma)
    tuloste = []
    i = 0
    while i < len(ohjelma):
        kaskyt = ohjelma[i].split(" ")
        match kaskyt[0]:
            # Tulosta
            case "PRINT":   
                if kaskyt[1] in muuttujat:
                    tuloste.append(int(muuttujat[kaskyt[1]]))
                else:
                    tuloste.append(int(kaskyt[1]))
            # Aseta arvo muuttujaan
            case "MOV":
                if kaskyt[2] in muuttujat:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[2]])
                else:
                    muuttujat[kaskyt[1]] = int(kaskyt[2])
            # Yhteenlasku arvoilla
            case "ADD":
                if kaskyt[2] in muuttujat:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) + int(muuttujat[kaskyt[2]])
                else:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) + int(kaskyt[2])
            # Vähennyslasku arvoilla
            case "SUB":
                if kaskyt[2] in muuttujat:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) - int(muuttujat[kaskyt[2]])
                else:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) - int(kaskyt[2])
            # Kertominen arvoilla
            case "MUL":
                if kaskyt[2] in muuttujat:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) * int(muuttujat[kaskyt[2]])
                else:
                    muuttujat[kaskyt[1]] = int(muuttujat[kaskyt[1]]) * int(kaskyt[2])
            # Hyppää annettuun kohtaan
            case "JUMP":
                i = siirtymat[kaskyt[1]]
                continue
            # Ehtolauseen käsittely
            case "IF":
                vertailut = ["==", "!=", "<", "<=", ">", ">="]
                operaattori_index = vertailut.index(kaskyt[2])
                if kaskyt[1] in muuttujat: 
                    arvo_1 = int(muuttujat[kaskyt[1]])
                else:
                    arvo_1 = int(kaskyt[1])
                if kaskyt[3] in muuttujat: 
                    arvo_2 = int(muuttujat[kaskyt[3]])
                else:
                    arvo_2 = int(kaskyt[3])
                
                match vertailut[operaattori_index]:
                    case "==":
                        if arvo_1 == arvo_2:
                            i = siirtymat[kaskyt[5]]
                    case "!=":
                        if arvo_1 != arvo_2:
                            i = siirtymat[kaskyt[5]]
                    case "<":
                        if arvo_1 < arvo_2:
                            i = siirtymat[kaskyt[5]]
                    case "<=":
                        if arvo_1 <= arvo_2:
                            i = siirtymat[kaskyt[5]]
                    case ">":
                        if arvo_1 > arvo_2:
                            i = siirtymat[kaskyt[5]]
                    case ">=":
                        if arvo_1 >= arvo_2:
                            i = siirtymat[kaskyt[5]]
            # Lopetus
            case "END":
                return tuloste
                
        i += 1
    return tuloste

if __name__ == "__main__":
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print(tulos)

    ohjelma2 = []
    ohjelma2.append("MOV A 1")
    ohjelma2.append("MOV B 10")
    ohjelma2.append("alku:")
    ohjelma2.append("IF A >= B JUMP loppu")
    ohjelma2.append("PRINT A")
    ohjelma2.append("PRINT B")
    ohjelma2.append("ADD A 1")
    ohjelma2.append("SUB B 1")
    ohjelma2.append("JUMP alku")
    ohjelma2.append("loppu:")
    ohjelma2.append("END")
    tulos = suorita(ohjelma2)
    print(tulos)

    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print(tulos)

    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print(tulos)