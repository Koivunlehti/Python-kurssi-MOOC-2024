from datetime import date

def vuodet_listaan(paivamaarat:list) -> list:
    vuodet = []
    for paivamaara in paivamaarat:
        vuodet.append(paivamaara.year)
    vuodet.sort()
    return vuodet

if __name__ == "__main__":
    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    print(vuodet)