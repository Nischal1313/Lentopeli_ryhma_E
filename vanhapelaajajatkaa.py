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

def execute_command(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

# Eurooppa (km)
prague_berlin = 256
berlin_firenze = 964
firenze_reykjavik = 3070
reykjavik_barcelona = 2974

# game("Václav Havel Airport Prague","germany", 256, 4, 0, "prague", 0,0)
# game("Berlin Brandenburg Airport","italy", 964, 4, 0, "berlin", 0,0)
# game("Peretola Airport","iceland", 3070, 4, 0, "firenze", 0,0)
# game("Kelavik International Airport","spain", 2974, 4, 0, "reykjavik", 0,0)

# Afrikka (km)
lagos_capetown = 4767
capetown_burundi = 3569
burundi_freetown = 4899
freetown_cairo = 5209
# afrikka
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


def save(coins, pelaajan_kilometrit, location_atm, crimes_stopped, user_name): # continent otettu pois, lisätään jos tarvitaan
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin.
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}',"
    sql += f" location = (select iso_country from airport where name = '{location_atm}'),"
    sql += f" crimes_stopped = '{crimes_stopped} where screen_name = '{user_name}'"
    execute_command(sql)
    return # ei vielä kutsuttu

def delete_user(user_name): # poistaa pelaajan KAIKKI tiedot
    sql = f"delete from game where screen_name = '{user_name}'"
    execute_command(sql)
    return

def get_old_data(user_name):
    sql = "select coin, km_travelled, location, crimes_stopped" # continent poistettu
    sql += f" from game where screen_name = '{user_name}'"
    suoritaHaku(sql)
    return #pitäisi palauttaa kaikki nämä tiedot


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla",
    user="root",
    password="rotallaonvaljaat",
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
    print(tulos)
    return


def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += " Where name = '{airport_name}'"
    sijainti = suoritaHaku(sql2)
    return sijainti


def end_game(crime_stopped, coin, km, location_atm3):  # kato mikä taso/manner pelattu

    if location_atm3 == "Kanada" and crime_stopped4 >= 3:
        print(
            "Onnittelut agentti! Olet suorittanut vaarallisen matkasi ympäri maailmaa, ja tulokset ovat selvät.\nKansainväliset rikolliset ovat nyt telkien takana, heidän suunnitelmansa paljastettu ja rikokset estetty.\nSinä ja agenttiryhmäsi onnistuitte, ja maailma on nyt turvallisempi paikka. Olet saavuttanut legendaarisen maineen agenttien joukossa, voitto on sinun!")
        print("Olet estänyt näin", crime_stopped, "rikosta kaikista rikoksista ja sinulla on", coin,
              "HETACOINS:ia ja olet matkustanut", km, "kilometriä.")
    if location_atm3 != "Kanada" or crime_stopped4 < 3:
        print(
            "Pimeys vallitsee, kun seisot hävinneenä lentokentän varjoissa. Vaikka taistelit parhaasi mukaan, rikolliset pääsivät kerta toisensa jälkeen käsistäsi.\nKansainväliset operaatiot päättyivät katastrofeihin, ja kukaan ei ole turvassa.\nSinut on virallisesti erotettu agenttijoukosta, ja jäät pohtimaan mitä olisit voinut tehdä toisin.\nJärjestöt jatkavat rikoksiaan, ja maailma tarvitsee nyt enemmän kuin koskaan sankareita.\nSinun seikkailusi päättyi pettymykseen, mutta ehkä tulet saamaan vielä mahdollisuuden palata taisteluun…")
        print("Olet estänyt vain", crime_stopped, "rikosta kaikista rikoksista ja sinulla on vain", coin,
              "HETACOINS:ia ja olet matkustanut", km, "kilometriä.")


