def palindromi(sana):
    kaannetty_sana = ""
    for i in range(len(sana)-1,-1,-1):
        kaannetty_sana += sana[i]
    if sana == kaannetty_sana:
        return True
    else:
        return False

while True:
    sana = input("Anna palindromi: ")
    if palindromi(sana):
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")

if __name__ == "__main__":
    pass