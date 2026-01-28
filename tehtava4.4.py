import random
luku=random.randint(1,10)
arvaus=int(input("Arvaa numero 1-10"))
while(arvaus!=luku):
    if(arvaus>luku):
        arvaus = int(input( "Liian suuri arvaus"'\n'"Arvaa uudestaan"))
    else:
        arvaus = int(input("Liian pieni arvaus"'\n'"Arvaa uudestaan"))
print("Oikein")