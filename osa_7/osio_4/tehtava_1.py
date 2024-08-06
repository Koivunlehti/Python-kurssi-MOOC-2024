import json

def tulosta_henkilot(tiedosto: str):
    with open("osa_7/osio_4/" + tiedosto) as sisalto:
        tiedot = sisalto.read()
    opiskelijat = json.loads(tiedot)
    
    for opiskelija in opiskelijat:
        print(f"{opiskelija['nimi']} {opiskelija['ika']} vuotta (",end="")
        for i in range(len(opiskelija['harrastukset'])):
            if i == len(opiskelija['harrastukset']) - 1:
                print(opiskelija['harrastukset'][i],end=")")
            else:    
                print(opiskelija['harrastukset'][i],end=", ")
        print()
        

if __name__ == "__main__":
    tulosta_henkilot("opiskelijat.json")