luku1=float(input("Anna Leisviskät" ))
luku2=float(input("Anna Naulat" ))
Ineedmorebullets=float(input("Anna Luodit" ))

tulos=(Ineedmorebullets*13.3)+(luku2*32*13.3)+(luku1*20*32*13.3)
##en tiedä oliko konversio stringiksi ja substringaaminen tähän haluttu ratkaisu, mutta en keksinyt elegantinpaa ratkaisua
substring1=str(tulos)[:2]
substring=str(tulos)[2:]
print(f"Tässä tulos metrijärjestelmän luvuilla: {substring1} kilogrammaa ja {substring} grammaa")