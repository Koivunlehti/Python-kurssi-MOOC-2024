def histogrammi(merkkijono: str):
    kaikki_merkit = {}
    for merkki in merkkijono:
        if merkki not in kaikki_merkit:
            kaikki_merkit[merkki] = 1
        else:
            kaikki_merkit[merkki] += 1
    
    for merkki, maara in kaikki_merkit.items():
        print(merkki, "*" * maara)

if __name__ == "__main__":

    histogrammi("abba")
    print()
    histogrammi("saippuakauppias")