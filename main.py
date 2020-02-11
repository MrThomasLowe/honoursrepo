from tkinter import *
import tkinter as tk
root = Tk()

enterStock

root.title("Stock Portfolio Optimisation Tool")
lbl = Label(root, text="test")
lbl.grid(column=0,row=0)
root.geometry("1280x720")

enterStock1 = tk.Entry(root)
root.create_window(200,400,window=enterStock1)

#keeps the program running until the window is closed
root.mainloop()
