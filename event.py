import tkinter as tk
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.grid(column=0, row=0)


def callback(eventObject):
    print(eventObject)

cbox.bind("<<ComboboxSelected>>", callback)
print('sumn shit')
tkwindow.mainloop()