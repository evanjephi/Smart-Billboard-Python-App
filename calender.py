import tkinter as tk
from tkinter import ttk
import calendar
cbID = 1

c = calendar.TextCalendar(calendar.SUNDAY)
app = tk.Tk() 
app.geometry('400x100')
years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']


thirtyOne = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
thirty = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
feb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
leapFeb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

monthDict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8,  'Sept':9, 'Oct':10, 'Nov':11, 'Dec':12}

hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
minute = ['0', '5', '10', '15', '20', '25', '30', '35', '50', '55']
second = ['0', '5', '10', '15', '20', '25', '30', '35', '50', '55']



def prnt():
    print(calendar.month(int(comboExample.get()), 4))
    
comboYears = ttk.Combobox(app, values = years, width = 4)
comboYears.grid(row = 0, column = 0)

comboMonths = ttk.Combobox(app, values = months, width = 4)
comboMonths.grid(row = 0, column = 1)


comboGlobal = ttk.Combobox(app, values = feb, width = 2)
comboGlobal.grid(row = 0, column = 2)

comboHour = ttk.Combobox(app, values = hour, width = 2)
comboHour.grid(row = 1, column = 0)

comboMinute = ttk.Combobox(app, values = minute, width = 2)
comboMinute.grid(row = 1, column = 1)

comboSecond = ttk.Combobox(app, values = second, width = 2)
comboSecond.grid(row = 1, column = 2)






comboYears1 = ttk.Combobox(app, values = years, width = 4)
comboYears1.grid(row = 0, column = 3)

comboMonths1 = ttk.Combobox(app, values = months, width = 4)
comboMonths1.grid(row = 0, column = 4)

comboGlobal1 = ttk.Combobox(app, values = feb, width = 2)
comboGlobal1.grid(row = 0, column = 5)

comboHour1 = ttk.Combobox(app, values = hour, width = 2)
comboHour1.grid(row = 1, column = 3)

comboMinute1 = ttk.Combobox(app, values = minute, width = 2)
comboMinute1.grid(row = 1, column = 4)

comboSecond1 = ttk.Combobox(app, values = second, width = 2)
comboSecond1.grid(row = 1, column = 5)





print('done')
def callbackYears(eventObject):
    #delCombo()
    global comboGlobal
    if (((int(comboYears.get()) % 4 == 0 and int(comboYears.get()) % 100 != 0) or int(comboYears.get()) % 400 == 0) and comboMonths.get() == 'Feb'):
        comboGlobal.config(values = ['1'])
    elif(comboMonths.get()=='Feb'):
        comboGlobal = ttk.Combobox(app, values = feb, width = 2)
        comboGlobal.grid(row = 0, column = 2)
    elif (comboMonths.get()=='Jan' or comboMonths.get()=='Mar' or comboMonths.get()=='May' or comboMonths.get()=='Jul' or comboMonths.get()=='Aug' or comboMonths.get()=='Oct' or comboMonths.get()=='Dec'):
        comboGlobal= ttk.Combobox(app, values = thirtyOne, width = 2)
        comboGlobal.grid(row = 0, column = 2)
    else:
        comboGlobal = ttk.Combobox(app, values = thirty, width = 2)
        comboGlobal.grid(row = 0, column = 2)

def callbackYears1(eventObject):
    print('in years 1')
    #delCombo()
    global comboGlobal1
    if (((int(comboYears1.get()) % 4 == 0 and int(comboYears1.get()) % 100 != 0) or int(comboYears1.get()) % 400 == 0) and comboMonths1.get() == 'Feb'):
        comboGlobal1 = ttk.Combobox(app, values = leapFeb, width = 2)
        comboGlobal1.grid(row = 0, column = 5)
        print ('in first IF')
    elif(comboMonths1.get()=='Feb'):
        comboGlobal1 = ttk.Combobox(app, values = feb, width = 2)
        comboGlobal1.grid(row = 0, column = 5)
        print ('in second IF')
    elif (comboMonths1.get()=='Jan' or comboMonths1.get()=='Mar' or comboMonths1.get()=='May' or comboMonths1.get()=='Jul' or comboMonths1.get()=='Aug' or comboMonths1.get()=='Oct' or comboMonths1.get()=='Dec'):
        comboGlobal1= ttk.Combobox(app, values = thirtyOne, width = 2)
        comboGlobal1.grid(row = 0, column = 5)
        print ('in third IF')
    else:
        comboGlobal1 = ttk.Combobox(app, values = thirty, width = 2)
        comboGlobal1.grid(row = 0, column = 5)
        print ('in last IF')


comboYears.bind("<<ComboboxSelected>>", callbackYears)
comboMonths.bind("<<ComboboxSelected>>", callbackYears)

comboYears1.bind("<<ComboboxSelected>>", callbackYears1)
comboMonths1.bind("<<ComboboxSelected>>", callbackYears1)


def prnt1():
    print("from " + comboYears.get() + "/" + str(monthDict[comboMonths.get()])+"/"+ comboGlobal.get()+"    " +comboHour.get()+":"+comboMinute.get()+":"+comboSecond.get())
    

btn = ttk.Button(text = "g", command = prnt1)
btn.grid(row = 2, column = 0)

for i in c.itermonthdays(2025, 4):
    if(i > 0):
        print(i)
app.mainloop()


