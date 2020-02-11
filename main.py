from tkinter import *
import tkinter as tk
print("test")

win = tk.Tk()

win.title("Stock Portfolio Optimisation Tool")
lbl = Label(win, text="test")
lbl.grid(column=0,row=0)
win.geometry("1280x720")
#keeps the program running until the window is closed
win.mainloop()
