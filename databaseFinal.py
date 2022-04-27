from tkinter import *
from tkinter import messagebox
from tkinter import font

import mysql.connector as mysql
from numpy.core.defchararray import isdigit, isalpha


def connect():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    if dbase.is_connected():
        messagebox.showinfo(title="Success", message="You are connected to the database")

        nextStepLabel = Label(main, text="What would you like to do with the database", bg='#FFF0F5')
        nextStepLabel.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50, sticky=W)
        nextStepLabel.config(font=fontt)

        insertButton = Button(main, text="Insert", command=insert, bg='#FFF0F5')
        deleteButton = Button(main, text="Delete", command=delete, bg='#FFF0F5')
        exitButton = Button(main, text="Exit", command=main.destroy, bg='#FFF0F5')

        insertButton.grid(row=8, column=0, pady=10, padx=10, ipadx=50, sticky=W)
        deleteButton.grid(row=8, column=1, pady=10, padx=10, ipadx=50, sticky=W)
        exitButton.grid(row=9, column=0, pady=10, padx=10, ipadx=55, sticky=W)


def insert():
    main.withdraw()
    insertWindow = Toplevel(main)
    insertWindow.title("Insert into database")

    pickLabel = Label(insertWindow, text="Pick a table to insert into", bg='#FFF0F5')
    studentButton = Button(insertWindow, text="Student", command=student, bg='#FFF0F5')
    hobbyButton = Button(insertWindow, text="Hobby", command=hobby, bg='#FFF0F5')
    schoolButton = Button(insertWindow, text="School", command=school, bg='#FFF0F5')
    sportButton = Button(insertWindow, text="Sport", command=sport, bg='#FFF0F5')
    exitButton = Button(insertWindow, text="Exit", command=lambda: openWindow(insertWindow), bg='#FFF0F5')

    pickLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=50, sticky=W)
    studentButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)
    hobbyButton.grid(row=1, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    schoolButton.grid(row=2, column=0, pady=10, padx=10, ipadx=50, sticky=W)
    sportButton.grid(row=2, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    exitButton.grid(row=3, column=0, pady=10, padx=10, ipadx=55, sticky=W)


def openWindow(newWin):
    main.deiconify()
    newWin.destroy()


def student():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    studInsertWindow = Toplevel(main)
    studInsertWindow.title("Insert into Student")

    fName = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    fName['font'] = fontt
    fName.grid(row=0, column=1, padx=20, pady=(10, 0))
    lName = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    lName['font'] = fontt
    lName.grid(row=1, column=1)
    studId = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    studId['font'] = fontt
    studId.grid(row=2, column=1)
    schoolId = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    schoolId['font'] = fontt
    schoolId.grid(row=3, column=1)
    hobbyId = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    hobbyId['font'] = fontt
    hobbyId.grid(row=4, column=1)
    sportId = Entry(studInsertWindow, width=30, bg='#FFF0F5')
    sportId['font'] = fontt
    sportId.insert(END, 'None')
    sportId.grid(row=5, column=1)

    fNameLabel = Label(studInsertWindow, text="First Name", bg='#FFF0F5')
    fNameLabel['font'] = fontt
    fNameLabel.grid(row=0, column=0, pady=(10, 0))
    lNameLabel = Label(studInsertWindow, text="Last Name", bg='#FFF0F5')
    lNameLabel['font'] = fontt
    lNameLabel.grid(row=1, column=0)
    studIdLabel = Label(studInsertWindow, text="Student ID", bg='#FFF0F5')
    studIdLabel['font'] = fontt
    studIdLabel.grid(row=2, column=0)
    schoolIdLabel = Label(studInsertWindow, text="School ID", bg='#FFF0F5')
    schoolIdLabel['font'] = fontt
    schoolIdLabel.grid(row=3, column=0)
    hobbyIdLabel = Label(studInsertWindow, text="Hobby ID", bg='#FFF0F5')
    hobbyIdLabel['font'] = fontt
    hobbyIdLabel.grid(row=4, column=0)
    sportIdLabel = Label(studInsertWindow, text="Sport ID", bg='#FFF0F5')
    sportIdLabel['font'] = fontt
    sportIdLabel.grid(row=5, column=0)

    submit_btn = Button(studInsertWindow, text="Insert To Database", command=lambda: studQ(studId, schoolId, hobbyId,
                                                                                           sportId, fName, lName))
    submit_btn['font'] = fontt
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    update_btn = Button(studInsertWindow, text="Update", command=lambda: selQuery("STUDENTS", studInsertWindow))
    update_btn['font'] = fontt
    update_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    selQuery("STUDENTS", studInsertWindow)
    studInsertWindow.mainloop()


def studQ(studId, schoolId, hobbyId, sportId, fName, lName):
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="03232001",
        database="abclass"
    )
    action = db.cursor()

    q = """INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s, %s)"""
    if isdigit(studId.get()) and isdigit(schoolId.get()) and isdigit(hobbyId.get()) and (
            isdigit(sportId.get()) or sportId.get() == "None"):
        if sportId.get() == "None":
            sportEntry = None
            action.execute(q, [fName.get(), lName.get(), studId.get(), schoolId.get(), hobbyId.get(), sportEntry])
        else:
            action.execute(q, [fName.get(), lName.get(), studId.get(), schoolId.get(), hobbyId.get(), sportId.get()])
        db.commit()
        db.close()
        messagebox.showinfo(title="Success", message="Record Inserted")
    else:
        messagebox.showerror(title="Error", message="Invalid Input")

    fName.delete(0, END)
    lName.delete(0, END)
    studId.delete(0, END)
    schoolId.delete(0, END)
    hobbyId.delete(0, END)
    sportId.delete(0, END)
    sportId.insert(END, 'None')


def hobby():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    hobbyInsertWindow = Toplevel(main)
    hobbyInsertWindow.title("Insert into the hobby table")

    hobbyId = Entry(hobbyInsertWindow, width=30, bg='#FFF0F5')
    hobbyId['font'] = fontt
    hobbyId.grid(row=0, column=1, padx=20, pady=(10, 0))
    hobbyName = Entry(hobbyInsertWindow, width=30, bg='#FFF0F5')
    hobbyName['font'] = fontt
    hobbyName.grid(row=1, column=1)

    hobbyIdLabel = Label(hobbyInsertWindow, text="Hobby ID", bg='#FFF0F5')
    hobbyIdLabel['font'] = fontt
    hobbyIdLabel.grid(row=0, column=0, pady=(10, 0))
    hobbyNameLabel = Label(hobbyInsertWindow, text="Hobby Name", bg='#FFF0F5')
    hobbyNameLabel['font'] = fontt
    hobbyNameLabel.grid(row=1, column=0)

    submit_btn = Button(hobbyInsertWindow, text="Insert To Database",
                        command=lambda: hobbyQ(hobbyId, hobbyName, dbase))
    submit_btn['font'] = fontt
    submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    update_btn = Button(hobbyInsertWindow, text="Update", command=lambda: selQuery("HOBBY", hobbyInsertWindow))
    update_btn['font'] = fontt
    update_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    selQuery("HOBBY", hobbyInsertWindow)
    hobbyInsertWindow.mainloop()


def hobbyQ(hobbyId, hobbyName, db):
    q = """INSERT INTO HOBBY VALUES (%s, %s)"""

    if isdigit(hobbyId.get()) and isalpha(hobbyName.get()):
        db.cursor().execute(q, [hobbyId.get(), hobbyName.get()])
        db.commit()
        db.close()
        messagebox.showinfo(title="Success", message="Record Inserted")
    else:
        messagebox.showerror(title="Error", message="Invalid Input")

    hobbyId.delete(0, END)
    hobbyName.delete(0, END)


def school():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    schoolInsertWindow = Toplevel(main)
    schoolInsertWindow.title("Insert into the school table")

    schoolId = Entry(schoolInsertWindow, width=30, bg='#FFF0F5')
    schoolId['font'] = fontt
    schoolId.grid(row=0, column=1, padx=20, pady=(10, 0))
    schoolName = Entry(schoolInsertWindow, width=30, bg='#FFF0F5')
    schoolName['font'] = fontt
    schoolName.grid(row=1, column=1)
    schoolCity = Entry(schoolInsertWindow, width=30, bg='#FFF0F5')
    schoolCity['font'] = fontt
    schoolCity.grid(row=2, column=1)
    schoolState = Entry(schoolInsertWindow, width=30, bg='#FFF0F5')
    schoolState['font'] = fontt
    schoolState.grid(row=3, column=1)

    schoolIdLabel = Label(schoolInsertWindow, text="School ID", bg='#FFF0F5')
    schoolIdLabel['font'] = fontt
    schoolIdLabel.grid(row=0, column=0, pady=(10, 0))
    schoolNameLabel = Label(schoolInsertWindow, text="School Name", bg='#FFF0F5')
    schoolNameLabel['font'] = fontt
    schoolNameLabel.grid(row=1, column=0)
    schoolCityLabel = Label(schoolInsertWindow, text="City", bg='#FFF0F5')
    schoolCityLabel['font'] = fontt
    schoolCityLabel.grid(row=2, column=0)
    schoolStateLabel = Label(schoolInsertWindow, text="State", bg='#FFF0F5')
    schoolStateLabel['font'] = fontt
    schoolStateLabel.grid(row=3, column=0)

    submit_btn = Button(schoolInsertWindow, text="Insert To Database",
                        command=lambda: schoolQ(schoolId, schoolName,schoolCity,schoolState, dbase))
    submit_btn['font'] = fontt
    submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    update_btn = Button(schoolInsertWindow, text="Update", command=lambda: selQuery("SCHOOL", schoolInsertWindow))
    update_btn['font'] = fontt
    update_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    selQuery("SCHOOL", schoolInsertWindow)
    schoolInsertWindow.mainloop()


def schoolQ(schoolId, schoolName, city, state, db):
    q = """INSERT INTO SCHOOL VALUES (%s, %s, %s, %s)"""

    if isdigit(schoolId.get()) and isalpha(schoolName.get()) and isalpha(city.get()) and isalpha(state.get()):
        db.cursor().execute(q, [schoolId.get(), schoolName.get(), city.get(), state.get()])
        db.commit()
        db.close()
        messagebox.showinfo(title="Success", message="Record Inserted")
    else:
        messagebox.showerror(title="Error", message="Invalid Input")

    schoolId.delete(0, END)
    schoolName.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)


