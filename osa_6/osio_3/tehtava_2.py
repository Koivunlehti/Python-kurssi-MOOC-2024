def uusi_henkilo(nimi: str, ika: int):
    nimi = str(nimi)
    try:
        ika = int(ika)
    except:
        ika = -1

    if nimi == "":
        raise ValueError("nimi on tyhjä merkkijono")
    if nimi.find(" ") == -1 or nimi.find(" ") == 0 or nimi.find(" ") == len(nimi) -1:
        raise ValueError("nimi ei koostu vähintään kahdesta sanasta")
    if len(nimi) > 40:
        raise ValueError("nimen pituus on yli 40 merkkiä")
    if ika < 0:
        raise ValueError("ikä on negatiivinen luku")
    if ika > 150:
        raise ValueError("ikä on suurempi kuin 150")
    return nimi, ika

if __name__ == "__main__":
    print(uusi_henkilo("teppo testaaja",32))