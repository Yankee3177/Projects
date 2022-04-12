import mysql.connector as mysql


def readFromTextFile(fileName):
    with open(fileName, 'r') as file:
        return file.read().splitlines()


def insert(insertList, cursor, db):
    for i in range(len(insertList)):
        if len(insertList[i]) == 5:
            insertList[i].append(None)

        q = """INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(q, insertList[i])

        db.commit()
        print("\nInsert complete")


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


def idNums(cursor):
    selQuery = "SELECT StudentID FROM STUDENTS"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    idList = []
    for sel in selectData:
        idList.append(int(str(sel).strip("(,)")))
    return idList


def schoolId(cursor):
    selQuery = "SELECT SchoolsID FROM SCHOOL"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    schoolList = []
    for sel in selectData:
        schoolList.append(int(str(sel).strip("(,)")))
    return schoolList


def hobbyId(cursor):
    selQuery = "SELECT HobbyID FROM HOBBY"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    hobbyList = []
    for sel in selectData:
        hobbyList.append(int(str(sel).strip("(,)")))
    return hobbyList


def sportId(cursor):
    selQuery = "SELECT SportID FROM SPORTS"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    sportList = []
    for sel in selectData:
        sportList.append(int(str(sel).strip("(,)")))
    return sportList


def manipulateFile(fileName, cursor, db):
    txtInput = readFromTextFile(fileName)
    insertList = []
    txtID = []
    errorList = []
    for i in txtInput:
        insertList.append(i.split(" "))

    for i in range(len(insertList)):
        if len(insertList[i]) < 5 or len(insertList[i]) > 6:
            errorList.append("Error: " + str(insertList[i]) + " is not a valid input")
            insertList.remove(insertList[i])
            continue

        if insertList[i][2].isnumeric():
            insertList[i][2] = int(insertList[i][2])
            if insertList[i][2] in txtID:
                errorList.append("Error: " + str(insertList[i]) + " student id is duplicated.")
                insertList.remove(insertList[i])
                continue
            else:
                txtID.append(insertList[i][2])
        else:
            errorList.append(
                "Error: " + str(insertList[i]) + " student id is not a number which means the format isn't correct")
            insertList.remove(insertList[i])
            continue

        if insertList[i][3].isnumeric():
            insertList[i][3] = int(insertList[i][3])
        else:
            errorList.append(
                "Error: " + str(insertList[i]) + " school id is not a number which means the format isn't correct")
            insertList.remove(insertList[i])
            continue

        if insertList[i][4].isnumeric():
            insertList[i][4] = int(insertList[i][4])
        else:
            errorList.append(
                "Error: " + str(insertList[i]) + " hobby id is not a number which means the format isn't correct")
            insertList.remove(insertList[i])
            continue

        if len(insertList[i]) == 6:
            if insertList[i][5].isnumeric():
                insertList[i][5] = int(insertList[i][5])
            else:
                errorList.append(
                    "Error: " + str(insertList[i]) + " sports id is not a number which means the format isn't correct")
                insertList.remove(insertList[i])

    studId = idNums(cursor)
    schId = schoolId(cursor)
    hyID = hobbyId(cursor)
    spId = sportId(cursor)

    for i in range(len(insertList)):
        if insertList[i][2] in studId:
            errorList.append("Error: " + str(insertList[i][0]) + " student id is duplicated")
            insertList.remove(insertList[i])
            continue

        if insertList[i][3] not in schId:
            add = input(
                "School ID " + str(insertList[i][3]) + " does not exist. Would you like to add it? (y/n) ").lower()
            if add == "y":
                schoolName = input("\nPlease enter the school name: ")
                schoolCity = input("Please enter the school city: ")
                schoolState = input("Please enter the school state: ")

                cursor.execute("INSERT INTO SCHOOL VALUES(%s,%s,%s,%s)",
                               (insertList[i][3], schoolName, schoolCity, schoolState))
                print("School added\n")
            else:
                errorList.append(
                    "Error: " + str(insertList[i][0]) + " school not added, so school does not exist in database.")
                insertList.remove(insertList[i])
                continue

        if insertList[i][4] not in hyID:
            hyAdd = input("Hobby ID " + str(i[4]) + " does not exist. Would you like to add it? (y/n) ").lower()
            if hyAdd == "y":
                hobbyName = input("\nPlease enter the hobby name: ")

                cursor.execute("INSERT INTO HOBBIES VALUES(%s,%s)", (insertList[i][4], hobbyName))
                print("Hobby added\n")
            else:
                errorList.append(
                    "Error: " + str(insertList[i][0]) + " hobby not added, so hobby does not exist in database.")
                insertList.remove(insertList[i])
                continue

        if len(insertList[i]) == 6:
            if insertList[i][5] not in spId:
                spAdd = input(
                    "Sport ID " + str(insertList[i][5]) + " does not exist. Would you like to add it? (y/n) ").lower()
                if spAdd == "y":
                    sportName = input("Please enter the sport name: ")

                    cursor.execute("INSERT INTO SPORTS VALUES(%s,%s)", (insertList[i][5], sportName))
                    print("Sport added\n")
                else:
                    errorList.append(
                        "Error: " + str(insertList[i][0]) + " sport not added, so sport does not exist in database.")
                    insertList.remove(insertList[i])

    db.commit()
    return insertList, errorList


def writeToFile(errorList):
    file = open("errors.txt", "w")
    file.write("\n".join(errorList))
    file.close()


def main():
    host = input("Enter the host name: ")
    userName = input("Enter the user name: ")
    passWord = input("Enter the password: ")
    database = input("Enter the database name: ")
    print()
    dataB = databaseConnect(host, userName, passWord, database)
    action = dataB.cursor()

    file = input("\nEnter name of text file: ")
    file += ".txt"
    inStuds, errList = manipulateFile(file, action, dataB)
    insert(inStuds, action, dataB)

    if len(errList) > 0:
        writeToFile(errList)
        print("\nErrors written to errors.txt")


main()
#Format for txt file is firstName lastName studentid schoolid hobbyid sportid