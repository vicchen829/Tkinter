# https://shengyu7697.github.io/python-tkinter-entry-number-only/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
import numpy as np

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

num1, num2 =np.random.randint(10, size = 2)
operation_list = ['+', '-', '*']
operation = operation_list[np.random.randint(0, 3, 1)[0]]
formula = f'{num1} {operation} {num2}'

if operation == '+':
    _answers = num1 + num2
elif operation == '-':
    _answers = num1 - num2
else:
    _answers = num1 * num2

mylabel1 = tk.Label(root, text = formula)
mylabel1.grid(row = 0, column = 0)

def button_event():
	_answer = int(myentry.get())
	if _answer == '':
		messagebox.showerror('message', '未輸入答案')
	elif _answer == _answers:
		messagebox.showinfo('message', '答對了!')
	else :
		messagebox.showerror('message', '答錯')

def validate(P):
	print(P)
	if str.isdigit(P) or P == '':
		return True
	else :
		return False

vcmd = (root.register(validate), '%P')
myentry = tk.Entry(root, validate = 'key', validatecommand = vcmd)
#myentry = tk.Entry(root)
myentry.grid(row = 0, column = 1)

mybutton = tk.Button(root, text = '完成', command = button_event)
mybutton.grid(row = 1, column = 1)

root.mainloop()