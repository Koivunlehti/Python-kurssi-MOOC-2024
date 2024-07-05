word_1 = input("Anna 1. sana: ")
word_2 = input("Anna 2. sana: ")

if word_1 < word_2:
    print(f"{word_2} on aakkosjärjestyksessä viimeinen.")
elif word_1 > word_2:
    print(f"{word_1} on aakkosjärjestyksessä viimeinen.")
else:
    print("Annoit saman sanan kahdesti")