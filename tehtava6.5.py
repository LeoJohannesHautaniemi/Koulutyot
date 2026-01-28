import random
Lukul=[]
Lukul2=[]
toistaja=random.randint(1,9)
while (toistaja>=0):
    lisaus=random.randint(1,9)
    Lukul.append(lisaus)
    toistaja=toistaja-1

    def lasku():
        return [luku for luku in Lukul if luku % 2 == 0]

for luku in Lukul:
    Lukul2.append(luku)
print(f"tässä vanha lista {Lukul2} ja uusi lista{lasku()}")