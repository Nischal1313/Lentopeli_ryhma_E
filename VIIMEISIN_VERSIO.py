from geopy.distance import geodesic as GD
import mysql.connector
import sys

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla",
    user="root",
    password="rotallaonvaljaat",
    autocommit=True,
)


def thanks():
    print("")
    print("THANKS FOR PLAYING!")


def if_africa():
    AF_coin1, crime_stopped1, km, location_atm, round_nro = game(
        "Murtala Muhammed International Airport",
        "Etelä-Afrikka",
        4767,
        4,
        0,
        "Nigeria",
        0,
        0,
    )

    AF_coin2, crime_stopped2, km1, location_atm1, round_nro1 = game(
        "Cape Town International Airport",
        "Burundi",
        3569,
        AF_coin1,
        crime_stopped1,
        location_atm,
        km,
        round_nro,
    )

    AF_coin3, crime_stopped3, km2, location_atm2, round_nro2 = game(
        "Bujumbura International Airport",
        "Sierra Leone",
        4899,
        AF_coin2,
        crime_stopped2,
        location_atm1,
        km1,
        round_nro1,
    )

    AF_coin4, crime_stopped4, km3, location_atm3, round_nro3 = game(
        "Lungi International Airport",
        "Egypti",
        5209,
        AF_coin3,
        crime_stopped3,
        location_atm2,
        km2,
        round_nro2,
    )

    end_game(crime_stopped4, AF_coin4, km3, location_atm3, "Egypti")


def if_amerikka():
    US_coin1, crime_stopped1, km, location_atm, round_nro = game(
        "José Marti International Airport",
        "Chile",
        6360,
        4,
        0,
        "Havanna",
        0,
        0,
    )

    US_coin2, crime_stopped2, km1, location_atm1, round_nro1 = game(
        "Santiago de Chile Airport",
        "US",
        8969,
        US_coin1,
        crime_stopped1,
        location_atm,
        km,
        round_nro,
    )

    US_coin3, crime_stopped3, km2, location_atm2, round_nro2 = game(
        "McCarran International Airport",
        "Brasilia",
        9975,
        US_coin2,
        crime_stopped2,
        location_atm1,
        km1,
        round_nro1,
    )

    US_coin4, crime_stopped4, km3, location_atm3, round_nro3 = game(
        "Galeão International Airport",
        "Kanada",
        8211,
        US_coin3,
        crime_stopped3,
        location_atm2,
        km2,
        round_nro2,
    )
    end_game(crime_stopped4, US_coin4, km3, location_atm3, "Kanada")


def if_asia():
    AA_coin1, crime_stopped1, km, location_atm, round_nro = game(
        "Kolkata Airport",
        "Nepali",
        639,
        4,
        0,
        "Intia",
        0,
        0,
    )

    AA_coin2, crime_stopped2, km1, location_atm1, round_nro1 = game(
        "Tribhuvan International Airport",
        "Qatar",
        3365,
        AA_coin1,
        crime_stopped1,
        location_atm,
        km,
        round_nro,
    )

    AA_coin3, crime_stopped3, km2, location_atm2, round_nro2 = game(
        "Hamad International Airport",
        "Malesia",
        5910,
        AA_coin2,
        crime_stopped2,
        location_atm1,
        km1,
        round_nro1,
    )

    AA_coin4, crime_stopped4, km3, location_atm3, round_nro3 = game(
        "Kuala Lumpur International Airport",
        "Etelä-Korea",
        4601,
        AA_coin3,
        crime_stopped3,
        location_atm2,
        km2,
        round_nro2,
    )

    end_game(crime_stopped4, AA_coin4, km3, location_atm3)


