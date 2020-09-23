from influxdb import InfluxDBClient
import mysql.connector as mysql

host = 'localhost'
port = 8086
db_name = 'pyexample'
user = 'sowmya'

# Connect to client
client = InfluxDBClient('localhost', 8086)

# Drop DB
client.drop_database(db_name);

# Create DB
print("Create database: ", db_name)
client.create_database(db_name)

# Get DB
get_db = client.get_list_database()
print("Get list database", get_db)

# Switch DB
client.switch_database(db_name)

# Insert DB
json_dy = [
{
    "measurement": "brushEvents",
    "tags": {
        "user":"sowmya",
        "brushId": "8143410660"
    },
    "time": "2020-09-11T8:01:00Z",
    "fields": {
        "duration": 127
    }
},
{
    "measurement": "brushEvents",
    "tags": {
        "user":"sowmya",
        "brushId": "8143410660"
    },
    "time": "2020-09-12T8:02:00Z",
    "fields": {
        "duration":132
     }
},
{
    "measurement": "brushEvents",
    "tags": {
        "user":"sowmya",
        "brushId": "8143410660"
    },
    "time": "2020-09-13T8:04:00Z",
    "fields": {
        "duration":129
     }
}
]

print("write points: {0}".format(json_dy))
client.write_points(json_dy)

results = client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" GROUP BY *')

print("Result: {0}".format(results))

points = results.get_points(tags ={'user':'sowmya'})

# Last value
results1 = client.query('SELECT LAST("duration") FROM "pyexample"."autogen"."brushEvents" ')

print("Result1: {0}".format(results1))

# Store output of Influxdb into local list
data = [[], [], []]
lp = 0
for point in points:
  lp = lp+1
  print("Time: %s, Duration: %i" %(point['time'],point['duration']))
  data[lp-1] = [str(point['time']), str(point['duration'])]
print("Influx2MySQL list", data)

# data [0][1]

# Start inserting local list into MYSQL
print("Inserting into mysql from influxdb")
c_db = mysql.connect(
   host = "localhost",
   user ="root",
   password ="password123",
   database = "workdb"
);
cursor = c_db.cursor()
'''cursor.execute("CREATE TABLE brushevents(user VARCHAR(220), brush_id VARCHAR(255), burshing_time VARCHAR(255), duration VARCHAR(255) NULL)")
cursor.execute("SHOW TABLES")'''

influx_data = "INSERT INTO brushevents(user,brush_id,burshing_time,duration) VALUES(%s,%s,%s,%s)"

details = [
('sowmya','8143','1','2')
];

cursor.executemany(influx_data,details)

c_db.commit()
print(cursor.rowcount,"record(s) inserted.")

