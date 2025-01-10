import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="58.72.151.123",
        user="human2",
        password="Passw0rd!123",
        database="mydb"
    )
