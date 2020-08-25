#INSERTING DATA INTO TABLE(cable_jobs):
import mysql.connector as mysql
db = mysql.connect(
  host = "localhost",
  user = "root",
  password = "password123",
  db = "workdb"
)
cursor = db.cursor()

add_data =("INSERT INTO cable_jobs(job_id INT(5),s_p_name VARCHAR(255), user_name VARCHAR(255), salary_$ INT , users_id INT NULL ) VALUES(%s, %s, %s, %s, %s)")

info = [
       (1001,'yashwant','yash_24',10000,'manager'),
       (1002,'anusha','anu_28',9000,'senior_assistent_manager'),
       (1003,'karthik','karthik_06',8000,'assistent_manager'),
       (1004,'puja','puja_24',5000,'service_manager'),
       (1005,'aasha','aasha_22',4500,'sales_manager')
]
cursor.executemany(add_data,info)

db.commit()
print(cursor.rowcount,"record inserted.")

