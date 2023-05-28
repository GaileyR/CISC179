"""
cisc179 base module.

This is the principal module of the cisc179 project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "cisc179"

import tkinter
from tkinter import *
from tkinter.font import Font

def deletetask():
    thelist.delete(ANCHOR)

def addtask():
    thelist.insert(END, addentry.get())
    addentry.delete(0, END)

def completedtask():
    thelist.itemconfig(
        thelist.curselection(),
        fg="LightPink4"
    )
    thelist.selection_clear(0, END)

#window
window = tkinter.Tk()
window.title("Task List")
window.geometry("400x470")

#font
thefont= Font(
    family="Calibri Light",
    size=16,
)

#frames or smth
top_frame = Frame(window)
bottom_frame = Frame(window)
top_frame.grid(row=0,
               column=0)
bottom_frame.grid(row=2,
                  column=0,
                  pady=20)

thelist = Listbox(top_frame,
               font= thefont,
               width=35,
               height=12,
               bg="pink3",
               highlightthickness=0,
               selectforeground= "pink2",
               selectbackground= "white",
               bd=0,
               justify="center",
               fg="white")

thelist.grid(row=0, column=0,
             padx=6, pady=5)

#tasks
tasks = ["List:",]
for item in tasks:
    thelist.insert(END, item)

addentry = Entry(window,
                width=45,
                font=("Calibri light", 12),
                )

addentry.grid(row=1,
              pady=15 )

#buttons
deletebutton = Button(bottom_frame,
                      text="Delete",
                      command=deletetask,
                      fg="white",
                      bg="pink3")
addbutton = Button(bottom_frame,
                   text="Add",
                   command=addtask,
                   fg="white",
                   bg="pink3")
donebutton = Button(bottom_frame,
                    text="Done",
                    command=completedtask,
                    fg="white",
                    bg="pink3")

deletebutton.grid(row=1, column=1)
addbutton.grid(row=1, column=0)
donebutton.grid(row=1, column=2)
for Button in bottom_frame.grid_slaves(row=1):
    Button.grid(ipadx=5, ipady=5,
                padx=5, pady=0)

#open window
window.mainloop()