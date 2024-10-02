from pprint import pprint

import psycopg2
from psycopg2.extras import RealDictCursor


connect = psycopg2.connect(database="local_db",
                           user="postgres", 
                           password="postgre",
                           host="localhost", 
                           port="5432")


def show_data(cursor):
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        print(f'Автомобиль {item["title"]} стоит {item["price"]}')

with connect:
    cursor = connect.cursor(cursor_factory=RealDictCursor)
    show_data(cursor)