def if_eurooppa():
    EU_coin1, crime_stopped1, km, location_atm, round_nro = game(
        "Václav Havel Airport Prague", "Saksa", 256, 4, 0, "Praha", 0, 0
    )
    EU_coin2, crime_stopped2, km1, location_atm1, round_nro1 = game(
        "Berlin Brandenburg Airport",
        "Islanti",
        2412,
        EU_coin1,
        crime_stopped1,
        location_atm,
        km,
        round_nro,
    )
    if EU_coin2 > 0:
        EU_coin3, crime_stopped3, km2, location_atm2, round_nro2 = game(
            "Keflavik International Airport",
            "Italia",
            3071,
            EU_coin2,
            crime_stopped2,
            location_atm1,
            km1,
            round_nro1,
        )
        if EU_coin3 > 0:
            EU_coin4, crime_stopped4, km3, location_atm3, round_nro3 = game(
                "Peretola Airport",
                "Espanja",
                799,
                EU_coin3,
                crime_stopped3,
                location_atm2,
                km2,
                round_nro2,
            )
            end_game(crime_stopped4, EU_coin4, km3, location_atm3, "Espanja")
        else:
            print("Sinun HETACOINS on nollilla, jonka takia hävisit tason tässä vaiheessa!")
    else:
        print("Sinun HETACOINS on nollilla, jonka takia hävisit tason tässä vaiheessa!")
    print("")
    while True:
        print("Haluatko pelata tason uudestaan?")
        EU_answer = str(input("KYLLÄ[1] , EN[2]: "))
        print("")
        if EU_answer == "1" or EU_answer == "2":
            break
    return EU_answer


def end_game(
    crime_stopped4, coin, km, location_atm3, correct_country_name
):  # kato mikä taso/manner pelattu
    if location_atm3 == correct_country_name and crime_stopped4 >= 3:
        print(
            "Onnittelut agentti! Olet suorittanut vaarallisen matkasi ympäri maailmaa, ja tulokset ovat selvät.\nKansainväliset rikolliset ovat nyt telkien takana, heidän suunnitelmansa paljastettu ja rikokset estetty.\nSinä ja agenttiryhmäsi onnistuitte, ja maailma on nyt turvallisempi paikka.\nOlet saavuttanut legendaarisen maineen agenttien joukossa, voitto on sinun!"
        )
        print(
            "Olet estänyt näin",
            crime_stopped4,
            "rikosta kaikista rikoksista ja sinulla on",
            coin,
            "HETACOINS:ia ja olet matkustanut",
            km,
            "kilometriä.",
        )
    if location_atm3 != correct_country_name or crime_stopped4 < 3:
        print(
            style.RED
            + "Pimeys vallitsee, kun seisot hävinneenä lentokentän varjoissa. \nVaikka taistelit parhaasi mukaan, rikolliset pääsivät kerta toisensa jälkeen käsistäsi.\nKansainväliset operaatiot päättyivät katastrofeihin, ja kukaan ei ole turvassa.\nSinut on virallisesti erotettu agenttijoukosta, ja jäät pohtimaan mitä olisit voinut tehdä toisin.\nJärjestöt jatkavat rikoksiaan, ja maailma tarvitsee nyt enemmän kuin koskaan sankareita.\nSinun seikkailusi päättyi pettymykseen, mutta ehkä tulet saamaan vielä mahdollisuuden palata taisteluun…"
        )
        print(
            "Olet estänyt vain",
            crime_stopped4,
            "rikosta kaikista rikoksista ja sinulla on vain",
            coin,
            "HETACOINS:ia ja olet matkustanut",
            km,
            "kilometriä." + style.RESET,
        )


def warning(coins):
    if coins == 0:
        print("")
    else:
        if 0 < coins < 2:
            print("")
            print(
                style.RED + "VAROITUS, sinulla on alle 2 kolikkoa!"
                " Jos et pääse rosvon jäljille seuraavalla lentokentällä, olet vaarassa hävitä pelin."
                + style.RESET)
    return


