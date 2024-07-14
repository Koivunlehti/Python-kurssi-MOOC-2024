def anagrammi(sana_1,sana_2):
    if sorted(sana_1.lower()) == sorted(sana_2.lower()):
        return True
    else:
        return False
    pass

if __name__ == "__main__":
    print(anagrammi("talo", "tola"))
    print(anagrammi("talo", "lato"))
    print(anagrammi("talo", "olat")) 
    print(anagrammi("tammi", "mitta"))
    print(anagrammi("python", "java"))