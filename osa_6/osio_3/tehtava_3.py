def hae_tiedostosta():
    numerot = []
    with open("osa_6/osio_3/lottonumerot.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            rivi = rivi.split(";")
            numerot.append(rivi)
    return numerot

def tallenna_tiedostoon(rivit):
    with open("osa_6/osio_3/korjatut_numerot.csv","w") as tiedosto:
        for rivi in rivit:
            tiedosto.write(f"{rivi[0]};{rivi[1]}\n")

def suodata_virheelliset():
    rivit = hae_tiedostosta()
    ehjat_rivit = []
    for rivi in rivit:
        try:
            # tarkistetaan otsikko tieto
            viikko = rivi[0].split(" ")
            if viikko[0] != "viikko":
                raise ValueError("rivi ei ala sanalla 'viikko'")
            viikko_nro = int(viikko[1])
            if viikko_nro < 1 or viikko_nro > 52:
                raise ValueError("viikkonumero ei ole mahdollinen")
            
            # tarkistetaan numerot
            numerot = rivi[1].split(",")
            esiintyvat_numerot = []
            for i in range(0,len(numerot)):
                numero = int(numerot[i])
                if numero in esiintyvat_numerot:
                    raise ValueError("sama numero esiintyy ainakin kahdesti")
                
                if numero < 1 or numero > 39:
                    raise ValueError("numero ei ole sallituissa rajoissa")

                esiintyvat_numerot.append(numero)

            if len(esiintyvat_numerot) != 7:
                raise ValueError("väärä määrä numeroita")

            ehjat_rivit.append(rivi)
        except:
            pass

    tallenna_tiedostoon(ehjat_rivit)

if __name__ == "__main__":
    suodata_virheelliset()