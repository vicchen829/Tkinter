# https://shengyu7697.github.io/python-tkinter-button/
import tkinter as tk
import datetime
from tkinter import ttk, messagebox

root = tk.Tk()
YYYYMMDD = datetime.datetime.now().strftime('%Y-%m-%d')
root.title(f'今天是{YYYYMMDD}')
root.geometry('600x400')

# def button_event():
# 	mybutton['text'] = 'hello world'
# 	mybutton.config(text = 'hahaha')

# mybutton = tk.Button(root, text = 'button',
# 							command = button_event)
# mybutton = tk.Button(root, text = 'button',
# 							command = lambda : mybutton.config(text = 'hahaha'))
# mybutton.pack()

# def button_red_event():
# 	button_red['bg'] = 'red'
# 	button_red['text'] = 'red button'
# 	button_red.config(width = 20, height = 10)

# def button_blue_event():
# 	button_blue['bg'] = 'blue'
# 	button_blue['text'] = 'blue button'
# 	button_blue.config(width = 30, height = 5)

def button_event(button, bg, text, width, height):
	button.config(bg = bg, text = text, width = width, height = height)

button_red = tk.Button(root, text = 'button1', 
								command = lambda : button_event(button_red, 'grey', 'darkk', 10, 5))
button_blue = tk.Button(root, text = 'button2', 
								command = root.destroy)#lambda : button_event(button_blue, 'yellow', 'yelloww', 5, 10))
# command=root.destroy 離開程式
button_red.pack()
button_blue.pack()
root.mainloop() 