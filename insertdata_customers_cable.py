#INSERTING DATA INTO cable-customers TABLE:cursor = c_db.cursor()
#INSERTING DATA INTO TABLE(cable_jobs):
import mysql.connector as mysql
c_db = mysql.connect(
  host = "localhost",
  user = "root",
  password = "password123",
  db = "cable_db"
)


#SELECT  FROM cable_db.customers;
cursor = c_db.cursor()

customers_data = "INSERT INTO customers(customer_id,customer_name,user_name,contact_info) VALUES(%s,%s,%s,%s)"

details = [
(1,'vasu','vasu_09','9010101010'),(2,'kranthi','kranthi_06','9020202020'),(3,'varshi','varshi_24','9030303030'),(4,'sowmya','sowmya_15','904040404'),(5,'anitha','anitha_01','9050505050'),(6,'nitish','nitish_15','9060606060'),(7,'pandu','pandu_24','9070707070')
];
cursor.executemany(customers_data,details)

c_db.commit()
print(cursor.rowcount,"record(s) inserted.")

