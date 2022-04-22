
from tkinter import *
from tkinter import messagebox
from tkinter import font

import mysql.connector as mysql
from numpy.core.defchararray import isdigit


def submit():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="03232001",
        database="abclass"
    )
    action = db.cursor()
    q = """INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s, %s)"""
    if isdigit(studId.get()) and isdigit(schoolId.get()) and isdigit(hobbyId.get()) and (isdigit(sportId.get()) or sportId.get() == "None"):
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



def query():
    #If you want to connect to a personal database, change the host to your hostname and fill in the rest of the information
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
    # db.close()

    records = ""
    for row in result:
        records += str(row) + "\n"

    query_label = Label(main, text=records,bg='#800000', fg='white')
    query_label['font'] = font.Font(family='Helvetica', size=12)
    query_label.grid(row=12, column=0, columnspan=2)


main = Tk()
main.configure(background='#800000')
fontt = font.Font(family='Courier', size=10, weight='bold')

main.title("Students Database")
main.geometry("450x400")

fName = Entry(main, width=30,bg='#FFF0F5')
fName['font'] = fontt
fName.grid(row=0, column=1, padx=20, pady=(10, 0))
lName = Entry(main, width=30,bg='#FFF0F5')
lName['font'] = fontt
lName.grid(row=1, column=1)
studId = Entry(main, width=30,bg='#FFF0F5')
studId['font'] = fontt
studId.grid(row=2, column=1)
schoolId = Entry(main, width=30,bg='#FFF0F5')
schoolId['font'] = fontt
schoolId.grid(row=3, column=1)
hobbyId = Entry(main, width=30,bg='#FFF0F5')
hobbyId['font'] = fontt
hobbyId.grid(row=4, column=1)
sportId = Entry(main, width=30,bg='#FFF0F5')
sportId['font'] = fontt
sportId.insert(END, 'None')
sportId.grid(row=5, column=1)

fNameLabel = Label(main, text="First Name",bg='#FFF0F5')
fNameLabel['font'] = fontt
fNameLabel.grid(row=0, column=0, pady=(10, 0))
lNameLabel = Label(main, text="Last Name",bg='#FFF0F5')
lNameLabel['font'] = fontt
lNameLabel.grid(row=1, column=0)
studIdLabel = Label(main, text="Student ID",bg='#FFF0F5')
studIdLabel['font'] = fontt
studIdLabel.grid(row=2, column=0)
schoolIdLabel = Label(main, text="School ID",bg='#FFF0F5')
schoolIdLabel['font'] = fontt
schoolIdLabel.grid(row=3, column=0)
hobbyIdLabel = Label(main, text="Hobby ID",bg='#FFF0F5')
hobbyIdLabel['font'] = fontt
hobbyIdLabel.grid(row=4, column=0)
sportIdLabel = Label(main, text="Sport ID",bg='#FFF0F5')
sportIdLabel['font'] = fontt
sportIdLabel.grid(row=5, column=0)


submit_btn = Button(main, text="Insert To Database", command=submit)
submit_btn['font'] = fontt
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


query_btn = Button(main, text="Show Student Record", command=query)
query_btn["font"] = fontt
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

main.resizable(False,True)
main.mainloop()
