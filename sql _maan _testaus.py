import mysql.connector

yhteys = mysql.connector.connect(
  host="localhost",
  port=3306,
  database="karkuteilla2",
  user="root",
  password="maailmanilmaa",
  autocommit=True,
)

def suoritaHaku(sql):
  kursori = yhteys.cursor()
  kursori.execute(sql)
  tulos = kursori.fetchall()
  return tulos

def if_country_exist(next_country):
  sql = "select name from country "
  sql += "where name = '" + next_country + "'"
  tulos = suoritaHaku(sql)
  return tulos



while True:
    next_country = input("Anna maa minne haluat matkustaa: ")
    vastaus = if_country_exist(next_country)
    if not vastaus:
        print("Väärä maa")
    else:
        print("Tervetuloa...")
        break
