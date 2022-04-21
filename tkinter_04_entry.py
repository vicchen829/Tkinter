# https://shengyu7697.github.io/python-tkinter-entry/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

tk.Label(root, text = 'Name:').grid(row = 0, column = 0)
myentry = tk.Entry(root)
myentry.grid(row = 0, column = 1)

def button_event():
	if myentry.get() != '':
		mybutton['text'] = myentry.get()
mybutton = tk.Button(root, text = 'button', command = button_event)
mybutton.grid(row = 1, column = 1)

var = tk.StringVar()
myentry2 = tk.Entry(root, textvariable = var, show = '*')
myentry2.grid(row = 2, column = 1)

def button_event2():
	if var.get() != '':
		mybutton2['text'] = var.get()
mybutton2 = tk.Button(root, text = 'button', command = button_event2)
mybutton2.grid(row = 2, column = 2)

root.mainloop() 