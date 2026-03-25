import random
rekisterinumerovalikappale=0
kilpailijat=[]
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
random.randint(1,11)
while(len(kilpailijat)<10):
    rekisterinumerovalikappale=rekisterinumerovalikappale+1
    kisaaja=Auto(rekisterinumerovalikappale)
    kilpailijat.append(kisaaja)
while (kisaaja.matka<10000):
    for kisaaja in kilpailijat:
        if(kisaaja.matka<10000):
            kisaaja.kiihdyta(random.randint(-10,15))
            kisaaja.kulje(1)
            print(kisaaja.matka)
for kisaaja in kilpailijat:
    print(f"{kisaaja.rekisteri}, huippunopeus on {kisaaja.huippunopeus}km/h, kuljettu matka on {kisaaja.matka}km/h, nopeus maalissa on {kisaaja.nopeus}km/h.")