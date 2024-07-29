def hae_sanat() -> list:
    sanat = []
    with open("osa_6/osio_1/wordlist.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            sanat.append(rivi)
    return sanat

def tarkista(teksti, sanat):
    tekstin_sanat = teksti.split(" ")
    for i in range(0, len(tekstin_sanat)):
        if tekstin_sanat[i].lower() not in sanat:
            print("*" + tekstin_sanat[i] + "*", end=" ")
        else:
            print(tekstin_sanat[i],end=" ")

def main():
    teksti = input("Write text: ")
    sanat = hae_sanat()
    tarkista(teksti,sanat)

main()