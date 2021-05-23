import tkinter
from tkinter import *

root = Tk()

root.title("GRADE CALULATOR")
root.geometry("500x400")
    
def marksCalculate():
    OS = int(OSValue.get())
    DBMS = int(DBMSValue.get())
    TOC = int(TOCValue.get())
    final = (OS + DBMS + TOC)
    Label(text=f"{final}", font="arial 20 bold").place(x=250, y=170)
    average = int(final / 3)
    Label(text=f"{average}", font="arial 20 bold").place(x=250, y=220)
    
    if average > 50:
        gradeScored = "PASS"
    else:
        gradeScored = "FAIL"
    Label(text=f"{gradeScored}", font="arial 20 bold").place(x=250, y=270)

subject1 = Label(root, text="OS", font="arial 20")
subject1.place(x=50, y=20)
subject2 = Label(root, text="DBMS", font="arial 20")
subject2.place(x=50, y=70)
subject3 = Label(root, text="TOC", font="arial 20")
subject3.place(x=50, y=120)
totalMarks = Label(root, text="Total", font="arial 20")
totalMarks.place(x=50, y=170)
averageMarks = Label(root, text="Average", font="arial 20")
averageMarks.place(x=50, y=220)
gradeScored = Label(root, text="Grades", font="arial 20")
gradeScored.place(x=50, y=270)

OSMarks = StringVar()
DBMSMarks = StringVar()
TOCMarks = StringVar()

OSValue = Entry(root, textvariable=OSMarks, font="arial 20", width=15)
OSValue.place(x=250, y=20)
DBMSValue = Entry(root, textvariable=DBMSMarks, font="arial 20", width=15)
DBMSValue.place(x=250, y=70)
TOCValue = Entry(root, textvariable=TOCMarks, font="arial 20", width=15)
TOCValue.place(x=250, y=120)

Button(text="Calculate", font="arial 15", bg="green", bd=5, command=marksCalculate).place(x=50, y=330)
Button(text="Exit", font="arial 15", bg="red", width=8, bd=5, command=root.destroy).place(x=350, y=330)

root.mainloop()
