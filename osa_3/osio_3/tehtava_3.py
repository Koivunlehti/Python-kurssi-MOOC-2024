while True:
    number = int(input("Anna luku: "))
    
    if number <= 0:
        break
    else:
        counter = 1
        result = 1
        while counter <= number:
            result *= counter
            counter += 1
        print(f"Luvun {number} kertoma on {result}")

print("Kiitos ja moi!")