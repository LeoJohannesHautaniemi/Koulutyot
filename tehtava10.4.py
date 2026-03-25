import random
rekisterinumerovalikappale=0
kilpailijat=[]
tungit=0
class Auto:
    def __init__(self,rekisteritunnus):
        self.rekisteri=f"ABC-{rekisteritunnus}"
        self.huippunopeus=random.randint(100,200)
        self.matka=0
        self.nopeus=0
        rekisteritunnus++1
    def kiihdyta(self, nopeus_muutos):
        self.nopeus += nopeus_muutos
        if self.nopeus <0:
            self.nopeus=0
        if self.nopeus > self.huippunopeus:
            self.nopeus=self.huippunopeus
    def kulje(self, tunnit=1):
        self.matka=self.nopeus*tunnit+self.matka
class Kilpailu:
    def __init__(self,nimi,kilometrit,autolista):
        self.kilpailunimi=nimi
        self.pituus=kilometrit
        self.osallistujat=autolista
    def tunti_kuluu(self):
        for kisaaja in kilpailijat:
                kisaaja.kiihdyta(random.randint(-10, 15))
                kisaaja.kulje(1)
    def tulosta_tilanne(self):
        for kisaaja in kilpailijat:
            print(f"{kisaaja.rekisteri}, huippunopeus on {kisaaja.huippunopeus}km/h, kuljettu matka on {kisaaja.matka}km/h, nopeus nyt on {kisaaja.nopeus}km/h.")
    def kilpailu_ohi(self):
        for kisaaja in kilpailijat:
            if kisaaja.matka>self.pituus:
                return True
        else:
            return False
while(len(kilpailijat)<10):
    rekisterinumerovalikappale=rekisterinumerovalikappale+1
    kisaaja=Auto(rekisterinumerovalikappale)
    kilpailijat.append(kisaaja)
Suuriromuralli=Kilpailu("Suuri romuralli",8000,kilpailijat)

while Suuriromuralli.kilpailu_ohi()==False:
        for kisaaja in kilpailijat:
            if(kisaaja.matka < Suuriromuralli.pituus):
                Suuriromuralli.tunti_kuluu()
                tungit=tungit+1
            if tungit % 10:
                Suuriromuralli.tulosta_tilanne()
if Suuriromuralli.kilpailu_ohi:
    print("Ohi on")
    Suuriromuralli.tulosta_tilanne()