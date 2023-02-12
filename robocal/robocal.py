import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateparser import parse

date_chosen=[]
counter = 0

def updateLabel(event):
    picked_date=parse(calendar.get_date())
    if calendar.get_date() in date_chosen:
            date_chosen.remove(str(calendar.get_date()))
            date_chosen2=list(set(date_chosen)).copy()
            label.config(text="Selected Date: {}".format(date_chosen2))
    else:
        if picked_date.weekday()<5:
            counter+1
            date_chosen.append(calendar.get_date())
            date_chosen2=list(set(date_chosen)).copy()
            label.config(text="Selected Date: {}".format(date_chosen2))

root = tk.Tk()
#root.geometry("400x400")

calendar = Calendar(root, mindate=date.today(),
                          maxdate=date.today()+ relativedelta(months=3),
                          showweeknumbers=False,
                          showothermonthdays=False,
                          headerbackground = "grey",
                          headerforeground = "white",
                          selectbackground = "lightyellow",
                          selectforeground = "red",
                          normalbackground = "white",
                          normalforeground = "black",
                          weekendbackground = "blue",
                          weekendforeground = "lightgrey",
                          tooltipforeground = "black",
                          font="Arial 14")
calendar.pack()
calendar.bind('<<CalendarSelected>>', updateLabel)

 
label = tk.Label(root, text="Selected Date: ")
label.pack()
root.mainloop()


