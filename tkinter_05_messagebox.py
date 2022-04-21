# https://shengyu7697.github.io/python-tkinter-messagebox/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox

# tkinter messagebox.showinfo() 顯示訊息對話框
# tkinter messagebox.showwarning() 警告訊息對話框
# tkinter messagebox.showerror() 錯誤訊息對話框
# tkinter messagebox.askokcancel() 確定取消對話框
# tkinter messagebox.askquestion() 是否問題對話框

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

# root.withdraw()
# showinfo() 顯示訊息對話框
# messagebox.showinfo('my message', 'hello world')

# showwarning() 警告訊息對話框
# messagebox.showwarning('my message', 'hello world')

# showerror() 錯誤訊息對話框
# messagebox.showerror('my messagebox', 'hello world')

# askokcancel() 確定取消對話框
# messagebox.askokcancel('my messagebox', 'hello world')

def button_event():
	ask_exit = messagebox.askquestion('my messagebox', 'Exit?')
	if ask_exit == 'yes':
		root.destroy()
tk.Button(root, text = 'exit' , command = button_event).pack()

root.mainloop()