class Auto:
    pass
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus: {self.huippunopeus}")
        print(f"nopeus: {self.nopeus}")
        print(f"matka: {self.matka}")

auto1 = Auto("ABC-123", 142)
auto2 = Auto("BCA-222", 299)

auto1.tulosta_tiedot()
auto2.tulosta_tiedot()