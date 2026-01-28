import random
summa=1
Lukul=[]
def lasku(summa):
    for luku in Lukul:
        summa=luku+summa
    return summa
toistot= random.randint(1,99)
while toistot>1:
    Lukul.append(random.randint(1,9))
    summa=lasku(summa)
    toistot=toistot-1
print(summa)