def stats(player_kilometers, coins, crimes_stopped, rounds_played):
    print("")
    print(
        style.BLUE
        + f" K.M. : {player_kilometers}       "
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
    answer = execute_sql(sql)
    return answer


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def execute_sql(sql):
    cursor = yhteys.cursor()
    cursor.execute(sql)
    ans = cursor.fetchall()
    return ans

def execute_command(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += f" Where name = '{airport_name}'"
    location = execute_sql(sql2)
    return location


def youre_going(next_country):
    sql = "select longitude_deg, latitude_deg"
    sql += " from airport where airport.iso_country"
    sql += " = (select iso_country from country"
    sql += f" where country.name = '{next_country}')"
    location = execute_sql(sql)
    return location


def oikea_matka(distance, right_distance):
    if right_distance > distance:
        penalty = (right_distance - distance) * 2
    if distance > right_distance:
        penalty = (distance - right_distance) * 2
    if distance == right_distance:
        penalty = penalty
    return penalty


def save(coins, pelaajan_kilometrit, location_atm, crimes_stopped, user_name, round_nro): # continent otettu pois, lisätään jos tarvitaan
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin.
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}',"
    sql += f" location = (select iso_country from airport where name = '{location_atm}'),"
    sql += f" crimes_stopped = '{crimes_stopped}, round_nro = '{round_nro}' where screen_name = '{user_name}'"
    execute_command(sql)
    return

def delete_old_user(user_name): #poistaa vanhan pelaajan kaikki tiedot
    sql = f"delete from game where screen_name = '{user_name}'"
    execute_command(sql)
    return

def add_new_user(screen_name, airport_name): #parametreinä kaikki vastaavat pythonista, selectin jälkeiset voisi muuttaa muuttujiksi?
    sql = "insert into game (coin, km_travelled, location, screen_name, crimes_stopped)"
    sql += f" select 4, 0, ident, '{screen_name}', 0 from airport where name = '{airport_name}'"
    execute_command(sql)
    return

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
    tulos = execute_sql(sql)
    return tulos


def get_second_tip(airport_name):
    sql = "Select tip_2 From airport "
    sql += f" where name = '{airport_name}'"
    tulos = execute_sql(sql)
    return tulos


def youre_here(airport_name):
    sql2 = "SELECT latitude_deg, longitude_deg from airport"
    sql2 += " Where name = '{airport_name}'"
    sijainti = execute_sql(sql2)
    return sijainti


def welcome_to(name):
    sql = f"select airport.name from airport,country where airport.iso_country = country.iso_country and "
    sql += f"country.name = '{name}'"
    tulos = execute_sql(sql)
    print("")
    return tulos


def if_country_is_real():
    while True:
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        sql = f"select name from country where name ='{next_country}'"
        tulos = execute_sql(sql)
        if tulos is not None:
            tulos = execute_sql(sql)[0]
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
    player_km,
    rounds_played,
):
    rounds_played += 1

    for x in welcome_to(location_atm):
        print(style.RED + f"Welcome to", x[0] + style.RESET)
        print("")

    stats(player_km, coins, crimes_stopped, rounds_played)

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
        player_choise = str(
            input(
                "Matkustan saamani tiedon perusteella [1], "
                "Yrittäkää kerätä lisää tietoa rikollisen seuraavasta kohteesta [2]: "
            )
        )
        print("")
        if player_choise == "1" or player_choise == "2":
            break

    if player_choise == "1":
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        while True:
            answer = if_country_exist(next_country)
            if not answer:
                next_country = input(str("Anna valtion nimi: ")).capitalize()
                print("")
            else:
                break
        if next_country == correct_country_name:
            coins += 2
            crimes_stopped += 1
        distance1 = youre_here(f"{airport_name}")
        distance2 = youre_going(f"{next_country}")  # pitäisi hakea tietokannasta

        distance = GD(distance1, distance2).km

        if next_country != correct_country_name:
            crimes_stopped = crimes_stopped
            coins -= 1
            warning(coins)

    if player_choise == "2":
        coins -= 1
        warning(coins)
        stats(player_km, coins, crimes_stopped, rounds_played)
        print("")

        for x in get_second_tip(airport_name):
            print(style.MAGENTA + x[0] + style.RESET)
        print("")
        next_country = str(input("Anna valtion nimi: ")).capitalize()
        print("")
        while True:
            answer = if_country_exist(next_country)
            if not answer:
                next_country = input(str("Anna valtion nimi: ")).capitalize()
                print("")
            else:
                break

        if next_country == correct_country_name:
            crimes_stopped += 1
            coins += 1
            distance1 = youre_here(f"{airport_name}")
            distance2 = youre_going(f"{next_country}")

            distance = GD(distance1, distance2).km
        else:
            coins -= 1
            warning(coins)
            distance1 = youre_here(f"{airport_name}")
            distance2 = youre_going(f"{next_country}")

            distance = GD(distance1, distance2).km

    penalty = oikea_matka(distance, 257)
    player_km += penalty

    return coins, crimes_stopped, round(player_km), next_country, rounds_played


