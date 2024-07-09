word = input("Sana: ")

print("*" * 30)
print("*", end="")
print(" " * (14 - len(word) // 2), end="")
print(word, end="")
if len(word) % 2 == 0:
    print(" " * (14 - len(word) // 2), end="")
else:
    print(" " * (13 - len(word) // 2), end="")
print("*")
print("*" * 30)