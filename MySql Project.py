import mysql.connector as mysql


def insertQ(tableName, cursor):
    itemList = insertItems(tableName,cursor)
    value = " VALUES (%s"
    for i in range(1, len(itemList[0])):
        value += ",%s"
    value += ")"
    q = "INSERT INTO " + tableName + value
    cursor.executemany(q, itemList)
    print("Inserted")


def selectQ(columnName, tableName, cursor, command=None):
    if command is None:
        select = "Select " + columnName + " from " + tableName
    else:
        select = "Select " + columnName + " from " + tableName + " where " + command

    cursor.execute(select)
    selectData = cursor.fetchall()

    print()

    for selectRow in selectData:
        print (str((selectRow)).strip("(',)").replace("'",""))

    print()
def delQ(tableName, cursor, command):
    delQuery = "DELETE FROM " + tableName + " where " + command
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


def insertItems(table,cursor):
    item = []
    cont = True
    print()
    print("These are the columns in the table: ")
    col = getColumns(cursor, table)
    for column in col:
        print(column[0], "type =", str(column[1]).strip("b'").replace("char", "Characters").replace("int", "Number"))
    print()
    while cont:
        inItem = list(input("Enter the first entry for the table, use a space to separate each individual information: ").split(" "))
        item.append(inItem)
        done = input("Are you done with all the items? Enter yes to finish with all the items. ").lower()
        if done == "yes":
            cont = False

    return item

def getColumns(cursor, tableName):
    q = "SHOW COLUMNS FROM " + tableName
    cursor.execute(q)
    columns = cursor.fetchall()
    return columns

def getTables(cursor):
    q = "SHOW TABLES"
    cursor.execute(q)
    tables = cursor.fetchall()
    return tables

def mySql(cursor,db):
    commandList = ["insert", "select", "delete", "exit"]
    while True:
        print("The following are the commands you can use: " + str(commandList).strip('[]').replace("'",""))
        command = input("Enter a command: ").lower()

        if command == "insert":
            tableName = input("Enter the table name: ")
            insertQ(tableName, cursor)
            db.commit()

        elif command == "select":
            tableName = input("Enter the table name: ")

            print("\nThese are the columns in the table: ")
            col = getColumns(cursor, tableName)
            for column in col:
                print(column[0])
            print()
            columnName = input("Enter the column name or names, you can use * to select all of the columns.\nIf you are "
                               "using multiple columns put the name of the table followed by a period before you"
                               " enter the name of the column: ")


            specificSearch = input("Would you like to search for specific information? Enter yes or no: ").lower()
            if specificSearch == "yes":
                command = input("Enter the command: ")
                selectQ(columnName, tableName, cursor, command)
            else:
                selectQ(columnName, tableName, cursor)

        elif command == "delete":
            tableName = input("Enter the table name for the place of the item you want to delete: ")

            print("\nThese are the entries in the table: ")
            str(selectQ("*", tableName, cursor)).replace("'","")
            print()

            print("\nThese are the columns in the table: ")
            col = getColumns(cursor, tableName)
            for column in col:
                print(column[0])
            print()
            cont = input("Are you sure you want to delete an entry? Enter yes or no: ").lower()
            if cont == "no":
                continue
            command = input("Enter the description of the item followed by an equal sign and then\n the value of that "
                            "item, if the item is a group of "
                            "characters add quotation marks to name of the item: ")
            print(command)
            delQ(tableName, cursor, command)
            db.commit()
            print("Deleted\n")

        elif command == "exit":
            print("\nThank you for using the program")
            break

        else:
            print("Invalid command\n")

def main():
    print("Welcome to the database project, please enter the following information to connect to the database. I will "
          "not store your password.\n")

    host = input("Enter the host name: ")
    userName = input("Enter the user name: ")
    passWord = input("Enter the password: ")
    database = input("Enter the database name: ")
    print()
    dataB = databaseConnect(host, userName, passWord, database)
    action = dataB.cursor()
    t = getTables(action)
    print("These are the tables in this database: ")
    for i, item in enumerate(t):
        print(i + 1, item[0])
    print()
    mySql(action, dataB)

main()






