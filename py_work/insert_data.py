#INSERTING DATA INTO TABLE:
import mysql.connector as mysql
db = mysql.connect(
  host = "localhost",
  user = "root",
  password = "password123",
  db = "workdb"
)
cursor = db.cursor()

add_db = "INSERT INTO users(name , user_name) VALUES(%s, %s)"
#val = ("sowmya","sowmya_15")
#Inserting Multiple Values
val = [
       ('sowmya','sowmya_15'),
       ('vasu','vasu_09'),
       ('kranthi','kranthi_06'),
       ('varshi','varshi_24')
]
#execute() is used for single user data insertion.
#executemany() is used for inserting multiple values.
cursor.executemany(add_db,val)

db.commit()
print(cursor.rowcount,"record inserted.")


