class Hissi:
    def __init__(self,maxkerros,minkerros):
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
maxkerros=int(input("Anna hissin korkein kerros"))
minkerros=int(input("Anna hissin matalin kerros"))
kone=Hissi(maxkerros,minkerros)
montakertaa=int(input(f"Anna monta kerrosta siirrytään"))
kone.siirry(montakertaa)
kone.siirry(-montakertaa)
print(kone.maxkerros,kone.minkerros,kone.missanyt)