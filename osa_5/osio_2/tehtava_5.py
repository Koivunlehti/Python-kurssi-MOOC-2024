def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x >= len(lauta[0]) or x < 0:
        return False
    if y >= len(lauta) or y < 0:
        return False
    if lauta[y][x] != "":
        return False
    lauta[y][x] = nappula
    return True

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)