def difficulty_lvl():
    while True:
        print("")
        print("Haluatko pelata pelin helpolla[1] vai vaikealla[2] vaikeustasolla?")
        print("")
        difficulty_level = input(
            str("[1]: Eurooppa tai Amerikat, [2]: Aasia tai Afrikka: ")
        )
        print("")
        if difficulty_level == "1" or difficulty_level == "2":
            break
    if difficulty_level == "1":
        while True:
            easy_level = input(
                "Valitse vaikeustason manner: Eurooppa[1] tai Amerikat[2]: "
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
            easy_level = input("Valitse vaikeustason manner: Aasia[3] tai Afrikka[4]: ")
            if easy_level == "3" or "4":
                break

        if easy_level == "3":
            print("")
            print("Valitsit Aasian.")

        if easy_level == "4":
            print("")
            print("Olet valinnut Afrikka.")

    return easy_level  # Paluttaa meille arvon siitä minkä tason pelaaja on valinnut.


def new_or_player(user_name):
    sql = f"Select screen_name From game where screen_name = '{user_name}'"
    ans = execute_sql(sql)
    if ans is not None:
        print("")
        print(f"Tervetuloa takaisin {style.GREEN}{user_name}{style.RESET}!")
        # voisko tähän pompauttaa kuvan, jossa on intro ja pelin ohjeet pelaajalle?
        print("")
        while True:
            new_old_game = int(input("Haluatko jatkaa vanhaa peliä [1] vai aloittaa kokonaan uuden pelin [2]?: "))

            if new_old_game == 2: # OIKEESTI POISTAA SIT KAIKKI HUOM HUOM!!!!!!!!!!!
                delete_old_user(user_name)
                print(
                    "Tervetuloa" + style.GREEN + f"{user_name}" + style.RESET, "uuteen peliin"
                )
            break
    else:
        print("")
        print(
            "Tervetuloa" + style.GREEN + f"{user_name}" + style.RESET, "uuteen peliin"
        )

    return

print("")
print("")
print("Tervetuloa pelaamaan Lentäen Karkuteillä!")
print("")
plane_art()
print("")
user_name = str(input(style.RED + "Anna käyttäjätunnus: " + style.RESET))


new_or_player(user_name)


while True:
    player_lvl = difficulty_lvl()
    if player_lvl == "1":
        while True:
            print("")
            again = if_eurooppa()
            if again == "2":  # 2 = ei
                thanks()
                break
    if player_lvl == "2":
        while True:
            again = if_amerikka()
            if again == "2":
                break
    if player_lvl == "3":
        while True:
            again = if_asia()
            if again == "2":
                break
    if player_lvl == "4":
        while True:
            again = if_africa()
            if again == "2":
                break
    print("")
    print("Mitä tasoa haluat pelata seuraavaksi?")
    print("")
    while True:
        new_lvl = str(input("PELAA TOISTA TASOA[1], TALLENNA JA LOPETA PELI [2]: "))
        if new_lvl == "1" or new_lvl == "2":
            break
    if new_lvl == "1":
        continue
    if new_lvl == "2":
        thanks()
        break
        # JA sitten tähän se tallennus funktio vai mitäs me keksittäis?
