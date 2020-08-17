import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "password123"
)
print(db)
# creating new database 
cursor = db.cursor()
cursor.execute("CREATE DATABASE workdb")
cursor.execute("SHOW DATABASES")
database = cursor.fetchall()
print(database)



