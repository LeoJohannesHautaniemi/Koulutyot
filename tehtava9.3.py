class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteri=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.matka=2000
        self.nopeus=0
    def kiihdyta(self, nopeus_muutos):
        self.nopeus += nopeus_muutos
        if self.nopeus <0:
            self.nopeus=0
        if self.nopeus > self.huippunopeus:
            self.nopeus=self.huippunopeus
    def kulje(self, tunnit):
        self.matka=self.nopeus*tunnit+self.matka
uusi_auto=Auto("ABC-123",142)
uusi_auto.kiihdyta(60)
uusi_auto.kulje(1.5)
print(uusi_auto.matka)