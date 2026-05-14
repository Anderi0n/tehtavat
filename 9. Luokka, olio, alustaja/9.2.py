class Auto:
    pass
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä (self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def tulosta_tiedot(self):
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus: {self.huippunopeus}")
        print(f"nopeus: {self.nopeus}")
        print(f"matka: {self.matka}")


auto1 = Auto("ABC-123", 142)
auto2 = Auto("BCA-222", 299)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.tulosta_tiedot()
auto1.kiihdytä(-200)
auto1.tulosta_tiedot()

