kerrokset = int(input("Kerrokset: "))

merkit = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"

if kerrokset <= len(merkit):

    # Alustetaan matriisi tarvittavan kokoiseksi
    koko = kerrokset * 2 -1
    kuvio = []
    for i in range(koko):
        kuvio.append([])
        for j in range(koko):
            kuvio[i].append(" ")

    # Lisätään merkit matriisiin kutistaen aluetta joka kierroksella
    pienennys = 0
    for i in range(kerrokset - 1,-1,-1):
        for j in range(0 + pienennys, len(kuvio) - pienennys):
            for k in range(0 + pienennys, len(kuvio) - pienennys):
                kuvio[j][k] = merkit[i]
        pienennys += 1

    # Tulostetaan kuvio
    for i in range(len(kuvio)):
        for j in range(len(kuvio[i])):
            print(kuvio[i][j], end="")
        print()