def sport():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    sportInsertWindow = Toplevel(main)
    sportInsertWindow.title("Insert into the sports table")

    sportId = Entry(sportInsertWindow, width=30, bg='#FFF0F5')
    sportId['font'] = fontt
    sportId.grid(row=0, column=1, padx=20, pady=(10, 0))
    sportName = Entry(sportInsertWindow, width=30, bg='#FFF0F5')
    sportName['font'] = fontt
    sportName.grid(row=1, column=1)

    sportIdLabel = Label(sportInsertWindow, text="Sport ID", bg='#FFF0F5')
    sportIdLabel['font'] = fontt
    sportIdLabel.grid(row=0, column=0, pady=(10, 0))
    sportNameLabel = Label(sportInsertWindow, text="Sport Name", bg='#FFF0F5')
    sportNameLabel['font'] = fontt
    sportNameLabel.grid(row=1, column=0)

    submit_btn = Button(sportInsertWindow, text="Insert To Database",
                        command=lambda: sportQ(sportId, sportName, dbase))
    submit_btn['font'] = fontt
    submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    update_btn = Button(sportInsertWindow, text="Update", command=lambda: selQuery("SPORTS", sportInsertWindow))
    update_btn['font'] = fontt
    update_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    selQuery("SPORTS", sportInsertWindow)
    sportInsertWindow.mainloop()


