import string

def vaihda_koko(merkkijono: str):
    teksti = ""
    for merkki in merkkijono:
        if merkki.isupper():
            merkki
            teksti += merkki.lower()
        else:
            teksti += merkki.upper()
    return teksti

def puolita(merkkijono: str):
    puolikas = merkkijono[:int(len(merkkijono) / 2)]
    return (puolikas, merkkijono.replace(puolikas,""))
    

def poista_erikoismerkit(merkkijono: str):
    teksti = ""
    for merkki in merkkijono:
        if merkki not in string.punctuation:
            teksti += merkki
    return teksti