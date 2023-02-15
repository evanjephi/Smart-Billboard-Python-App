from tkinter import *

root = Tk()

var1 = StringVar()
var2 = StringVar()

var1.set('a')
var2.set(0)

Radiobutton(root, text = "group1", variable = var1, value = 'a').pack()
Radiobutton(root, text = "group1", variable = var1, value = 'c').pack()
Radiobutton(root, text = "group2", variable = var2, value = 1).pack()
Radiobutton(root, text = "group2", variable = var2, value = 0).pack()

def printVar():
    print(var1.get())
    print(var2.get())
brwsImgBtn = Button(root, text = "Print", command = printVar)
brwsImgBtn.pack(side="bottom")

root.mainloop()