def warning(coins):
    if coins < 2:
        print(
            "VAROITUS, sinulla on alle 2 kolikkoa! Jos et pääse rosvon jäljille seuraavalla lentokentällä, olet vaarassa hävitä pelin.")
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
    print("Whatt" + style.BLACK + f"Welcome to {airport_name}" + style.RESET)
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
    return easy_level  # P #Palutta #


# Paluttaa meille arvon siitä minkä tason pelaaja on valinnut.

def new_or_old_game():
    while True:
        uusi_vanha_peli = int(input("Haluatko jatkaa vanhaa peliä (1) vai aloittaa uuden pelin (2)?: "))
        if uusi_vanha_peli == 1:
            get_old_data(user_name)
            


        elif uusi_vanha_peli == 2:
            delete_user(user_name)
            # jotenkin pitäisi saada uusi peli käyntiin tämän jälkeen
            break






def vanha_vai_uusi_pelaaja(user_name):
    sql = f"Select screen_name From game where screen_name = '{user_name}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)

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
            coin1, crime_stopped1, km, location_atm, round_nro = (
                game("Václav Havel Airport Prague",
                     "Saksa", 256,
                     4, 0, "prague",
                     0, 0))

            coin2, crime_stopped2, km1, location_atm1, round_nro1 = game(
                "Berlin Brandenburg Airport",
                "islanti",
                256,
                coin1,
                crime_stopped1,
                location_atm,
                km,
                round_nro,
            )

            game(
                "Peretola Airport",
                "iceland",
                3070,
                coin2,
                crime_stopped2,
                location_atm1,
                km1,
                round_nro1,
            )

        if pelaajan_taso_valinta == "2":
            coin1, crime_stopped1, km, location_atm, round_nro = (
                game("José Marti International Airport", "Chile", "6360",
                     4, 0, "Havanna", 0, 0, ))

coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Santiago de Chile Airport", "US",
         8969, coin1, crime_stopped1, location_atm, km, round_nro))

coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
    game("McCarran International Airport", "Brasilia",
         9975, coin2, crime_stopped2, location_atm1, km1, round_nro1))

coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
    game("Galeão International Airport", "Kanada",
         8211, coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, coin4, km3, location_atm3)

if pelaajan_taso_valinta == "3":
    game()  # Tähän latautuu Aasia

# else:
#    coin1, crime_stopped1, km, location_atm, round_nro = game("Murtala Muhammed International Airport",
#                                                              "Nigeria", 4767, 4,
#                                                              0, "Nigeria", 0,
#                                                              0))))  # Tähän latautuu Afrikka

#    break

EU_coin
AA_coin
US_coin
AF_coin

# Amerikka
coin1, crime_stopped1, km, location_atm, round_nro = (
    game("José Marti International Airport", "Chile", "6360",
         4, 0, "Havanna", 0, 0, ))

coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Santiago de Chile Airport", "US",
         8969, coin1, crime_stopped1, location_atm, km, round_nro))

coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
    game("McCarran International Airport", "Brasilia",
         9975, coin2, crime_stopped2, location_atm1, km1, round_nro1))

coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
    game("Galeão International Airport", "Kanada",
         8211, coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, coin4, km3, location_atm3)

# Eurooppa
coin1, crime_stopped1, km, location_atm, round_nro = (
    game("Václav Havel Airport Prague", "Saksa", "256",
         4, 0, "Praha", 0, 0, ))

coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Berlin Brandenburg Airport", "Islanti",
         8969, coin1, crime_stopped1, location_atm, km, round_nro))

coin3, crime_stopped3, km2, location_atm2, round_nro2 = (
    game("McCarran International Airport", "Brasilia",
         9975, coin2, crime_stopped2, location_atm1, km1, round_nro1))

coin4, crime_stopped4, km3, location_atm3, round_nro3 = (
    game("Galeão International Airport", "Kanada",
         8211, coin3, crime_stopped3, location_atm2, km2, round_nro2))

end_game(crime_stopped4, coin4, km3, location_atm3)