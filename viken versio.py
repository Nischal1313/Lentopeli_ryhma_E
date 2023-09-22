from geopy.distance import geodesic as GD
import mysql.connector
import sys

# eurooppa (km)
prague_berlin = 256
berlin_firenze = 964
firenze_reykjavik = 3070
reykjavik_barcelona = 2974


# afrikka (km)
lagos_capetown = 4767
capetown_burundi = 3569
burundi_freetown = 4899
freetown_cairo = 5209

# aasia (km)
calutta_kathmandu = 639
kathmandu_doha = 3365
doha_kualalumpur = 5910
kualalumpur_seoul = 4601

# amerikka (km)
havanna_santiago = 6360
santiogo_lasvegas = 8969
lasvegas_riodejaneiro = 9975
riodejaneiro_quebec = 8211

#sanakirja: oikeat matkat
eurooppa = {"256", "964", "3070", "2974"}
amerikka = {"6360", "8969", "9975", "8211"}
aasia = {"639", "3365", "5910", "4601"}
afrikka = {"4767", "3569", "4899", "5209"}

def oikea_matka():
    if eurooppa[0] > distance:
        rangaistus = (eurooppa[0] - distance) * 2
    elif distance > eurooppa[0]:
        rangaistus = (distance - eurooppa[0]) * 2
    elif eurooppa[0] == distance:
        print("ei tule rangaistus!")

    return rangaistus


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla",
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


def suoritaHaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


def vaikeustasojamanner():
    while True:
        difficulty_level = input(
            str("Haluatko pelata pelin helpolla(1) vai vaikealla(2) vaikeustasolla? ")
        )
        if difficulty_level == "1" or difficulty_level == "2":
            break
    if difficulty_level == "1":
        while True:
            easy_level = input(
                "Valitse vaikeustason manner: Eurooppa(1) tai Amerikat(2):"
            )
            if easy_level == "1" or "2":
                break

        if easy_level == "1":
            print("Olet valinnut Euroopan.")
            # print(jetaski)
            print(
                "Olet saapunut Eurooppaan, tervetuloa Prahan kansainväliseen lentokenttään!"
            )

        if easy_level == "2":
            print("Olet valinnut Amerikat.")
            # print(jetski)
            print(
                "Olet saapunut Amerikkaan, tervetuloa Havannan kansainväliseen lentokenttään!"
            )
            game(havanna, chile, 0, 0, 0, 0,havanna)


    if difficulty_level == "2":
        while True:
            easy_level = input("Valitse vaikeustason manner: Aasia(3) tai Afrikka(4):")
            if easy_level == "3" or "4":
                break

        if easy_level == "3":
            print("Olet valinnut Aasian.")
            # print(jetaski)
            print(
                "Olet saapunut Aasian,tervetuloa Kalkutan kansainväliseen lentokenttään!"
            )
            game(calcutta, nepal, 0, 0, 0, 0, calcutta)

        if easy_level == "4":
            print("Olet valinnut Afrikka.")
            # print(jetski)
            print(
                "Olet saapunut Afrikka, tervetuloa Etelä-Afrikan kansainväliseen lentokenttään!"
            )
            game(lagos, etelä-afrikka, 0,0, 0, 0, lagos)

            return easy_level


oikea_manner = vaikeustasojamanner()



def get_first_tip():
    sql = "Select tip_1, From airport "
    sql += " where name = '" + airport_name + "'"
    tulos = suoritaHaku(sql)
    print(tulos)
    return

def youre_here():
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += " Where name = '" + airport_name + "'"
    sijainti = suoritaHaku(sql2)
    return sijainti


def game(airport_name, correct_country_name, airport_name2, pelaajan_kilometrit, coins, crimes_stopped, location_atm):

    get_first_tip(airport_name)

    youre_here(location_atm)

    distance = GD(sijainti2, sijainti).km
    pelaajan_kilometrit = 0
    coins = 0
    crimes_stopped = 0
    print(f"Tervetuloa {airport_name}!")
    print(pelaajan_kilometrit, coins, crimes_stopped)
    print(
        "Saamasi tiedon mukaan sinun pitäisi päättää mihin valtioon matkustat seuraavaksi."
    )
    print(
        "Mikäli tietosi perusteella et pysty valitsemaan valtiota, voimme mahdollisuuksien mukaan hankkia sinulle lisää tietoa."
    )
    player_choise = str(
        input(
            "Matkustan saamani tiedon perusteella (1), "
            "Yrittäkää kerätätä lisäätietoa rikollisen seuraavasta kohteesta.(2)"
        )
    )
    if player_choise == "1":
        next_country = input("Anna valtion nimi: ")
        if next_country == correct_country_name:
            coins += 2
            crimes_stopped += 1

    if player_choise == "2":
        coins = coins - 1
        sql = "Select tip_2, From airport "
        sql += " where name = '" + airport_name + "'"
        tulos = suoritaHaku(sql)
        print(tulos)
        next_country = input(
            f"Aika on lopussa, sinun on pakko valita seuraava kohde saamasi tietojen perusteella."
        )
        if next_country == correct_country_name:
            coins += 1
            crimes_stopped +=1
        else:
            coins -= 1

        #kilometrifunktio rangaistus
        return airport_name, pelaajan_kilometrit,coins, crimes_stopped, location_atm




print("Tervetuloa pelaamaan Lentäen Karkuteillä!")
plane_art()
user_name = str(input("Anna käyttäjätunnus: "))


def vanha_vai_uusi_pelaaja(user_name,):
    sql = "Select screen_name From game"
    sql += f" where screen_name = '{user_name}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos is not None:
        print(f"Welcome back{user_name}")

    if tulos is None:
        print(f"Welcome {user_name} to a new game.")
        vaikeustasojamanner(ekamuutuja)
        game()

    return tulos


if vanha_vai_uusi_pelaaja(user_name) is not None:
    while True:
        print(
            f"Tervetuloa takaisin {user_name}! Haluatko aloittaa uuden pelin vai jatkaa vanhaa peliä?"
        )
        new_or_oldgame = input(
            "Paina 1, jos haluat aloittaa uuden pelin. Paina 2, jos haluat jatkaa vanhaa peliä "
        )
        if new_or_oldgame == "1":
            vaikeustasojamanner(manner_nimi)  # oikea manner, joka antaa tietoa game funktiolle
            game()  # laita oikeat tasot tulemaan
            print("kiitos!")
            break
        if new_or_oldgame == "2":
            print("oho")
        # load old game








