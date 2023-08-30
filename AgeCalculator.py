from tkinter import *
from datetime import datetime

bg = 'green'
fg = 'cyan'
App = Tk()
App.title('Age Calculator')
App['background'] = bg
App.geometry('250x250')

msg = Label(App, text='Enter your DOB', background=bg, foreground=fg)
msg.grid(row=0, column=0, columnspan=3)

dayL = Label(App, text='Day:', background=bg, foreground=fg)
dayE = Entry(App, width=2)

monL = Label(App, text='Month:', background=bg, foreground=fg)
monE = Entry(App, width=2)

yrL = Label(App, text='Year:', background=bg, foreground=fg)
yrE = Entry(App, width=6)

dayL.grid(row=1, column=0)
dayE.grid(row=1, column=1)

monL.grid(row=1, column=2)
monE.grid(row=1, column=3)

yrL.grid(row=1, column=4)
yrE.grid(row=1, column=5)


def find_days():
    date = int(dayE.get())
    mon = int(monE.get())
    yr = int(yrE.get())

    dob = datetime(day=date, month=mon, year=yr)
    time_now = datetime.now()
    time_dif = time_now - dob
    dys = Label(App, text='You lived' + str(time_dif.days) + 'days')
    dys.grid(row=3, column=0, columnspan=4)


def find_scs():
    date = int(dayE.get())
    mon = int(monE.get())
    yr = int(yrE.get())
    dob = datetime(day=date, month=mon, year=yr)
    time_now = datetime.now()
    time_dif = time_now - dob
    scs = Label(App, text='You lived' + str(time_dif.total_seconds()) + 'seconds!')
    scs.grid(row=4, column=0, columnspan=6)


dysB = Button(App, text='Total Days', command=find_days)
scsB = Button(App, text='Total Seconds', command=find_scs)
dysB.grid(row=2, column=1, columnspan=3)
scsB.grid(row=2, column=5, columnspan=5)
App.mainloop()
