class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteri=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.matka=0
        self.nopeus=0
        self.kuljettu_matka=0
    def kiihdyta(self, nopeus_muutos):
        self.nopeus += nopeus_muutos
        if self.nopeus <0:
            self.nopeus=0
        if self.nopeus > self.huippunopeus:
            self.nopeus=self.huippunopeus

uusi_auto=Auto("ABC-123",142)
print(uusi_auto.rekisteri , uusi_auto.huippunopeus ,uusi_auto.nopeus, uusi_auto.matka)
uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)
print(uusi_auto.nopeus)
uusi_auto.kiihdyta(-200)
print(uusi_auto.nopeus)