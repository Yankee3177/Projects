import Student
import Hobby
import School
import Sports

print("Welcome to the Database project command line interface!")

host = input("\nEnter the host name: ")
userName = input("Enter the user name: ")
passWord = input("Enter the password: ")
database = input("Enter the database name: ")
print()

while True:
    access = input("\nDo you want to access a certain table or exit the program? Enter 1 for table, "
                   "2 to exit: ")
    if access == "1":

        table = input("Enter the table you want to access:").lower()
        if table == "student":
            stud = Student.Student(host, userName, passWord, database)
            stud.mySql(stud.action, stud.db)
            continue

        elif table == "hobby":
            hob = Hobby.Hobby(host, userName, passWord, database)
            hob.mySql(hob.action, hob.db)
            continue

        elif table == "school":
            sch = School.School(host, userName, passWord, database)
            sch.mySql(sch.action, sch.db)
            continue

        elif table == "sports":
            sp = Sports.Sports(host, userName, passWord, database)
            sp.mySql(sp.action, sp.db)
            continue

        else:
            print("Invalid table")
            continue
    if access == "2":
        print("\nThank you for using the program!")
        break
    else:
        print("Invalid input")
        continue
