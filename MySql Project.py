import mysql.connector as mysql


def insertQ(tableName, cursor):
    itemList = insertItems()
    value = " VALUES (%s"
    for i in range(1,len(itemList[0])):
        value += ",%s"
    value += ")"
    q = "INSERT INTO " + tableName + value
    cursor.executemany(q, itemList)


def selectQ(columnName, tableName, cursor, command=None):
    if command is None:
        select = "Select " + columnName + " from " + tableName
    else:
        select = "Select " + columnName + " from " + tableName + " where " + command

    cursor.execute(select)
    selectData = cursor.fetchall()

    for selectRow in selectData:
        print(selectRow)


def delQ(tableName, cursor, command):
    delQuery =  "DELETE FROM " + tableName + " where " + command
    cursor.execute(delQuery)


def databaseConnect(hostt, userName, passWord, databasee=None):
    if databasee is None:
        dbase = mysql.connect(
            host=hostt,
            user=userName,
            passwd=passWord,
        )
    else:
        dbase = mysql.connect(
            host=hostt,
            user=userName,
            passwd=passWord,
            database=databasee
        )
    return dbase


def insertItems():
    item = []
    cont = True
    while cont:
        inItem = list(input("Enter items separated by spaces: ").split(" "))
        item.append(inItem)
        done = input("Are you done with all the items? Enter yes to finish with all the items. ").lower()
        if done == "yes":
            cont = False

    return item


db = databaseConnect("localhost", "root", "03232001", "junk")
action = db.cursor()

db.commit()

# TODO use all the created functions to make the actual commandline. Remember to make it as easy as possible
#   so a person that has just the basic knowledge of what a database is knows how to do it.



# action.executemany(query, values)
#
# value = [
#     ("0001", "Basketball"),
#     ("0002", "Volleyball"),
#     ("0004", "Wrestling"),
#     ("0007", "Track"),
#     ("9000", "no sport")
# ]

# delQuery = delQ("SPORTS", "SPORTNAME = 'no sport'")
# action.execute(delQuery)

# db.commit()

