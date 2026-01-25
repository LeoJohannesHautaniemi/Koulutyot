kayttis=input("Anna Käyttäjätunnus")
salasana=input("Anna Salasana")
yritykset=0
while((kayttis!="python" or salasana !="rules") and yritykset <= 5):
    kayttis = input("Anna Käyttäjätunnus")
    salasana = input("Anna Salasana")
    yritykset=yritykset+1
if(kayttis=="python" and salasana=="rules"):
    print("Tervetuloa")
else:
    print("Pääsy evätty")