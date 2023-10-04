from geopy.distance import geodesic as GD
import mysql.connector
import sys

def if_amerikka():
    US_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("José Marti International Airport", "Chile", 6360,
             4, 0, "Havanna", 0, 0, ))

    US_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
        game("Santiago de Chile Airport", "US",
             8969, US_coin1, crime_stopped1, location_atm, km, round_nro))

    US_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
        game("McCarran International Airport", "Brasilia",
             9975, US_coin2, crime_stopped2, location_atm1, km1, round_nro1))

    US_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
        game("Galeão International Airport", "Kanada",
             8211, US_coin3, crime_stopped3, location_atm2, km2, round_nro2))


def if_aasia():
    AA_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("Kolkata Airport", "Nepali", 639,
             4, 0, "Intia", 0, 0, ))

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


def if_eurooppa():
    EU_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("Václav Havel Airport Prague", "Saksa", 256,
             4, 0, "Praha", 0, 0))

    EU_coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
        game("Berlin Brandenburg Airport", "Islanti",
             2412, EU_coin1, crime_stopped1, location_atm, km, round_nro))

    EU_coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
        game("Keflavik International Airport", "Italia",
             3071, EU_coin2, crime_stopped2, location_atm1, km1, round_nro1))

    EU_coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
        game("Peretola Airport", "Espanja",
             799, EU_coin3, crime_stopped3, location_atm2, km2, round_nro2))

    end_game(crime_stopped4, EU_coin4, km3, location_atm3)

def if_afrikka():
    AF_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("Murtala Muhammed International Airport", "Etelä-Afrikka", 4767,
             4, 0, "Nigeria", 0, 0, ))

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

def end_game(crime_stopped, coin, km, location_atm3 ): #kato mikä taso/manner pelattu

    if location_atm3 == "Kanada" and crime_stopped4 >= 3:
        print("Onnittelut agentti! Olet suorittanut vaarallisen matkasi ympäri maailmaa, ja tulokset ovat selvät.\nKansainväliset rikolliset ovat nyt telkien takana, heidän suunnitelmansa paljastettu ja rikokset estetty.\nSinä ja agenttiryhmäsi onnistuitte, ja maailma on nyt turvallisempi paikka. Olet saavuttanut legendaarisen maineen agenttien joukossa, voitto on sinun!")
        print("Olet estänyt näin", crime_stopped, "rikosta kaikista rikoksista ja sinulla on", coin,
              "HETACOINS:ia ja olet matkustanut", km, "kilometriä.")
    if location_atm3 != "Kanada" or crime_stopped4 < 3:
        print("Pimeys vallitsee, kun seisot hävinneenä lentokentän varjoissa. Vaikka taistelit parhaasi mukaan, rikolliset pääsivät kerta toisensa jälkeen käsistäsi.\nKansainväliset operaatiot päättyivät katastrofeihin, ja kukaan ei ole turvassa.\nSinut on virallisesti erotettu agenttijoukosta, ja jäät pohtimaan mitä olisit voinut tehdä toisin.\nJärjestöt jatkavat rikoksiaan, ja maailma tarvitsee nyt enemmän kuin koskaan sankareita.\nSinun seikkailusi päättyi pettymykseen, mutta ehkä tulet saamaan vielä mahdollisuuden palata taisteluun…")
        print("Olet estänyt vain", crime_stopped, "rikosta kaikista rikoksista ja sinulla on vain", coin,
              "HETACOINS:ia ja olet matkustanut", km, "kilometriä." )

def warning(coins):
    if coins < 2:
        print("")
        return print("VAROITUS, sinulla on alle 2 kolikkoa! Jos et pääse rosvon jäljille seuraavalla lentokentällä, olet vaarassa hävitä pelin.")
    return


def if_aasia():
    AA_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("Kolkata Airport", "Nepali", 639,
             4, 0, "Intia", 0, 0, ))

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


def stats(pelaajan_kilometrit,coins,crimes_stopped,rounds_played):
    print("")
    print(
        style.BLUE
        + f" K.M. : {pelaajan_kilometrit}       "
        + style.RESET
        + style.RED
        + f"  HETACOINS: {coins}       "
        + style.RESET
        + style.BLUE
        + f"  Rikokset pysäytetty: {crimes_stopped}       "
        + style.RESET
        + style.RED
        + f"  Kierros: {rounds_played}       "
        + style.RESET
    )
    print("")


