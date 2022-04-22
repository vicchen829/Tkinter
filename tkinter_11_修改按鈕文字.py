# https://shengyu7697.github.io/python-tkinter-change-button-text/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from tkinter import filedialog
import numpy as np
import time, os

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')


root.mainloop()