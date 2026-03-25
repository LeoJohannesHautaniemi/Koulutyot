import mysql.connector
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="käyttäjänimi",
    password="salasana",
    autocommit=True)
icao = input("Anna lentoaseman ICAO-koodi: ")
sql = """SELECT name, FROM airport WHERE ident = %s"""
kursori = yhteys.cursor()
kursori.execute(sql, (icao,))
tulos = kursori.fetchone()
if tulos:
    nimi, iso_country = tulos
    print(f"Lentokentän nimi: {nimi}")
    print(f"Sijaintikunta: {iso_country}")