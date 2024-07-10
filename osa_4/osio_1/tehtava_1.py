while True:
    word = input("Editori: ")
    word = word.lower()
    if word == "word" or word == "notepad":
        print("surkea")
    elif word == "visual studio code":
        print("loistava valinta!")
        break
    else:
        print("ei ole hyvä")