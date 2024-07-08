pin = "4321"
counter = 1

while True:
    if input("PIN-koodi: ") == pin:
        break
    else:
        counter += 1
        print("Väärin")

if counter == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {counter} yritystä")