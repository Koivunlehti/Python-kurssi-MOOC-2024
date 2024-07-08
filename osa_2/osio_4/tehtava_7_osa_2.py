story = ""
last_word = ""

while True:
    word = input("Anna sana: ")
    if word == "loppu" or word == last_word:
        break
    else:
        story += word + " "
    last_word = word

print(story)