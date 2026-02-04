toiminto=input(f"Valitse toiminto \n 1 Syötä uusi lentoasema \n 2 Hae syötetyä asemaa \n 3 Lopeta")
lista={}
while toiminto!='3':
    if toiminto == '1':
        lentoasema = input("Anna aseman nimi")
        icao = input("Anna tuon aseman icao koodi")
        lista[icao] = lentoasema
    if toiminto == '2':
        koodi = input("Anna aseman icao koodi")
        if koodi in lista:
            print(f"Asema koodille {koodi} on {lista[koodi]}")
    toiminto = input(f"Valitse toiminto \n 1 Syötä uusi lentoasema \n 2 Hae syötetyä asemaa \n 3 Lopeta")