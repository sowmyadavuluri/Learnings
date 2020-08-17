import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "password123",
    db = "workdb"
)
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)
#To select first row
cursor.execute("SELECT name, user_name FROM users")
# use fetchone() for first row
first_result = cursor.fetchone()
print(first_result)

