# https://shengyu7697.github.io/python-tkinter-filedialog/
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

root.withdraw()
# 叫出開啟檔案對話框
username = os.getlogin()
user_desktop = f'C:\\Users\\{username}\\Desktop'
# initialdir : 設定初始目錄
# filetypes : 設定開啟的檔案類型
file_path = filedialog.askopenfilename(parent=root, 
                                    title='請選擇xxx檔案',
                                    initialdir = user_desktop,
                                    filetypes=[('Excel files', '.xlsx .xls')])

if not file_path:
    print('file path is empty')
else:
    with open(file_path, 'r') as f:
        print(f.read())


root.mainloop()