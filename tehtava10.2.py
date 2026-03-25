class Hissi:
    def __init__(self,maxkerros,minkerros,hissinro):
        self.hissinro=str(hissinro)
        self.maxkerros=maxkerros
        self.minkerros=minkerros
        self.missanyt=minkerros
    def siirry(self,kerrat):
        if(kerrat>0):
            while kerrat >0:
                self.ylos()
                kerrat=kerrat-1
        if(kerrat<0):
            while kerrat<0:
                self.alas()
                kerrat = kerrat +1
    def ylos(self,):
        self.missanyt=self.missanyt+1
        print(f"Hissi on nyt {self.missanyt} kerroksessa.")
    def alas(self,):
        self.missanyt=self.missanyt-1
        print(f"Hissi on nyt {self.missanyt} kerroksessa.")
class Talo:
    def __init__(self,alinkerros,ylinkerros,hissienmaara):
        self.alinkerros=alinkerros
        self.ylinkerros=ylinkerros
        self.hissienmaara=hissienmaara
        self.hissilista=[]
        for hissienmaara in range(hissienmaara):
            hissienmaara=Hissi(ylinkerros,alinkerros,hissienmaara)
            self.hissilista.append(hissienmaara)
    def ajahissia(self,hissinro,montakerrosta):
        self.hissilista[hissinro].siirry(montakerrosta)
talo1=Talo(2,9,3)
print(talo1.ajahissia(1,2))