word = input("Sana: ")
char = input("Merkki: ")

index = word.find(char)

if index != -1:
    if index + 2 < len(word):
        print(word[index:index + 3])