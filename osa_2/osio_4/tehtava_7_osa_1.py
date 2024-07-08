story = ""

while True:
    word = input("Anna sana: ")
    if word == "loppu":
        break
    else:
        story += word + " "

print(story)