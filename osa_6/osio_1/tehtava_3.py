def lue_tiedosto():
    tiedosto = open("osa_6/osio_1/matriisi.txt")
    matriisi = []
    for rivi in tiedosto:
            matriisi.append(rivi.replace("\n","").split(","))
    return matriisi

def summa():
        matriisi = lue_tiedosto()
        kaikkien_summa = 0
        for luvut in matriisi:
            for luku in luvut:
                kaikkien_summa += int(luku)
        return kaikkien_summa
             

def maksimi():
    matriisi = lue_tiedosto()
    suurin = 0
    ensimmainen_luku = True
    for luvut in matriisi:
        for luku in luvut:
            if ensimmainen_luku:
                suurin = int(luku)
                ensimmainen_luku = False
            else:
                if int(luku) > suurin:
                    suurin = int(luku)
    return suurin

def rivisummat():
    matriisi = lue_tiedosto()
    summat = []
    for luvut in matriisi:
        summa = 0
        for luku in luvut:
            summa += int(luku)
        summat.append(summa)
    return summat

if __name__ == "__main__":
    print("Summa:", summa())
    print("Maksimi:", maksimi())
    print("Rivisummat:", rivisummat())