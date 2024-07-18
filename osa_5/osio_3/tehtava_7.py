def lukukirja():
    sanakirja = {}
    tekstit = ["nolla","yksi","kaksi","kolme","neljä","viisi","kuusi","seitsemän","kahdeksan","yhdeksän"]
    tekstit_index = 0
    kymmenet = 0
    for i in range(100):
        if i <= 10:
            if i == 10:
                sanakirja[i] = "kymmenen"
            else:
                sanakirja[i] = tekstit[tekstit_index]
        if i > 10 and i < 20:
            sanakirja[i] = tekstit[tekstit_index] + "toista"
        if i >= 20:
            if i % 10 == 0:
                sanakirja[i] = tekstit[kymmenet] + "kymmentä"   
            else:
                sanakirja[i] = tekstit[kymmenet] + "kymmentä" + tekstit[tekstit_index]

        tekstit_index += 1
        if tekstit_index >= 10:
            tekstit_index = 0
            kymmenet += 1
    return sanakirja

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])