def if_country_exist(next_country):
  sql = "select name from country "
  sql += f"where name = '{next_country}'"
  tulos = suoritaHaku(sql)
  return tulos

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



def suoritaHaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos



def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += f" Where name = '{airport_name}'"
    sijainti = suoritaHaku(sql2)
    return sijainti

def youre_going(next_country):
    sql = "select longitude_deg, latitude_deg"
    sql += " from airport where airport.iso_country"
    sql += " = (select iso_country from country"
    sql += f" where country.name = '{next_country}')"
    sijainti = suoritaHaku(sql)
    return sijainti


def oikea_matka(distance, oikeamatka):
    if oikeamatka > distance:
        rangaistus = (oikeamatka - distance) * 2
    if distance > oikeamatka:
        rangaistus = (distance - oikeamatka) * 2
    if distance == oikeamatka:
        rangaistus = rangaistus
    return rangaistus

def tallennus(coins, pelaajan_kilometrit, location_atm, crimes_stopped, coin_used, user_name):
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}',"
    sql += f" location = '{location_atm}', crimes_stopped = '{crimes_stopped}', coin_used = '{coin_used}'"
    sql += f" where screen_name = '{user_name}'"
    suoritaHaku(sql)
    return  # ei kai tarvii palauttaa mitään? #Tätä ei ole viellä kutsuttu.


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla_database",
    user="root",
    password="METROPOLIA13",
    autocommit=True,
)


def plane_art():
    return print(
        """
      ``+*:.
      =@@@@#.
       +@@@@@@..          .-:.
        :@@@@@@%:   .%@=..*@@@:.
         .*@@@@@@@:::#@@@**#@@@@@@@@@:.
           :@@@@@@@@@@@@@@@@@@@@@@@@#-.
            .-@@@@@@@@@@@@@@@@@=...
             .%@@@@@@@@@%#.
           :@@@@@@@@@@@@@:
           :%@@@@@@@@@@@@@#.
            .:@@@@@#.%@@@@@@+
          .@#.@@@@@:   #@@@@@@.
          :@@@@@@@+     .#@@@@@@@@@@@@*.
           .=@@@@@.       .+@@@@@@@#=..
             -@@@=         .@@@@@@.
             +@@#          .@@@--@@.
             #@@-          .@@+.
             .:+           .%@. """
    )


def get_first_tip(airport_name):
    sql = "Select tip_1 From airport "
    sql += f" where Name = '{airport_name}'"
    tulos = suoritaHaku(sql)
    return tulos

def get_second_tip(airport_name):
    sql = "Select tip_2 From airport "
    sql += f" where name = '{airport_name}'"
    tulos = suoritaHaku(sql)
    return tulos


def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += " Where name = '{airport_name}'"
    sijainti = suoritaHaku(sql2)
    return sijainti


def welcome_to(name):
    sql = f"select airport.name from airport,country where airport.iso_country = country.iso_country and "
    sql += f"country.name = '{name}'"
    tulos = suoritaHaku(sql)
    print("")
    return tulos



def if_country_is_real():
    while True:
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        sql = f"select name from country where name ='{next_country}'"
        tulos = suoritaHaku(sql)
        if tulos is not None:
            tulos = suoritaHaku(sql)[0]
            break
        else:
            continue
    return tulos


