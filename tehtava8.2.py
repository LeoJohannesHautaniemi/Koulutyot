import mysql.connector
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="käyttäjänimi",
    password="salasana",
    autocommit=True
)

maakoodi = input("Anna maakoodi : ")

sql = """
SELECT type, COUNT(*) 
FROM airport
WHERE iso_country = %s
GROUP BY type
"""

kursori = yhteys.cursor()
kursori.execute(sql, (maakoodi,))
tulokset = kursori.fetchall()

if tulokset:
    print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
    for tyyppi, lukumaara in tulokset:
        print(f"{tyyppi}: {lukumaara}")
