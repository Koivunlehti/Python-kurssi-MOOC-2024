def transponoi(matriisi: list):
    # Kerätään tähän taulukkoon matriisin kaikki numerot järjestyksessä
    apulista = []   
    for rivi in matriisi:
        for alkio in rivi:
            apulista.append(alkio) 
    
    # Käytetään for silmukoiden indeksejä päinvastoin
    # ja asetetaan apulistan arvoja alkuperäiseen matriisiin
    apulista_index = 0
    for i in range(len(matriisi)):    
        for j in range(len(matriisi[i])):
            matriisi[j][i] = apulista[apulista_index]
            apulista_index += 1

if __name__ == "__main__":
    matriisi = [[1,2,3],[4,5,6],[7,8,9]]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)