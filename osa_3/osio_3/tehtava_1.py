number = int(input("Anna luku: "))

index = 1

while index <= number:
    index_2 = 1
    while index_2 <= number:
        print(f"{index} x {index_2} = {index * index_2}")
        index_2 += 1
    index += 1
    