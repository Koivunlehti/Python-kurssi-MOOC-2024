word = input("Sana: ")
char = input("Merkki: ")

index = 0
while True:
    index = word.find(char)
    if index == -1:
        break
    else:
        if index + 2 < len(word):
            print(word[index:index + 3])
        word = word[index + 1:]