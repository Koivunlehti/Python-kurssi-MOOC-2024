def eniten_kirjainta(merkkijono):
    eniten_esiintyva = ""
    esiintymiskerrat = 0
    for merkki in merkkijono:
        if merkkijono.count(merkki) > esiintymiskerrat:
            eniten_esiintyva = merkki
            esiintymiskerrat = merkkijono.count(merkki)
    return eniten_esiintyva


if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))