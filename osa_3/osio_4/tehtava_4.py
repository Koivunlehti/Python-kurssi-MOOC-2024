
def tulosta_monesti(merkkijono, maara):
    laskuri = 0
    while laskuri < maara:
        print(merkkijono)
        laskuri += 1

if __name__ == "__main__":
    tulosta_monesti("hei", 5)

    print()

    merkkijono = "Alussa olivat suo, kuokka ja Python"
    kertaa = 3
    tulosta_monesti(merkkijono, kertaa)