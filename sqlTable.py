import tkinter as tk
from tkinter import ttk
import pymysql

mydb = pymysql.connect("mysqltpj.ddns.net","root","root","adsdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT adid, cost, startd, endd, adstatus FROM b_class_ad where userid = 1")
scores = tk.Tk() 
myresult = mycursor.fetchall()
mydb.close()
#def show():
cols = ('Id','Cost','Start Date','End Date', 'Status')
listBox = ttk.Treeview(scores, columns=cols, show='headings')
label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)
tempList = []

for x in myresult:
    tempList.append([x[0], x[1] ,x[2], x[3], x[4]])
tempList.sort(key=lambda e: e[2], reverse=False)
for i, (adid, cost, sdate, edate, status) in enumerate(tempList, start=1):
    listBox.insert("", "end", values=(adid, cost, sdate, edate, status))


# create Treeview with 3 columns

# set column headings


listBox.column('#1', minwidth=20, width = 30, stretch = True)
listBox.column('#2', minwidth=20, width = 40, stretch = True)
listBox.column('#3', minwidth=20, width = 150, stretch = True)
listBox.column('#4', minwidth=20, width = 150, stretch = True)
listBox.column('#5', minwidth=20, width = 30, stretch = True)
#showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

scores.mainloop()