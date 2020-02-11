from tkinter import *
import tkinter as tk
win = Tk()

win.title("Stock Portfolio Optimisation Tool")
lbl = Label(win, text="test")
lbl.grid(column=0,row=0)
win.geometry("1280x720")

enterStock1 = Entry(win,width=10)
enterStock1.grid(column=1,row=0)
enterStock2 = Entry(win,width=10)
enterStock2.grid(column=2,row=0)
enterStock3 = Entry(win,width=10)
enterStock3.grid(column=1,row=1)
enterStock4 = Entry(win,width=10)
enterStock4.grid(column=1,row=2)

enterStock1.focus()

#keeps the program running until the window is closed
win.mainloop()
