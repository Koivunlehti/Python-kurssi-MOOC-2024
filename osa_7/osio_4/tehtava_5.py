import difflib

def hae_sanat() -> list:
    sanat = []
    with open("osa_7/osio_4/wordlist.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            sanat.append(rivi)
    return sanat

def tarkista(teksti, sanat):
    tekstin_sanat = teksti.split(" ")
    vaarin = []
    for i in range(0, len(tekstin_sanat)):
        if tekstin_sanat[i].lower() not in sanat:
            print("*" + tekstin_sanat[i] + "*", end=" ")
            vaarin.append(tekstin_sanat[i])
        else:
            print(tekstin_sanat[i],end=" ")
    print()

    print("korjausehdotukset:")
    for sana in vaarin:
        print(f"{sana}:", end=" ")
        korjaukset = difflib.get_close_matches(sana,sanat)
        for i in range(len(korjaukset)):
            if i == len(korjaukset) - 1:
                print(korjaukset[i])
            else:
                print(korjaukset[i],end=", ")

def main():
    teksti = input("Write text: ")
    sanat = hae_sanat()
    tarkista(teksti,sanat)

main()