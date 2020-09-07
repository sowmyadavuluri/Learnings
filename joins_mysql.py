import mysql.connector as mysql
c_db = mysql.connect(
     host = "localhost",
     user = "root",
     password ="password123",
     database ="cable_db"
)
cursor = c_db.cursor()
join_jobs = "SELECT customers.user_name AS user, jobs.employee_name AS e_name FROM customers INNER JOIN jobs ON customers.customer_id = jobs.job_id "

cursor.execute(join_jobs)

myresult = cursor.fetchall()

for x in  myresult:
  print(x)
