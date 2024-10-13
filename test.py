import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123password',
)

mycursor = mydb.cursor() # initalize cursor of database

mycursor.execute("CREATE DATABASE testdb")