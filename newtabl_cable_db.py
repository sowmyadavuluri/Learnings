import mysql.connector as mysql
c_db = mysql.connect(
   host = "localhost",
   user ="root",
   password ="password123",
   database = "cable_db"
);
cursor = c_db.cursor()
cursor.execute("CREATE TABLE jobs(job_id INT PRIMARY KEY AUTO_INCREMENT , employee_name VARCHAR(255), user_name VARCHAR(255), contact_info VARCHAR(300) NULL)")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

