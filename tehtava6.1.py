import random
arvo=1
def noppa():
    tulos=random.randint(1,6)
    return tulos
while(arvo!=6):
    arvo=noppa()
    print(f"Nopan tulos on {arvo}")