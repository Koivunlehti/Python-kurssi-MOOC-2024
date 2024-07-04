number = int(input("Anna luku: "))

if number < 1000:
    print("Luku on pienempi kuin 1000")
    if number < 100:
        print("Luku on pienempi kuin 100")
        if number < 10:
            print("Luku on pienempi kuin 10")

print("Kiitos!")