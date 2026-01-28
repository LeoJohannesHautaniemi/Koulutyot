luku=0
lista=[]
while luku !='':
    luku = (input("Anna Luku: "))
    if luku !='':
        luku =int(luku)
        lista.append(luku)
lista.sort(reverse=True)
for luku in lista[0:6]:
    print(luku)