sentence = input("Anna lause: ")

while True:
    if len(sentence) > 0:
        print(sentence[0])
    if sentence.find(" ") == -1:
        break
    else:
        sentence = sentence[sentence.find(" ") + 1:]
