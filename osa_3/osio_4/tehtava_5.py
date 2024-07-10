def risunelio(koko):
    laskuri = 0
    while laskuri < koko:
        print("#" * koko)
        laskuri += 1


if __name__ == "__main__":
    risunelio(3)
    print()
    risunelio(5)