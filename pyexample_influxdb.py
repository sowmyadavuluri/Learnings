from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port = 8086)

print("Create database: "+ 'pyexample')
client.create_database('pyexample')


client.get_list_database()
[{'name': 'telegraf'}, {'name': '_internal'}, {'name': 'pyexample'}]

print("switch user: "+"sowmya")
client.switch_database('pyexample')


json_dy = [
     {
         "measurement": "brushEvents",
         "tags": {
             "user":"sowmya",
             "bushID": "8143410660"
         },
         "time": "2020-09-11T8:04:00Z",
         "fields":{
              "duration": 127
         }
     },
     {
         "measurement": "brushEvents",
         "tags": {
             "user":"sowmya",
             "brushId": "8143410660"
         },
         "time":"2020-09-11T8:04:00Z",
         "fields":{
             "duration":132
          }
     },
     {
         "measurement": "brushEvents",
         "tags": {
             "user":"sowmya",
             "brushId": "8143410660"
         },
         "time":"2020-09-11T8:04:00Z",
         "fields":{
             "duration":129
          }
     }
]

print("write points: {0}".format(json_dy))
client.write_points(json_dy)
True

results = client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')

print("Result: {0}".format(results))

results.raw
{"statement_id": 0, "series": [{"name": "brushEvents", "tags": {"user": "sowmya"}, "columns": ["time", "duration"], "values": [["2020-09-11T8:04:00Z", 127], ["2020-09-11T8:04:00Z", 132], ["2020-09-11T8:04:00Z", 129]]}]}

points = results.get_points(tags ={'user':'sowmya'})

for point in points:
  print("Time: %s, Duration: %i" %(point['time'],point['duration']))




















