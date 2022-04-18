from tkinter import *
import mysql.connector as mysql


def submit():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="03232001",
        database="abclass"
    )
    action = db.cursor()
    q = """INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s, %s)"""

    action.execute(q, [fName.get(), lName.get(), studId.get(), schoolId.get(), hobbyId.get(), sportId.get()])
    db.commit()
    db.close()

    fName.delete(0, END)
    lName.delete(0, END)
    studId.delete(0, END)
    schoolId.delete(0, END)
    hobbyId.delete(0, END)
    sportId.delete(0, END)


def query():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="03232001",
        database="abclass"
    )
    action = db.cursor()
    q = """SELECT * FROM STUDENTS"""
    action.execute(q)
    result = action.fetchall()
    #db.close()

    records = ""
    for row in result:
        records += str(row) + "\n"

    query_label = Label(main, text=records)
    query_label.grid(row=12, column=0, columnspan=2)


main = Tk()

main.title("SQL Test")
main.geometry("400x400")

fName = Entry(main, width=30)
fName.grid(row=0, column=1, padx=20, pady=(10, 0))
lName = Entry(main, width=30)
lName.grid(row=1, column=1)
studId = Entry(main, width=30)
studId.grid(row=2, column=1)
schoolId = Entry(main, width=30)
schoolId.grid(row=3, column=1)
hobbyId = Entry(main, width=30)
hobbyId.grid(row=4, column=1)
sportId = Entry(main, width=30)
sportId.grid(row=5, column=1)

# Create Text Box Labels
fNameLabel = Label(main, text="First Name")
fNameLabel.grid(row=0, column=0, pady=(10, 0))
lNameLabel = Label(main, text="Last Name")
lNameLabel.grid(row=1, column=0)
studIdLabel = Label(main, text="Student ID")
studIdLabel.grid(row=2, column=0)
schoolIdLabel = Label(main, text="School ID")
schoolIdLabel.grid(row=3, column=0)
hobbyIdLabel = Label(main, text="Hobby ID")
hobbyIdLabel.grid(row=4, column=0)
sportIdLabel = Label(main, text="Sport ID")
sportIdLabel.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(main, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(main, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

main.mainloop()
