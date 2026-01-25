import random
luku=random.randint(1,10)
arvaus=float(input("Arvaa numero 1-10"))
while(arvaus!=luku):
    if(arvaus>luku):
        print("Liian suuri arvaus")
        arvaus = float(input("Arvaa uudestaan"))
    if(arvaus<luku):
        print("Liian pieni arvaus")
        arvaus = float(input("Arvaa uudestaan"))
print("Oikein")