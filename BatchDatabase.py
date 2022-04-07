import mysql.connector as mysql


def readFromTextFile(fileName):
    with open(fileName, 'r') as file:
        return file.read().splitlines()

def insert(insertList,cursor,db):
    for i in range(len(insertList)):
        cursor.executemany("INSERT INTO Students VALUES(%s,%s,%s,%s,%s,%s)", insertList[i])
        db.commit()

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
    selQuery = "SELECT StudentID FROM Students"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    idList = []
    for sel in selectData:
        idList.append(int(str(sel).strip("(,)")))
    return idList


def schoolId(cursor):
    selQuery = "SELECT SchoolID FROM Schools"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    schoolList = []
    for sel in selectData:
        schoolList.append(int(str(sel).strip("(,)")))
    return schoolList


def hobbyId(cursor):
    selQuery = "SELECT HobbyID FROM Hobby"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    hobbyList = []
    for sel in selectData:
        hobbyList.append(int(str(sel).strip("(,)")))
    return hobbyList

def sportId(cursor):
    selQuery = "SELECT SportID FROM Sports"

    cursor.execute(selQuery)
    selectData = cursor.fetchall()
    sportList = []
    for sel in selectData:
        sportList.append(int(str(sel).strip("(,)")))
    return sportList


def manipulateFile(fileName,cursor,db):
    txtInput = readFromTextFile(fileName)
    insertList = []
    txtID = []
    for i in txtInput:
        insertList.append(i.split(" "))

    for i in range(len(insertList)):
        if len(insertList[i]) < 5 or len(insertList[i]) > 6:
            print("This input is not valid")
            insertList.remove(insertList[i])
            continue

        if insertList[i][2].isnumeric():
            insertList[i][2] = int(insertList[i][2])
            if insertList[i][2] in txtID:
                print("Error: ID already exists")
                insertList.remove(insertList[i])
            else:
                txtID.append(insertList[i][2])
        else:
            print("Error: " + insertList[i][2] + " is not a number")
            insertList.remove(insertList[i])

        if insertList[i][3].isnumeric():
            insertList[i][3] = int(insertList[i][3])
        else:
            print("Error: " + insertList[i][3] + " is not a number")
            insertList.remove(insertList[i])

        if insertList[i][4].isnumeric():
            insertList[i][4] = int(insertList[i][4])
        else:
            print("Error: " + insertList[i][4] + " is not a number")
            insertList.remove(insertList[i])

        if len(insertList[i]) == 6:
            if insertList[i][5].isnumeric():
                insertList[i][5] = int(insertList[i][5])
            else:
                print("Error: " + insertList[i][5] + " is not a number")
                insertList.remove(insertList[i])


    studId = idNums(cursor)
    schId = schoolId(cursor)
    hyID = hobbyId(cursor)
    spId = sportId(cursor)

    for i in insertList:
        if i[2] in studId:
            print("Error: " + str(i[2]) + " already exists")
            insertList.remove(i)
            continue

        if i[3] not in schId:
            add = input("School ID " + str(i[3]) + " does not exist. Would you like to add it? (y/n) ").lower()
            if add == "y":
                schoolName = input("Please enter the school name: ")
                schoolCity = input("Please enter the school city: ")
                schoolState = input("Please enter the school state: ")

                cursor.execute("INSERT INTO School VALUES(%s,%s,%s,%s)", (i[3],schoolName,schoolCity,schoolState))
                print("School added")
            else:
                print("School not added")
                insertList.remove(i)
                continue

        if i[4] not in hyID:
            hyAdd = input("Hobby ID " + str(i[4]) + " does not exist. Would you like to add it? (y/n) ").lower()
            if hyAdd == "y":
                hobbyName = input("Please enter the hobby name: ")

                cursor.execute("INSERT INTO Hobbies VALUES(%s,%s)", (i[4],hobbyName))
                print("Hobby added")
            else:
                print("Hobby not added")
                insertList.remove(i)
                continue

        if len(i) == 6:
            if i[5] not in spId:
                spAdd = input("Sport ID " + str(i[5]) + " does not exist. Would you like to add it? (y/n) ").lower()
                if spAdd == "y":
                    sportName = input("Please enter the sport name: ")

                    cursor.execute("INSERT INTO Sports VALUES(%s,%s)", (i[5],sportName))
                    print("Sport added")
                else:
                    print("Sport not added")
                    insertList.remove(i)
                    continue
    db.commit()
    return insertList

dataB = databaseConnect("localhost", "root", "03232001", "abclass")
action = dataB.cursor()

# TODO - send the error messages to a text file, format the inputs so that they look good on the command line. Make the main func.

