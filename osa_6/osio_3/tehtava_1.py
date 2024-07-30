def lue(pyynto, min :int ,max :int):
    while True:
        try:
            luku = int(input(pyynto))
            if luku >= min and luku <= max:
                return luku
        except:
            pass
        print(f"Syötteen on oltava kokonaisluku väliltä {min}... {max}")



if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)