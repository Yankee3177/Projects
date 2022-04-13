import mysql.connector as mysql


class Student:
    hostt = ""
    user = ""
    passWord = ""
    db = ""

    def __init__(self,host,userName,password,database):
        self.hostt = host
        self.user = userName
        self.passWord = password
        self.db = database

        self.db = mysql.connect(
            host=self.hostt,
            user=self.user,
            passwd=self.passWord,
            database=self.db
        )
        self.action = self.db.cursor()



    def insertQ(self,tableName, cursor):
        itemList = self.insertItems(tableName, cursor)
        value = " VALUES (%s"
        for i in range(1, len(itemList[0])):
            value += ",%s"
        value += ")"
        q = "INSERT INTO " + tableName + value
        cursor.executemany(q, itemList)
        print("Inserted")

    def selectQ(self,columnName, tableName, cursor, command=None):
        if command is None:
            select = "Select " + columnName + " from " + tableName
        else:
            select = "Select " + columnName + " from " + tableName + " where " + command

        cursor.execute(select)
        selectData = cursor.fetchall()

        print()

        for selectRow in selectData:
            print(str((selectRow)).strip("(',)").replace("'", ""))

        print()

    def delQ(self,tableName, cursor, command):
        delQuery = "DELETE FROM " + tableName + " where " + command
        cursor.execute(delQuery)

    def insertItems(self,table, cursor):
        item = []
        cont = True
        print()
        print("These are the columns in the table: ")
        col = self.getColumns(cursor, table)
        for column in col:
            print(column[0], "type =",
                  str(column[1]).strip("b'").replace("char", "Characters").replace("int", "Number"))
        print()
        while cont:
            inItem = list(input(
                "Enter the first entry for the table, use a space to separate each individual information: ").split(
                " "))
            item.append(inItem)
            done = input("Are you done with all the items? Enter yes to finish with all the items. ").lower()
            if done == "yes":
                cont = False

        return item

    def getColumns(self,cursor, tableName):
        q = "SHOW COLUMNS FROM " + tableName
        cursor.execute(q)
        columns = cursor.fetchall()
        return columns


    def mySql(self,cursor, db):
        commandList = ["insert", "select", "delete", "exit"]
        while True:
            print("The following are the commands you can use: " + str(commandList).strip('[]').replace("'", ""))
            command = input("Enter a command: ").lower()

            if command == "insert":
                tableName = "STUDENTS"
                self.insertQ(tableName, cursor)
                db.commit()

            elif command == "select":
                tableName = "STUDENTS"

                print("\nThese are the columns in the table: ")
                col = self.getColumns(cursor, tableName)
                for column in col:
                    print(column[0])
                print()
                columnName = input(
                    "Enter the column name or names, you can use * to select all of the columns.\nIf you are "
                    "using multiple columns put the name of the table followed by a period before you"
                    " enter the name of the column: ")

                specificSearch = input("Would you like to search for specific information? Enter yes or no: ").lower()
                if specificSearch == "yes":
                    command = input("Enter the command: ")
                    self.selectQ(columnName, tableName, cursor, command)
                else:
                    self.selectQ(columnName, tableName, cursor)

            elif command == "delete":
                tableName = "STUDENTS"

                print("\nThese are the entries in the table: ")
                str(self.selectQ("*", tableName, cursor)).replace("'", "")
                print()

                print("\nThese are the columns in the table: ")
                col = self.getColumns(cursor, tableName)
                for column in col:
                    print(column[0])
                print()
                cont = input("Are you sure you want to delete an entry? Enter yes or no: ").lower()
                if cont == "no":
                    continue
                command = input(
                    "Enter the description of the item followed by an equal sign and then\n the value of that "
                    "item, if the item is a group of "
                    "characters add quotation marks to name of the item: ")
                print(command)
                self.delQ(tableName, cursor, command)
                db.commit()
                print("Deleted\n")

            elif command == "exit":
                print("\nThank you for using the program")
                break

            else:
                print("Invalid command\n")