import mysql.connector as mysql

def insertQ(tableName):
    return "INSERT INTO " + tableName + " VALUES (%s, %s)"

def selectQ(columnName,tableName):
    return "Select " + columnName + " from " + tableName

def delQ(tableName, command):
    return "DELETE FROM " + tableName + " where " + command

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "03232001",
    database = "abclass"
)

action = db.cursor()
query = "INSERT INTO hobby VALUES (%s, %s)"

values = [
    ("0001", "Ping Pong"),
    ("0002", "Gym"),
    ("3275", "Draw"),
    ("0007", "Read")
]

action.executemany(query, values)

value = [
    ("0001", "Basketball"),
    ("0002", "Volleyball"),
    ("0004", "Wrestling"),
    ("0007", "Track"),
    ("9000","no sport")
    ]
q = insertQ("SPORTS")

action.executemany(q,value)
db.commit()

selectQuery = selectQ("*", "sports")
action.execute(selectQuery)
selectData = action.fetchall()

for rows in selectData:
    print(rows)

delQuery = delQ("SPORTS","SPORTNAME = 'no sport'")
action.execute(delQuery)

db.commit()

selectQuery = selectQ("*","sports")
action.execute(selectQuery)
data = action.fetchall()

for rows in data:
    print(rows)
print()

selectQuery = selectQ("*","hobby")
action.execute(selectQuery)
data = action.fetchall()

for rows in data:
    print(rows)







