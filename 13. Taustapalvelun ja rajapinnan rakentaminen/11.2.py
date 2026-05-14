class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def tulosta_tiedot(self):
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus: {self.huippunopeus}")
        print(f"nopeus: {self.nopeus}")
        print(f"matka: {self.matka}")


class Sahkoauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, akkukapasiteetti,nopeus,matka):
        super().__init__(rekisteritunnus, huippunopeus,nopeus,matka)
        self.akkukapasiteetti = akkukapasiteetti

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


    def tulosta_tiedot(self,):
        super().tulosta_tiedot()
        print(f"Akkukapasiteeti on {self.akkukapasiteetti}kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,bensatankki,nopeus,matka):
        super().__init__(rekisteritunnus, huippunopeus,nopeus,matka)
        self.bensatankki = bensatankki


    def aja(self,tunnit):
        self.matka += self.nopeus * tunnit

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"bensakapatankki on {self.bensatankki}l")




sahko = Sahkoauto("ABC-15", 180, 52.2,100,0)

bensa= Polttomoottoriauto("ACD-123", 165, 32.3,80,0)


print("Sähköauton tiedot: ")
sahko.aja(3)
sahko.tulosta_tiedot()


print("bensaauton tiedot: ")
bensa.aja(3)
bensa.tulosta_tiedot()
