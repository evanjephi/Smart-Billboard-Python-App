import tkinter as tk
import datetime
now = datetime.datetime.now()
class MyApp():
    def __init__(self):
        self.root = tk.Tk()
        l1 = tk.Label(self.root, text="Hello")
        l2 = tk.Label(self.root, text="World")
        l1.grid(row=0, column=0, padx=(0, 0))
        l2.grid(row=1, column=0, padx=(0, 0))
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

app = MyApp()
app.root.mainloop()