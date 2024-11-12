class Raha:
    def __init__(self,eurot:int, sentit:int) -> None:
        self.eurot = eurot
        self.sentit = sentit
    
    def __str__(self) -> str:
        return f"{self.eurot}.{'0' if self.sentit < 10 else ''}{self.sentit} eur"


if __name__ == "__main__":
    e1 = Raha(4, 10)
    e2 = Raha(2, 5)  # kaksi euroa ja viisi senttiä

    print(e1)
    print(e2)