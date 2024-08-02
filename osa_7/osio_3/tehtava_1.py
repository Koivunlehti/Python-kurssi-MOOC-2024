from datetime import datetime

def main():
    paiva = int(input("Päivä: "))
    kuukausi = int(input("Kuukausi: "))
    vuosi = int(input("Vuosi: "))
    
    ero = datetime(1999,12,31) - datetime(vuosi, kuukausi, paiva) 
    if ero.days >= 0:
        print(f"Olit {ero.days} päivää vanha, kun vuosituhat vaihtui.")
    else:
        print(f"Et ollut syntynyt, kun vuosituhat vaihtui.")
main()