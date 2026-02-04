nimi = input("Anna nimi")
lista={nimi}
while(nimi!=''):
    nimi = input("Anna nimi")
    if nimi in lista:
        print("Nimi on jo listassa")
    else:
        print("Uusi nimi")
    lista.add(nimi)
print (lista)