def sportQ(sportId, sportName, db):
    q = """INSERT INTO SPORTS VALUES (%s, %s)"""

    if isdigit(sportId.get()) and isalpha(sportName.get()):
        db.cursor().execute(q, [sportId.get(), sportName.get()])
        db.commit()
        db.close()
        messagebox.showinfo(title="Success", message="Record Inserted")
    else:
        messagebox.showerror(title="Error", message="Invalid Input")

    sportId.delete(0, END)
    sportName.delete(0, END)


def selQuery(table, currWin):
    # If you want to connect to a personal database, change the host to your hostname and fill in the rest of the
    # information
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="03232001",
        database="abclass"
    )
    action = db.cursor()
    q = "SELECT * FROM " + table
    action.execute(q)
    result = action.fetchall()

    records = ""
    for row in result:
        records += str(row) + "\n"

    query_label = Label(currWin, text=records, bg='#800000', fg='white')
    query_label['font'] = fontt
    query_label.grid(row=9, column=0, columnspan=2)


def delete():
    main.withdraw()
    delWindow = Toplevel(main)
    delWindow.title("Delete from database")

    pickLabel = Label(delWindow, text="Pick a table to delete from", bg='#FFF0F5')
    studentButton = Button(delWindow, text="Student", command=delStudent, bg='#FFF0F5')
    hobbyButton = Button(delWindow, text="Hobby", command=delHobby, bg='#FFF0F5')
    schoolButton = Button(delWindow, text="School", command=delSchool, bg='#FFF0F5')
    sportButton = Button(delWindow, text="Sport", command=delSport, bg='#FFF0F5')
    exitButton = Button(delWindow, text="Exit", command=lambda: openWindow(delWindow), bg='#FFF0F5')

    pickLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=50, sticky=W)
    studentButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)
    hobbyButton.grid(row=1, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    schoolButton.grid(row=2, column=0, pady=10, padx=10, ipadx=50, sticky=W)
    sportButton.grid(row=2, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    exitButton.grid(row=3, column=0, pady=10, padx=10, ipadx=55, sticky=W)

    delWindow.mainloop()


def delStudent():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    delStudentWindow = Toplevel(main)
    delStudentWindow.title("Delete from the student table")

    deleteEntry = Entry(delStudentWindow, width=30, bg='#FFF0F5')
    deleteEntry['font'] = fontt
    deleteEntry.grid(row=0, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    deleteEntry.insert(END, 'Format is "column_name = value"')

    deleteEntryLabel = Label(delStudentWindow, text="Enter the information to delete", bg='#FFF0F5')
    deleteEntryLabel['font'] = fontt
    deleteEntryLabel.grid(row=0, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    delButton = Button(delStudentWindow, text="Delete",
                       command=lambda: delStudQ(dbase, deleteEntry, delStudentWindow))
    delButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    action = dbase.cursor()
    q = """SELECT * FROM STUDENTS"""
    action.execute(q)
    result = action.fetchall()

    records = ""
    for row in result:
        records += str(row) + "\n"
    columnRec = ""
    colum = "SHOW COLUMNS FROM STUDENTS"
    action.execute(colum)
    col = action.fetchall()
    for column in col:
        columnRec += str(column[0]) + " type = " + str(column[1]).strip("b'").replace("char", "Characters").replace(
            "int", "Number") + "\n"

    columnRec_label = Label(delStudentWindow, text=records, bg='#800000', fg='white')
    columnRec_label['font'] = fontt
    columnRec_label.grid(row=2, column=0, sticky=W)

    columnRec_label = Label(delStudentWindow, text=columnRec, bg='#800000', fg='white')
    columnRec_label['font'] = fontt
    columnRec_label.grid(row=2, column=1, sticky=W)

    delStudentWindow.mainloop()


def delStudQ(dbase, deleteEntry, delWin):
    action = dbase.cursor()
    q = "DELETE FROM STUDENTS WHERE " + deleteEntry.get()
    action.execute(q)
    dbase.commit()
    deleteEntry.delete(0, END)
    deleteEntry.insert(END, 'Format is "column_name = value"')
    messagebox.showinfo(title="Success", message="Record was deleted")
    delWin.destroy()


def delHobby():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    delHobbyWindow = Toplevel(main)
    delHobbyWindow.title("Delete from the hobby table")

    deleteEntry = Entry(delHobbyWindow, width=30, bg='#FFF0F5')
    deleteEntry['font'] = fontt
    deleteEntry.grid(row=0, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    deleteEntry.insert(END, 'Format is "column_name = value"')

    deleteEntryLabel = Label(delHobbyWindow, text="Enter the information to delete", bg='#FFF0F5')
    deleteEntryLabel['font'] = fontt
    deleteEntryLabel.grid(row=0, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    delButton = Button(delHobbyWindow, text="Delete", command=lambda: delHobbyQ(dbase, deleteEntry, delHobbyWindow))
    delButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    action = dbase.cursor()
    q = """SELECT * FROM HOBBY"""
    action.execute(q)

    result = action.fetchall()
    records = ""
    for row in result:
        records += str(row) + "\n"

    columnRec = ""
    colum = "SHOW COLUMNS FROM HOBBY"
    action.execute(colum)
    col = action.fetchall()
    for column in col:
        columnRec += str(column[0]) + " type = " + str(column[1]).strip("b'").replace("char", "Characters").replace(
            "int", "Number") + "\n"

    recLabel = Label(delHobbyWindow, text=records, bg='#800000', fg='white')
    recLabel['font'] = fontt
    recLabel.grid(row=2, column=0, sticky=W)

    columnRecLabel = Label(delHobbyWindow, text=columnRec, bg='#800000', fg='white')
    columnRecLabel['font'] = fontt
    columnRecLabel.grid(row=2, column=1, columnspan=2, sticky=W)

    delHobbyWindow.mainloop()


def delHobbyQ(dbase, deleteEntry, delWin):
    action = dbase.cursor()
    q = "DELETE FROM HOBBY WHERE " + deleteEntry.get()
    action.execute(q)
    dbase.commit()
    deleteEntry.delete(0, END)
    deleteEntry.insert(END, 'Format is "column_name = value"')
    messagebox.showinfo(title="Success", message="Record was deleted")
    delWin.destroy()


def delSchool():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    delSchoolWindow = Toplevel(main)
    delSchoolWindow.title("Delete from the school table")

    deleteEntry = Entry(delSchoolWindow, width=30, bg='#FFF0F5')
    deleteEntry['font'] = fontt
    deleteEntry.grid(row=0, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    deleteEntry.insert(END, 'Format is "column_name = value"')

    deleteEntryLabel = Label(delSchoolWindow, text="Enter the information to delete", bg='#FFF0F5')
    deleteEntryLabel['font'] = fontt
    deleteEntryLabel.grid(row=0, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    delButton = Button(delSchoolWindow, text="Delete", command=lambda: delSchoolQ(dbase, deleteEntry, delSchoolWindow))
    delButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    action = dbase.cursor()
    q = """SELECT * FROM SCHOOL"""
    action.execute(q)

    result = action.fetchall()
    records = ""
    for row in result:
        records += str(row) + "\n"

    columnRec = ""
    colum = "SHOW COLUMNS FROM SCHOOL"
    action.execute(colum)
    col = action.fetchall()
    for column in col:
        columnRec += str(column[0]) + " type = " + str(column[1]).strip("b'").replace("char", "Characters").replace(
            "int", "Number") + "\n"

    recLabel = Label(delSchoolWindow, text=records, bg='#800000', fg='white')
    recLabel['font'] = fontt
    recLabel.grid(row=2, column=0, sticky=W)

    columnRecLabel = Label(delSchoolWindow, text=columnRec, bg='#800000', fg='white')
    columnRecLabel['font'] = fontt
    columnRecLabel.grid(row=2, column=1, columnspan=2, sticky=W)

    delSchoolWindow.mainloop()


def delSchoolQ(dbase, deleteEntry, delWin):
    action = dbase.cursor()
    q = "DELETE FROM SCHOOL WHERE " + deleteEntry.get()
    action.execute(q)
    dbase.commit()
    deleteEntry.delete(0, END)
    deleteEntry.insert(END, 'Format is "column_name = value"')
    messagebox.showinfo(title="Success", message="Record was deleted")
    delWin.destroy()


def delSport():
    dbase = mysql.connect(
        host=host.get(),
        user=userName.get(),
        passwd=passWord.get(),
        database=databasee.get()
    )
    delSportWindow = Toplevel(main)
    delSportWindow.title("Delete from the sport table")

    deleteEntry = Entry(delSportWindow, width=30, bg='#FFF0F5')
    deleteEntry['font'] = fontt
    deleteEntry.grid(row=0, column=1, pady=10, padx=10, ipadx=50, sticky=W)
    deleteEntry.insert(END, 'Format is "column_name = value"')

    deleteEntryLabel = Label(delSportWindow, text="Enter the information to delete", bg='#FFF0F5')
    deleteEntryLabel['font'] = fontt
    deleteEntryLabel.grid(row=0, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    delButton = Button(delSportWindow, text="Delete", command=lambda: delSportQ(dbase, deleteEntry, delSportWindow))
    delButton.grid(row=1, column=0, pady=10, padx=10, ipadx=50, sticky=W)

    action = dbase.cursor()
    q = """SELECT * FROM SPORTS"""
    action.execute(q)

    result = action.fetchall()
    records = ""
    for row in result:
        records += str(row) + "\n"

    columnRec = ""
    colum = "SHOW COLUMNS FROM SPORTS"
    action.execute(colum)
    col = action.fetchall()
    for column in col:
        columnRec += str(column[0]) + " type = " + str(column[1]).strip("b'").replace("char", "Characters").replace(
            "int", "Number") + "\n"

    recLabel = Label(delSportWindow, text=records, bg='#800000', fg='white')
    recLabel['font'] = fontt
    recLabel.grid(row=2, column=0, sticky=W)

    columnRecLabel = Label(delSportWindow, text=columnRec, bg='#800000', fg='white')
    columnRecLabel['font'] = fontt
    columnRecLabel.grid(row=2, column=1, columnspan=2, sticky=W)

    delSportWindow.mainloop()


def delSportQ(dbase, deleteEntry, delWin):
    action = dbase.cursor()
    q = "DELETE FROM SPORTS WHERE " + deleteEntry.get()
    action.execute(q)
    dbase.commit()
    deleteEntry.delete(0, END)
    deleteEntry.insert(END, 'Format is "column_name = value"')
    messagebox.showinfo(title="Success", message="Record was deleted")
    delWin.destroy()


main = Tk()
main.configure(background='#800000')
fontt = font.Font(family='Courier', size=10, weight='bold')

main.title("Database Application")
main.geometry("450x400")

host = Entry(main, width=30, bg='#FFF0F5')
host['font'] = fontt
host.grid(row=0, column=1, padx=20, pady=(10, 0))
userName = Entry(main, width=30, bg='#FFF0F5')
userName['font'] = fontt
userName.grid(row=1, column=1)
passWord = Entry(main, width=30, bg='#FFF0F5')
passWord['font'] = fontt
passWord.grid(row=2, column=1)
databasee = Entry(main, width=30, bg='#FFF0F5')
databasee['font'] = fontt
databasee.grid(row=3, column=1)

hostLabel = Label(main, text="Host Name", bg='#FFF0F5')
hostLabel['font'] = fontt
hostLabel.grid(row=0, column=0, pady=(10, 0))
userNameLabel = Label(main, text="User Name", bg='#FFF0F5')
userNameLabel['font'] = fontt
userNameLabel.grid(row=1, column=0)
passWordLabel = Label(main, text="Password", bg='#FFF0F5')
passWordLabel['font'] = fontt
passWordLabel.grid(row=2, column=0)
databaseeLabel = Label(main, text="Database Name", bg='#FFF0F5')
databaseeLabel['font'] = fontt
databaseeLabel.grid(row=3, column=0)

connect_button = Button(main, text="Connect To Database", command=connect)
connect_button['font'] = fontt
connect_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

main.mainloop()
