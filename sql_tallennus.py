import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla_database",
    user="root",
    password="rotallaonvaljaat",
    autocommit=True,
)

def suoritaHaku(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


def tallennus(coins, pelaajan_kilometrit, location_atm, crimes_stopped, coin_used, user_name):
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}',"
    sql += f" location = '{location_atm}', crimes_stopped = '{crimes_stopped}', coin_used = '{coin_used}'"
    sql += f" where screen_name = '{user_name}'"
    suoritaHaku(sql)  # pitääkö tehdä oma, kun ei tarvitse hakea mitään dataa?
    # kursori = yhteys.cursor()
    # kursori.execute(sql)
    return  # ei kai tarvii palauttaa mitään?

