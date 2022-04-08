from datetime import datetime
from tkinter import *
from tkcalendar import Calendar


cal_root = Tk()
cal_root.geometry("250x250")
cal = Calendar(cal_root, selectmode='day',
               year=datetime.now().year, month=datetime.now().month,
               day=datetime.now().day, date_pattern='yyyy-MM-dd')

cal.pack()


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())
    return cal.get_date()


Button(cal_root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(cal_root, text="")

date.pack(pady=20)
