def ilman_vokaaleja(merkkijono):
    vokaalit = "aeiouyäö"
    for vokaali in vokaalit:
        merkkijono = merkkijono.replace(vokaali,"")
    return merkkijono

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))