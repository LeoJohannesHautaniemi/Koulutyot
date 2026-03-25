class Auto:
    def __init__(self,rekisteritunnus,huippunopeus, tamanhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteri=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.tamanhetkinen_nopeus=tamanhetkinen_nopeus
        self.matka=kuljettu_matka
uusi_auto=Auto("ABC-123","142 km/h")
print(uusi_auto.rekisteri , uusi_auto.huippunopeus ,uusi_auto.tamanhetkinen_nopeus, uusi_auto.matka)