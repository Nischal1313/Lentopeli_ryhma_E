import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla_database",
    user="root",
    password="rotallaonvaljaat",
    autocommit=True,
)

def suoritaKomento(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def tallennus(coins, pelaajan_kilometrit, location_atm, crimes_stopped, coin_used, user_name, continent):
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin.
    # continent arvo tarvii tallentaa vaan kerran, se pitää katsoa jos ei halua, että se joka kerralla tallentuu
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}', location = '{location_atm}',"
    sql += f" crimes_stopped = '{crimes_stopped}', coin_used = '{coin_used}', continent = '{continent}'"
    sql += f" where screen_name = '{user_name}'"
    suoritaKomento(sql)
    return

