import mysql.connector

# create database connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1578'
)

# prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE customers")
print("database created!")