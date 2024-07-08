word_1 = input("Anna jono 1: ")
word_2 = input("Anna jono 2: ")

if len(word_1) > len(word_2):
    print(f"{word_1} on pidempi")
elif len(word_2) > len(word_1):
    print(f"{word_2} on pidempi")
else:
    print("jonot ovat yhtä pitkät")