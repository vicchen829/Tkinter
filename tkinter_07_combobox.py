# https://shengyu7697.github.io/python-tkinter-combobox/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
import numpy as np

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

def button_event():
	print(mycombobox.current(), mycombobox.get())
	buttonText.set('idx:' + str(mycombobox.current()) + ',' + mycombobox.get())

def combobox_selected(event):
	label1.set('我最愛 ' + mycombobox.get())

_values = ['apple', 'banana', 'orange', 'lemon', 'tomato']

# state = 'readonly' 選項只能讀取不能修改
mycombobox = ttk.Combobox(root, values = _values, state='readonly')
mycombobox.pack(pady = 10)
mycombobox.current(2)
mycombobox.bind('<<ComboboxSelected>>', combobox_selected)

buttonText = tk.StringVar()
buttonText.set('button')
tk.Button(root, textvariable = buttonText, command = button_event).pack()

label1 = tk.StringVar()
label1.set('我最愛 ')
tk.Label(root, textvariable=label1, height=5, font=('Arial', 12)).pack()


root.mainloop()