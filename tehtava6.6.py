import math
def metripizza(eurot,halkaisija):
    alue=1/4*math.pi*halkaisija**2
    hintaper=alue/eurot
    return hintaper


pizzaH=float(input("Anna pitsan halkasija: "))
pizzaM=float(input("Anna pitsan hinta: "))
pizza1=metripizza(pizzaM,pizzaH)

pizzaH=float(input("Anna toisen pitsan halkasija: "))
pizzaM=float(input("Anna toisen pitsan hinta: "))
pizza2=metripizza(pizzaM,pizzaH)

if(pizza2<pizza1):
    print("Pizza 2 on halvempi per alue")
if(pizza2>pizza1):
    print("Pizza 1 on halvempi per alue")
if(pizza2==pizza1):
    print("Pizzat ovat saman hintaiset per alue")