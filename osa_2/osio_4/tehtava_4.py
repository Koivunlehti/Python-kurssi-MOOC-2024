password = input("Salasana: ")

while True:
    if input("Toista salasana: ") == password:
        print("Käyttäjätunnus luotu!")
        break
    else:
        print("Ei ollut sama!")