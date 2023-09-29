import mysql.connector
from geopy.distance import geodesic as GD


def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += f" Where name = '{airport_name}'"
    sijainti = suoritaHaku(sql2)
    return sijainti


def oikea_matka(distance, oikeamatka):
    if oikeamatka > distance:
        rangaistus = (oikeamatka - distance) * 2
    if distance > oikeamatka:
        rangaistus = (distance - oikeamatka) * 2
    if distance == oikeamatka:
        rangaistus = rangaistus
    return rangaistus


def youre_going(next_country):
    sql = "select longitude_deg, latitude_deg"
    sql += " from airport where airport.iso_country"
    sql += " = (select iso_country from country"
    sql += f" where country.name = '{next_country}')"
    sijainti = suoritaHaku(sql)
    return sijainti


def get_first_tip(airport_name):
    sql = "Select tip_1 From airport "
    sql += f" where Name = '{airport_name}'"
    tulos = suoritaHaku(sql)
    print(tulos)
    return

def if_country_exist(next_country):
  sql = "select name from country "
  sql += "where name = '" + next_country + "'"
  tulos = suoritaHaku(sql)
  return tulos


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


def suoritaHaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
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
    print("")
    print(f"Welcome to {airport_name}")
    print("")

    get_first_tip(airport_name)
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

        # Funktion pitää palauttaa pelaajan_kilometrit, jonka voi ottaa samalla fuktion parametrilla, kun right_distance
        # jos pelaaja vastaa väärin sitten voi mennä laskemaan tuon fuktion, niin sitä voisi nyt laittaa tuohon
        # if lauseeseen, joka kattoo oliko pelaajan vastus oikea vai ei

        # Meidän olisi myös hyvä kattoo, että monesko kierro pelissä on meneillään. Jos kierroksia on jo mennyt 4 ja
        # pelaaja ei ole onnistunut pysättämään 3/4 rikosta niin se olisi automaattinen game over

        # Pitäisi myös katttoo if lausekkeella, että meneekö coins nollaan ja se viesti mistä oli puhetta, että
        # tulee pomolta viesti, että seuraava taso täytyy läpäistä ilman vinkkejä tai jtn sinne päin

    rangaistus = oikea_matka(distance, 257)
    pelaajan_kilometrit += rangaistus

    # print(rangaistus)

    # Ei palauta arvoa km oikein

    return coins, crimes_stopped, round(pelaajan_kilometrit), next_country, rounds_played


coin1, crime_stopped1, km, location_atm, round_nro = (
    game("Václav Havel Airport Prague", "Saksa",
         256, 4, 0, "prague", 0, 0))

coin2, crime_stopped2, km1, location_atm1, round_nro1 = (
    game("Berlin Brandenburg Airport", "islanti",
         256, coin1, crime_stopped1, location_atm, km, round_nro))

game("Peretola Airport", "iceland",
     3070, coin2, crime_stopped2, location_atm1, km1, round_nro1)
