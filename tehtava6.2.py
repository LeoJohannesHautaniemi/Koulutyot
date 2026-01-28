import random
tahkot=int(input("Monta tahkoa nopassa?"))
arvo=1
def noppa(tahkot2):
    tulos=random.randint(1,tahkot2)
    return tulos
while(arvo!=tahkot):
    arvo=noppa(tahkot)
    print(f"Nopan tulos on {arvo}")