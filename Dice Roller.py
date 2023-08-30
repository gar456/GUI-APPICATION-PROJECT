from tkinter import*


die = {
  0 : '🎲',
  1 : '⚀',
  2 : '⚁',
  3 : '⚂',
  4 : '⚃',
  5 : '⚄',
  6 : '⚅'
}

App = Tk()
App.title('Dice Roller')


dice = Label(App, text=die[0], font=('Times', 100), foreground='black')
dice.grid(row=0, column=0, padx=25, pady=5)

def roll():
    from random import randint
    i = randint(1, 6)
    msg = Label(App, text=die[i], font=('Times', 100), foreground='black')
    msg.grid(row=0, column=0, padx=25, pady=5)

rollB = Button(App, text='Roll', command=roll)
rollB.grid(row=1, column=0)

App.mainloop()