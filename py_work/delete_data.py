import mysql.connector as mysql
db = mysql.connect(
   host = "localhost",
   user = "root",
   password = "password123",
   db = "workdb"
)
cursor = db.cursor()
delete =  "DELETE FROM users WHERE name = 'sowmya'"
cursor.execute(delete)
db.commit()
print(cursor.rowcount,"record(s) deleted")

