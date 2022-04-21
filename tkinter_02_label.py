# https://shengyu7697.github.io/python-tkinter-label/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

tk.Label(root, text = 'hello label').pack()
# tk.Label(root, text = 'hello label').grid(row = 1, column = 1)
# tk.Label(root, text = 'hello0000 label').grid(row = 0, column = 1)

tk.Label(root, text = 'Arial_18',
        font = ('Arial', 18)).pack()

tk.Label(root, text = 'hello world',
        width = 20, height = 5,
        bg = 'yellow').pack()
root.mainloop()