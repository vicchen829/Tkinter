#https://shengyu7697.github.io/python-tkinter-tutorial/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
# tk.Tk()建立主視窗
root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
#geometry() 改變主視窗大小
root.geometry('600x400')

#Label 標籤
mylabel1 = tk.Label(root, text = 'hello world',
                  font = ('Arial', 18))
#mylabel1.pack()

#print(label1['text'])

#Button 按紐
#使用Button建立一個按鈕並指定button_event事情處理函數
def button_event():
    mybutton['text'] = 'Hello World'

mybutton = tk.Button(root, text = 'button',
                    command = button_event)
#mybutton.pack()

#Entry 文字輸入框
# label1 = tk.Label(root, text = 'Name:')
# label1.grid(row = 0, column = 0)
# entry1 = tk.Entry(root)
# entry1.grid(row = 0, column = 1)

# label2 = tk.Label(root, text = 'Password:')
# label2.grid(row = 1, column = 0)
# entry2 = tk.Entry(root, show = '*')
# entry2.grid(row = 1, column = 1)

# loginbutton = tk.Button(root, text = 'Login')
# loginbutton.grid(row = 2, column = 1)

# colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
# r = 0
# for c in colours:
#     tk.Label(root, text = c, width = 10).grid(row = r, column = 0)
#     tk.Entry(root, bg = c, width = 15).grid(row = r, column = 1)
#     r += 1

# Combobox 下拉式選單
mycombobox = ttk.Combobox(root)
mycombobox['values'] = ['apple', 'banana', 'orange', 'lemon', 'tomato']
mycombobox.pack(pady = 10)
mycombobox.current(1)

#messagebox 訊息框
def button_message():
    messagebox.showinfo('my messagebox', 'hello~')

messagebutton = tk.Button(root, text = 'button',
                            command = button_message)
messagebutton.pack()
root.mainloop()