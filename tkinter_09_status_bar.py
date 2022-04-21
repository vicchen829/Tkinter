# https://shengyu7697.github.io/python-tkinter-canvas/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
import numpy as np
import time

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

# 在 tkinter 裡沒有專用的 statusbar 這種類別，但可以透過修改 Label 的樣式來達成

# 在 Label 的屬性中 bd=1：指定邊框大小，
# 在 statusbar.pack 指定要放在視窗底部 side=tk.BOTTOM，並且寬度填滿整個視窗的寬度 fill=tk.X
# statusbar = tk.Label(root, text = f'Date : {YYYYMMDD}', 
#                     bd = 1, relief = tk.SUNKEN, anchor=tk.W)
# statusbar.pack(side = tk.BOTTOM, fill = tk.X)

def button_event():
    statustext.set('processing...')
    statusbar.update()
    time.sleep(1)
    statustext.set('done')

statustext = tk.StringVar()
statustext.set(f'Date : {YYYYMMDD}')
statusbar = tk.Label(root, textvariable = statustext, relief=tk.SUNKEN, anchor='w')
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

button = tk.Button(root, text = 'Start', command = button_event)
button.pack()

root.mainloop()