def game(
        airport_name,
        correct_country_name,
        right_distance,
        coins,
        crimes_stopped,
        location_atm,
        pelaajan_kilometrit,
        rounds_played
):
    rounds_played += 1

    for x in welcome_to(location_atm):
        print(style.RED + f"Welcome to", x[0] + style.RESET)
        print("")

    stats(pelaajan_kilometrit, coins, crimes_stopped, rounds_played)


    for x in get_first_tip(airport_name):
        print(style.MAGENTA + x[0] + style.RESET)
        print("")
    print(
        "Saamasi tiedon mukaan sinun pitäisi päättää mihin valtioon matkustat seuraavaksi."
    )
    print("")
    print(
        "Mikäli tietosi perusteella et pysty valitsemaan valtiota, voimme mahdollisuuksien mukaan hankkia sinulle lisää tietoa."
    )
    print("")
    while True:
        player_choise = str(input(
            "Matkustan saamani tiedon perusteella (1), "
            "Yrittäkää kerätätä lisäätietoa rikollisen seuraavasta kohteesta.(2): "
        )
        )
        print("")
        if player_choise == "1" or player_choise == "2":
            break

    if player_choise == "1":
        print("")
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        while True:
            vastaus = if_country_exist(next_country)
            if not vastaus:
                next_country = input(str("Anna valtion nimi: ")).capitalize()
                print("")
            else:
                break
        if next_country == correct_country_name:
            coins += 2
            crimes_stopped += 1
        sijainti1 = youre_here(f"{airport_name}")
        sijainti2 = youre_going(f"{next_country}")  # pitäisi hakea tietokannasta

        distance = GD(sijainti1, sijainti2).km

        if next_country != correct_country_name:
            crimes_stopped = crimes_stopped
            coins -= 1
            warning(coins)

    if player_choise == "2":
        coins -= 1
        warning(coins)
        stats(pelaajan_kilometrit, coins, crimes_stopped, rounds_played)
        print("")
        for x in get_second_tip(airport_name):
            print(style.MAGENTA + x[0] + style.RESET)
        print("")
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        while True:
            vastaus = if_country_exist(next_country)
            if not vastaus:
                next_country = input(str("Anna valtion nimi: ")).capitalize()
                print("")
            else:
                break

        if next_country == correct_country_name:
            crimes_stopped += 1
            coins += 1
            sijainti1 = youre_here(f"{airport_name}")
            sijainti2 = youre_going(f"{next_country}")

            distance = GD(sijainti1, sijainti2).km
        else:
            coins -= 1
            warning(coins)
            sijainti1 = youre_here(f"{airport_name}")
            sijainti2 = youre_going(f"{next_country}")

            distance = GD(sijainti1, sijainti2).km

    rangaistus = oikea_matka(distance, 257)
    pelaajan_kilometrit += rangaistus

    return coins, crimes_stopped, round(pelaajan_kilometrit), next_country, rounds_played


def vaikeustasojamanner():
    while True:
        print("Haluatko pelata pelin helpolla(1) vai vaikealla(2) vaikeustasolla?")
        print("")
        difficulty_level = input(
            str("1: Eurooppa tai Amerikat, 2: Aasia tai Afrikka: ")
        )
        print("")
        if difficulty_level == "1" or difficulty_level == "2":
            break
    if difficulty_level == "1":
        while True:
            easy_level = input(
                "Valitse vaikeustason manner: Eurooppa(1) tai Amerikat(2): "
            )
            if easy_level == "1" or "2":
                break

        if easy_level == "1":
            print("")
            print("Olet valinnut Euroopan.")
        if easy_level == "2":
            print("")
            print("Olet valinnut Amerikat.")

    if difficulty_level == "2":
        while True:
            easy_level = input("Valitse vaikeustason manner: Aasia(3) tai Afrikka(4): ")
            if easy_level == "3" or "4":
                break

        if easy_level == "3":
            print("")
            print("Olet valinnut Aasian.")

        if easy_level == "4":
            print("")
            print("Olet valinnut Afrikka.")

    return easy_level #Paluttaa meille arvon siitä minkä tason pelaaja on valinnut.


def vanha_vai_uusi_pelaaja(user_name):
    sql = f"Select screen_name From game where screen_name = '{user_name}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos is not None:
        print(f"Tervetuloa takaisin {user_name}!")

    else:
        print("")
        print(
            "Tervetuloa " + style.GREEN + f"{user_name}" + style.RESET, "uuteen peliin"
        )
        return tulos



print("")
print("")
print("")
print("Tervetuloa pelaamaan Lentäen Karkuteillä!")

print("")

plane_art()

print("")

user_name = str(input(style.RED + "Anna käyttäjätunnus: " + style.RESET))


vastaus = vanha_vai_uusi_pelaaja(user_name)

if not vastaus:
    while True:
        print(" ")
        pelaajan_taso_valinta = vaikeustasojamanner()
        print("")
        if pelaajan_taso_valinta == "1":
            if_eurooppa()
        if pelaajan_taso_valinta == "2":
            if_amerikka()
        if pelaajan_taso_valinta == "3":
            if_aasia()
        if pelaajan_taso_valinta == "4":
            if_afrikka()
        break




