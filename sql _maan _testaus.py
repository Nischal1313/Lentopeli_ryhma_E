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
    vastaus = if_country_exist(next_country)
    if not vastaus:
        next_country = print(str(("Anna valtion nimi: ")))
    else:
        break



VALUUTTA ASIAT:

    # Amerikka
US_coin1, crime_stopped1, km, location_atm, round_nro = (
    game("José Marti International Airport", "Chile", 6360,
         4, 0, "Havanna", 0, 0,))

US_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Santiago de Chile Airport", "US",
         8969, US_coin1, crime_stopped1, location_atm, km, round_nro))

US_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
game("McCarran International Airport", "Brasilia",
     9975, US_coin2, crime_stopped2, location_atm1, km1, round_nro1))

US_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
game("Galeão International Airport", "Kanada",
     8211, US_coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, US_coin4, km3, location_atm3)


    # Eurooppa
EU_coin1, crime_stopped1, km, location_atm, round_nro = (
    game("Václav Havel Airport Praguet", "Saksa", 256,
         4, 0, "Praha", 0, 0,))

EU_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Berlin Brandenburg Airport", "Islanti",
         2412, EU_coin1, crime_stopped1, location_atm, km, round_nro))

EU_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
game("Kelavik International Airport", "Italia",
     3071, EU_coin2, crime_stopped2, location_atm1, km1, round_nro1))

EU_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
game("Peretola Airport", "Espanja",
     799, EU_coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, EU_coin4, km3, location_atm3)


    # Afrikka
AF_coin1, crime_stopped1, km, location_atm, round_nro = (
    game("Murtala Muhammed International Airport", "Etelä-Afrikka", 4767,
         4, 0, "Nigeria", 0, 0,))

AF_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Cape Town International Airport", "Burundi",
         3569, AF_coin1, crime_stopped1, location_atm, km, round_nro))

AF_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
game("Bujumbura International Airport", "Sierra Leone",
     4899, AF_coin2, crime_stopped2, location_atm1, km1, round_nro1))

AF_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
game("Lungi International Airport", "Egypti",
     5209, AF_coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, AF_coin4, km3, location_atm3)


    # Aasia
AA_coin1, crime_stopped1, km, location_atm, round_nro = (
    game("Kolkata Airport", "Nepali", 639,
         4, 0, "Intia", 0, 0,))

AA_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Tribhuvan International Airport", "Qatar",
         3365, AA_coin1, crime_stopped1, location_atm, km, round_nro))

AA_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
game("Hamad International Airport", "Malesia",
     5910, AA_coin2, crime_stopped2, location_atm1, km1, round_nro1))

AA_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
game("Kuala Lumpur International Airport", "Etelä-Korea",
     4601, AA_coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, AA_coin4, km3, location_atm3)