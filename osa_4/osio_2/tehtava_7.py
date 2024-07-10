def joulukuusi(kerrokset):
    print("joulukuusi!")
    leveys = 1
    while kerrokset > 0:
        print(" " * kerrokset + "*" * leveys)
        leveys += 2
        kerrokset -= 1
    print(" " * (leveys // 2) + "*")


if __name__ == "__main__":
    joulukuusi(3)
    print()
    joulukuusi(5)