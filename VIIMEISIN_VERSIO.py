from geopy.distance import geodesic as GD
import mysql.connector
import sys

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

# Eurooppa (km)
prague_berlin = 256
berlin_reykjavik = 2412
reykjavik_firenze = 3071
firenze_barcelona = 799

# game("Václav Havel Airport Prague","germany", 256, 4, 0, "prague", 0,0)
# game("Berlin Brandenburg Airport","italy", 964, 4, 0, "berlin", 0,0)
# game("Peretola Airport","iceland", 3070, 4, 0, "firenze", 0,0)
# game("Kelavik International Airport","spain", 2974, 4, 0, "reykjavik", 0,0)

# Afrikka (km)
lagos_capetown = 4767
capetown_burundi = 3569
burundi_freetown = 4899
freetown_cairo = 5209
#afrikka
# game("Murtala Muhammed International Airport","south_africa", 4767, 4, 0, "lagos", 0,0)
# game("Cape Town International Airport ","bujumbura", 3569, 4, 0, "capetown", 0,0)
# game("Bujumbura International Airport","sierra_leone", 4899, 4, 0, "burundi", 0,0)
# game("Lungi International Airport ","egypt", 5209, 4, 0, "freetown", 0,0)

# Aasia (km)
calutta_kathmandu = 639
kathmandu_doha = 3365
doha_kualalumpur = 5910
kualalumpur_seoul = 4601
# aasia
# game("Kolkata Airport", "nepal", 639, 4, 0, "calkutta", 0,0)
# game("Tribhuvan International Airport", "gatar", 3365, 4, 0, "kathmandu", 0,0)
# game("Hamad International Airport ","malaysia", 5910, 4, 0, "doha", 0,0)
# game("Kuala Lumpur International Airport","south_korea", 4601, 4, 0, "kualalumpur", 0,0)

# Amerikka (km)
havanna_santiago = 6360
santiogo_lasvegas = 8969
lasvegas_riodejaneiro = 9975
riodejaneiro_quebec = 8211

# amerikka
# game("José Marti International Airport", "chile", 6360, 4, 0, "havanna", 0,0)
# game("Santiago de Chile Airport", "US", 8969, 4, 0, "santiago", 0,0)
# game("McCarran International Airport","brazil", 9975, 4, 0, "lasvegas", 0,0)
# game("Galeão International Airport","canada", 8211, 4, 0, "riodejaneiro", 0,0)

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


def if_eurooppa():
    EU_coin1, crime_stopped1, km, location_atm, round_nro = (
        game("Václav Havel Airport Prague", "Saksa", 256,
             4, 0, "Praha", 0, 0, ))

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
    database="karkuteilla2",
    user="root",
    password="maailmanilmaa",
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
    sql = "Select tip_1 From airport"
    sql += f" Where name = '{airport_name}'"
    tulos = suoritaHaku(sql)
    return tulos


def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += " Where name = '{airport_name}'"
    sijainti = suoritaHaku(sql2)
    return sijainti

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
        print("VAROITUS, sinulla on alle 2 kolikkoa! Jos et pääse rosvon jäljille seuraavalla lentokentällä, olet vaarassa hävitä pelin.")
    return warning(coins)


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
    print("")
    print(style.BLACK + f"Welcome to {airport_name}" + style.RESET)
    print("")

    for x in get_first_tip(airport_name):
        print(style.MAGENTA + x[0] + style.RESET)

    print("")
    print(
        f"Sinun stats KM: {pelaajan_kilometrit} HETACOINS: {coins} Rikokset pysäytetty: {crimes_stopped} Kierros: {rounds_played}")
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
        if player_choise == "1" or player_choise == "2":
            break

    if player_choise == "1":
        next_country = input("Anna valtion nimi: ")
        while True:
            vastaus = if_country_exist(next_country)
            if not vastaus:
                next_country = input(str(("Anna valtion nimi: ")))
            else:
                break
        if next_country == correct_country_name:
            coins += 2
            crimes_stopped += 1
        sijainti1 = youre_here(f"{airport_name}")
        sijainti2 = youre_going(f"{next_country}")  # pitäisi hakea tietokannasta

        distance = GD(sijainti1, sijainti2).km
        print(distance)
        if next_country != correct_country_name:
            coins -= 1
            crimes_stopped = crimes_stopped

    if player_choise == "2":
        coins = coins - 1
        sql = "Select tip_2 From airport "
        sql += f" where name = '{airport_name}'"
        tulos = suoritaHaku(sql)
        print(tulos)
        next_country = input(
            f"Aika on lopussa, sinun on pakko valita seuraava kohde saamasi tietojen perusteella."
        )
        if next_country == correct_country_name:
            crimes_stopped += 1
            sijainti1 = youre_here(f"{airport_name}")
            sijainti2 = youre_going(f"{next_country}")

            distance = GD(sijainti1, sijainti2).km
        else:
            coins -= 1
            sijainti1 = youre_here(f"{airport_name}")
            sijainti2 = youre_going(f"{next_country}")

            distance = GD(sijainti1, sijainti2).km


    rangaistus = oikea_matka(distance, 257)
    pelaajan_kilometrit += rangaistus

    warning(coins)

    # Ei palauta arvoa km oikein

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
            print("Olet valinnut Euroopan.")
            print("")
            print(
                "Olet saapunut Tśekkiin, tervetuloa Prahan kansainväliseen lentokenttään!"
            )
        if easy_level == "2":
            print("Olet valinnut Amerikat.")
            print(plane_art())
            print(
                "Olet saapunut Cuubaan, tervetuloa Havannan kansainväliseen lentokenttään!"
            )

    if difficulty_level == "2":
        while True:
            easy_level = input("Valitse vaikeustason manner: Aasia(3) tai Afrikka(4): ")
            if easy_level == "3" or "4":
                break

        if easy_level == "3":
            print("Olet valinnut Aasian.")
            print(plane_art())
            print(
                "Olet saapunut Kalkuttaan, tervetuloa Kolkatan kansainväliseen lentokenttään!"
            )

        if easy_level == "4":
            print("Olet valinnut Afrikka.")
            print(plane_art())
            print(
                "Olet saapunut Nigeriaan, tervetuloa Murtala Muhammedin kansainväliseen lentokenttään!"
            )
    return easy_level #P #Palutta #
 #Paluttaa meille arvon siitä minkä tason pelaaja on valinnut.


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
            if_eurooppa() #Tähän latautuu Eurooppa


        if pelaajan_taso_valinta == "2":
            if_amerikka() #Tähän latautuu Amerikka

        if pelaajan_taso_valinta == "3":
            if_aasia() #Tähän latautuu Aasia

        else:
            if_afrikka() #Tähän latautuu Afrikka

        break





# EU_coin = Euroopan valuutta
# AA_coin = Aasian valuutta
# US_coin = Amerikan valuutta
# AF_coin = Afrikan valuutta