class teksti:
    def __init__(self,nimi):
        self.nimi=nimi
class kirja(teksti):
    def __init__(self,nimi,sivut,kirjailija):
        self.sivut=sivut
        super().__init__(nimi)
        self.kirjailija=kirjailija
class lehti(teksti):
    def __init__(self,nimi,paatoimittaja):
        self.paatoimittaja=paatoimittaja
        super().__init__(nimi)
akkari=lehti("Aku Ankka","Aki Hyyppä")
hytti=kirja("Hytti n:o6",200,"Rosa Liksom")
print(hytti.nimi,hytti.sivut,hytti.kirjailija)
print(akkari.nimi,akkari.paatoimittaja)