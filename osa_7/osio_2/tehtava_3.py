from string import ascii_lowercase, digits
from random import randint

def loytyyko(kohde: str, haettavat: str):
    loyty = False
    for i in range(len(haettavat)):
        if kohde.find(haettavat[i]) != -1:
            loyty = True
            break
    return loyty

def luo_hyva_salasana(merkkimaara: int, numeroita: bool, erikoismerkkeja: bool) -> str:
    sallitut_erikoismerkit = "!?=+-()#"
    salasana = ""

    while salasana == "":
        for i in range(merkkimaara):
            salasana += ascii_lowercase[randint(0,len(ascii_lowercase)-1)]

        if numeroita:
            for i in range(merkkimaara):
                if randint(0,1) == 1:
                    salasana = salasana.replace(salasana[i],digits[randint(0, len(digits) - 1)])
        
        if erikoismerkkeja:
            for i in range(merkkimaara):
                if randint(0,1) == 1:
                    salasana = salasana.replace(salasana[i], sallitut_erikoismerkit[randint(0, len(sallitut_erikoismerkit) - 1)])
        
        kirjain_loyty = loytyyko(salasana, ascii_lowercase)
        numero_loyty = loytyyko(salasana, digits)
        erikoismerkki_loyty = loytyyko(salasana, sallitut_erikoismerkit)

        if numeroita and erikoismerkkeja:
            if kirjain_loyty == False or numero_loyty == False or erikoismerkki_loyty == False:
                salasana = ""
        elif numeroita:
            if kirjain_loyty == False or numero_loyty == False:
                salasana = ""
        elif erikoismerkkeja:
            if kirjain_loyty == False or erikoismerkki_loyty == False:
                salasana = ""

    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))