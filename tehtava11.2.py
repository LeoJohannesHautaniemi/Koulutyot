class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteri=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.matka=0
        self.nopeus=0
    def kulje(self, tunnit=1):
        self.matka=self.nopeus*tunnit+self.matka
class Eauto(Auto):
    def __init__(self,rekisteri,huippunopeus,akku):
        Auto.__init__(rekisteri,huippunopeus)
        self.akku=akku
        self.nopeus=100
class Pauto(Auto):
    def __init__(self,rekisteri,huippunopeus,lopo):
        Auto.__init__(rekisteri, huippunopeus)
        self.lopo=lopo
        self.nopeus=1000
byd=Eauto("ABC-15", 180, "52.5 kWh")
ford=Pauto("ACD-123", 165 , "32.3 l")
byd.kulje(3)
ford.kulje(3)
print(ford.matka,byd.matka)