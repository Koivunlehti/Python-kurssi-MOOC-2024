age = int(input("Kerro ikäsi? "))

if age < 5:
    if age < 0:
        print("Taitaa olla virhe")
    else:
        print("En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {age}-vuotias")