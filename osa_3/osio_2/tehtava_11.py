word = input("Anna merkkijono: ")

counter = len(word) - 1
while counter >= 0:
    print(word[counter:len(word)])
    counter -= 1