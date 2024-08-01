import string

def jaa_merkkeihin(merkkijono: str) -> tuple:
    kirjaimet = ""
    merkit = ""
    muut = ""

    for merkki in merkkijono:
        if merkki in string.ascii_letters:
            kirjaimet += merkki
        elif merkki in string.punctuation:
            merkit += merkki
        else:
            muut += merkki
            
    return (kirjaimet, merkit, muut)

if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])