from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import pyfolio as pf
import empyrical as ep
from yahoofinancials import YahooFinancials
from datetime import datetime
from dateutil.relativedelta import relativedelta

#https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Create-your-first-GUI-application

win = Tk()
win.title("Stock Portfolio Optimisation Tool")
win.geometry("1280x720")

class App(object):
    def __init__(self,master):
        self.master = master
        self.create_text()
        self.create_tabs()

    def create_text(self):

        enterStock1 = Entry(win,width=10)
        enterStock1.place(x=15,y=15)
        enterStock2 = Entry(win,width=10)
        enterStock2.place(x=15,y=30)
        enterStock3 = Entry(win,width=10)
        enterStock3.place(x=30,y=15)
        enterStock4 = Entry(win,width=10)
        enterStock4.place(x=30,y=30)

        enterStock1.focus()
    
    def create_tabs(self):
        tab_control = ttk.Notebook(win)
        portfolioTab = ttk.Frame(tab_control)

        tab_control.add(portfolioTab, text='Portfolio Optimisation')
        tab_control.pack(expand=1,fill='both')



#keeps the program running until the window is closed

app=App(win)
win.mainloop()