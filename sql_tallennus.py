import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="karkuteilla",
    user="root",
    password="rotallaonvaljaat",
    autocommit=True,
)

def execute_command(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def save(coins, pelaajan_kilometrit, location_atm, crimes_stopped, user_name, round_nro): # continent otettu pois, lisätään jos tarvitaan
    # parametreinä kaikki arvot, jotka tulee aaltosulkeiden väliin.
    sql = f"update game set coin = '{coins}', km_travelled = '{pelaajan_kilometrit}',"
    sql += f" location = (select iso_country from airport where name = '{location_atm}'),"
    sql += f" crimes_stopped = '{crimes_stopped}, round_nro = '{round_nro}' where screen_name = '{user_name}'"
    execute_command(sql)
    return

