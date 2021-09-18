import mysql.connector

CONECTION = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='parcial_lg4',
    port=3306
)