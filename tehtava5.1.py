import random
summa=0
i=int(input("Monta arpakuutiota? "))
for noppa in range(i):
    kuutionarvo=random.randint(1,6)
    summa+=kuutionarvo
print(summa)