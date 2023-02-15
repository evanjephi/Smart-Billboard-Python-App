import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pyodbc
#import mysql.connector
import sys
from PIL import Image
import base64
import PIL.Image
import datetime
from tkinter import messagebox
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ez.ads.noreply@gmail.com"  # Enter your address
receiver_email = "n.drake2045@gmail.com"  # Enter receiver address
#password = input("Type your password and press enter: ")

exp = " "  
usrSql = ""
passSql = ""
usrN = "."
passw = "."
userID = 0
bindata = 0b111011
text = ''
reader = SimpleMFRC522()
codeVal=''

sqlServer = 'mysqltpj.ddns.net'
sqlServerUsr = 'root'
sqlServerPass = 'root'
databaseName = 'adsdb'
#sqlString = 'DRIVER=FreeTDS;SERVER=192.168.0.26;PORT=49170;DATABASE=adsDB;UID=sa;PWD=access;TDS_Version=8.0;'

now = datetime.datetime.now()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
       

class enterText(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #varClass = StringVar()
       adTxt = tk.Text(self, height=4, width=54)
       adTxt.grid(row = 0, column = 0, rowspan= 1, columnspan = 10, ipadx = 15 , ipady = 20)
       
       def press(num):
           #global exp
           #exp=exp + str(num.lower())
           #equation.set(exp)
           global text
           adTxt.insert(tk.INSERT, num.lower())
           content = adTxt.get(1.0, "end-1c")
           text = content
           print(content)
           
       def clrTxt():
           adTxt.delete('1.0', END)
           
       def bkSpc():
           adTxt.delete('%s - 1c' % tk.INSERT)
       
       def delete():
           adTxt.delete('%s' % tk.INSERT)
       
       def enterKey():
           adTxt.insert(tk.INSERT, '\n')
           
       def OK():
           print('OK pressed')
           upP = upLoadPage(self)
           upP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       btnWidth = 2
       btnIpadx = 2
       btnIpady = 2
       equation = tk.StringVar()
       
       
       #Row 1
       q = Button(self,text = '1' , width = btnWidth, command = lambda : press('1'))
       q.grid(row = 1 , column = 0, ipadx = 1, ipady = 3)
       
       w = Button(self,text = '2' , width = btnWidth, command = lambda : press('2'))
       w.grid(row = 1, column = 1, ipadx = btnIpadx , ipady = btnIpady )

       E = Button(self,text = '3' , width = btnWidth, command = lambda : press('3'))
       E.grid(row = 1 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       R = Button(self,text = '4' , width = btnWidth, command = lambda : press('R'))
       R.grid(row = 1 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       T = Button(self,text = '5' , width = btnWidth, command = lambda : press('T'))
       T.grid(row = 1 , column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       Y = Button(self,text = '6' , width = btnWidth, command = lambda : press('Y'))
       Y.grid(row = 1 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       U = Button(self,text = '7' , width = btnWidth, command = lambda : press('U'))
       U.grid(row = 1 , column = 6, ipadx = btnIpadx, ipady = btnIpady )

       I = Button(self,text = '8' , width = btnWidth, command = lambda : press('I'))
       I.grid(row = 1 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       O = Button(self,text = '9' , width = btnWidth, command = lambda : press('O'))
       O.grid(row = 1 , column = 8, ipadx = btnIpadx, ipady = btnIpady )

       P = Button(self,text = '0' , width = btnWidth, command = lambda : press('P'))
       P.grid(row = 1 , column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       #Row 2
       
       q = Button(self,text = 'Q' , width = btnWidth, command = lambda : press('Q'))
       q.grid(row = 2 , column = 0, ipadx = 1, ipady = 3)
       
       w = Button(self,text = 'W' , width = btnWidth, command = lambda : press('W'))
       w.grid(row = 2 , column = 1, ipadx = btnIpadx , ipady = btnIpady )

       E = Button(self,text = 'E' , width = btnWidth, command = lambda : press('E'))
       E.grid(row = 2 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       R = Button(self,text = 'R' , width = btnWidth, command = lambda : press('R'))
       R.grid(row = 2 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       T = Button(self,text = 'T' , width = btnWidth, command = lambda : press('T'))
       T.grid(row = 2 , column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       Y = Button(self,text = 'Y' , width = btnWidth, command = lambda : press('Y'))
       Y.grid(row = 2 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       U = Button(self,text = 'U' , width = btnWidth, command = lambda : press('U'))
       U.grid(row = 2 , column = 6, ipadx = btnIpadx, ipady = btnIpady )

       I = Button(self,text = 'I' , width = btnWidth, command = lambda : press('I'))
       I.grid(row = 2 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       O = Button(self,text = 'O' , width = btnWidth, command = lambda : press('O'))
       O.grid(row = 2 , column = 8, ipadx = btnIpadx, ipady = btnIpady )

       P = Button(self,text = 'P' , width = btnWidth, command = lambda : press('P'))
       P.grid(row = 2 , column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       
       #Row 3



       A = Button(self,text = 'A' , width = btnWidth, command = lambda : press('A'))
       A.grid(row = 3 , column = 0, ipadx = btnIpadx , ipady = btnIpady)



       S = Button(self,text = 'S' , width = btnWidth, command = lambda : press('S'))
       S.grid(row = 3 , column = 1, ipadx = btnIpadx , ipady = btnIpady)

       D = Button(self,text = 'D' , width = btnWidth, command = lambda : press('D'))
       D.grid(row = 3 , column = 2, ipadx = btnIpadx, ipady = btnIpady)

       F = Button(self,text = 'F' , width = btnWidth, command = lambda : press('F'))
       F.grid(row = 3 , column = 3, ipadx = btnIpadx , ipady = btnIpady)


       G = Button(self,text = 'G' , width = btnWidth, command = lambda : press('G'))
       G.grid(row = 3 , column = 4, ipadx = btnIpadx , ipady = btnIpady)


       H = Button(self,text = 'H' , width = btnWidth, command = lambda : press('H'))
       H.grid(row = 3 , column = 5, ipadx = btnIpadx , ipady = btnIpady)


       J = Button(self,text = 'J' , width = btnWidth, command = lambda : press('J'))
       J.grid(row = 3 , column = 6, ipadx = btnIpadx , ipady = btnIpady)


       K = Button(self,text = 'K' , width = btnWidth, command = lambda : press('K'))
       K.grid(row = 3 , column = 7, ipadx = btnIpadx , ipady = btnIpady)

       L = Button(self,text = 'L' , width = btnWidth, command = lambda : press('L'))
       L.grid(row = 3 , column = 8, ipadx = btnIpadx , ipady = btnIpady)


       semi_co = Button(self,text = '.' , width = btnWidth, command = lambda : press('.'))
       semi_co.grid(row = 3 , column = 9, ipadx = btnIpadx , ipady = btnIpady)


       

        # Row 4

       Z = Button(self,text = 'Z' , width = btnWidth, command = lambda : press('Z'))
       Z.grid(row = 4, column = 0, ipadx = btnIpadx , ipady = btnIpady)


       X = Button(self,text = 'X' , width = btnWidth, command = lambda : press('X'))
       X.grid(row = 4, column = 1, ipadx = btnIpadx , ipady = btnIpady)


       C = Button(self,text = 'C' , width = btnWidth, command = lambda : press('C'))
       C.grid(row = 4, column = 2, ipadx = btnIpadx , ipady = btnIpady)


       V = Button(self,text = 'V' , width = btnWidth, command = lambda : press('V'))
       V.grid(row = 4, column = 3, ipadx = btnIpadx , ipady = btnIpady)

       B = Button(self, text= 'B' , width = btnWidth , command = lambda : press('B'))
       B.grid(row = 4, column = 4 , ipadx = btnIpadx ,ipady = btnIpady)


       N = Button(self,text = 'N' , width = btnWidth, command = lambda : press('N'))
       N.grid(row = 4, column = 5, ipadx = btnIpadx , ipady = btnIpady)


       M = Button(self,text = 'M' , width = btnWidth, command = lambda : press('M'))
       M.grid(row = 4, column = 6, ipadx = btnIpadx , ipady = btnIpady)



      

       slas = Button(self,text = '/' , width = btnWidth, command = lambda : press('/'))
       slas.grid(row = 4, column = 7, ipadx = btnIpadx , ipady = btnIpady)


       q_mark = Button(self,text = '?' , width = btnWidth, command = lambda : press('?'))
       q_mark.grid(row = 4, column = 8, ipadx = btnIpadx , ipady = btnIpady)


       coma = Button(self,text = ',' , width = btnWidth, command = lambda : press(','))
       coma.grid(row = 4, column = 9, ipadx = btnIpadx , ipady = btnIpady)

       #Row 5
       dot = Button(self,text = '.' , width = btnWidth, command = lambda : press('.'))
       dot.grid(row = 5, column = 6, ipadx = btnIpadx , ipady = btnIpady)

       at = Button (self, text = '@', width = btnWidth, command = lambda : press('@'))
       at.grid(row = 5, column = 5, ipadx = btnIpadx , ipady = btnIpady)
        
        #Row 6

       space = Button(self,text = 'Space' , width = 7, command = lambda : press(' '))
       space.grid(row = 5, column = 3, columnspan = 2 , ipadx = 6 , ipady = 3)

       open_b = Button(self,text = '(' , width = btnWidth, command = lambda : press('('))
       open_b.grid(row = 5 , column = 0 , ipadx = btnIpadx , ipady = btnIpady)

       close_b = Button(self,text = ')' , width = btnWidth, command = lambda : press(')'))
       close_b.grid(row = 5 , column = 1 , ipadx = btnIpadx , ipady = btnIpady)
               
       hasht = Button(self,text = '#' , width = btnWidth, command = lambda : press('#'))
       hasht.grid(row = 5, column = 2 , ipadx = btnIpadx , ipady = btnIpady)
       
       bkSpace = Button(self, text = '<--', width = btnWidth, command = bkSpc)
       bkSpace.grid(row = 5, column = 8, ipadx = 2, ipady = btnIpady)

       clear = Button(self,text = 'Clear' , width = btnWidth, command = clrTxt)
       clear.grid(row = 5, column = 9, ipadx = btnIpadx , ipady = btnIpady)

       d_colon = Button(self,text = '"' , width = btnWidth, command = lambda : press('"'))
       d_colon.grid(row = 5, column = 6, ipadx = btnIpadx , ipady = btnIpady)


       enter = Button(self,text = 'Enter' , width = btnWidth, command = enterKey)
       enter.grid(row = 5, column = 7, ipadx = btnIpadx , ipady = btnIpady)
       
       #Row 7
       
       
       dollar = Button(self,text = '$' , width = btnWidth, command = lambda : press('$'))
       dollar.grid(row = 6, column = 0 , ipadx = btnIpadx , ipady = btnIpady)
       
       plus = Button(self,text = '+' , width = btnWidth, command = lambda : press('+'))
       plus.grid(row = 6, column = 1 , ipadx = btnIpadx , ipady = btnIpady)
       
       minus = Button(self,text = '-' , width = btnWidth, command = lambda : press('-'))
       minus.grid(row = 6, column = 2 , ipadx = btnIpadx , ipady = btnIpady)
       
       excl = Button(self,text = '!' , width = btnWidth, command = lambda : press('!'))
       excl.grid(row = 6, column = 3 , ipadx = btnIpadx , ipady = btnIpady)
       
       underscore = Button(self,text = '_' , width = btnWidth, command = lambda : press('_'))
       underscore.grid(row = 6, column = 4 , ipadx = btnIpadx , ipady = btnIpady)
       
       left = Button(self,text = '<' , width = btnWidth, command = lambda : press('<'))
       left.grid(row = 6, column = 5 , ipadx = btnIpadx , ipady = btnIpady)
       
       right = Button(self,text = '>' , width = btnWidth, command = lambda : press('>'))
       right.grid(row = 6, column = 6 , ipadx = btnIpadx , ipady = btnIpady)
       
       delete = Button(self,text = 'Del' , width = btnWidth, command =  delete)
       delete.grid(row =6, column = 7 , ipadx = btnIpadx , ipady = btnIpady)
       
       okay = Button(self,text = 'OK' , width = 7, command =  OK)
       okay.grid(row = 6, column = 8, columnspan = 9, ipadx = btnIpadx , ipady = btnIpady)
       

class upLoadPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid_columnconfigure(3, weight=1)
       self.grid_rowconfigure(7, weight=1)
       varClass = StringVar()
       nameID = ("Name: " + usrSql + "                                    " + "User ID: " + str(userID))
       label = tk.Label(self, text=nameID)
       label.grid(row=0, column=1, columnspan=14)
       
       lblfrom = tk.Label(self, text='From')
       lblfrom.grid(row=1, column=3)
       lblto = tk.Label(self, text='To')
       lblto.grid(row=4, column=3)
       lblYear = tk.Label(self, text='Year:')
       lblYear.grid(row=2, column=0)
       
       lblMonth = tk.Label(self, text='Mon:')
       lblMonth.grid(row=2, column=2)
       
       lblDay = tk.Label(self, text='Day:')
       lblDay.grid(row=2, column=4)
       
       lblHour = tk.Label(self, text='Hour:')
       lblHour.grid(row=3, column=0)
       
       lblMinute = tk.Label(self, text='Min:')
       lblMinute.grid(row=3, column=2)
       
       lblSecond = tk.Label(self, text='Sec:')
       lblSecond.grid(row=3, column=4)
       
       
       
       lblYear1 = tk.Label(self, text='Year:')
       lblYear1.grid(row=5, column=0)
       
       lblMonth1 = tk.Label(self, text='Mon:')
       lblMonth1.grid(row=5, column=2)
       
       lblDay1 = tk.Label(self, text='Day:')
       lblDay1.grid(row=5, column=4)
       
       lblHour1 = tk.Label(self, text='Hour:')
       lblHour1.grid(row=6, column=0)
       
       lblMinute1 = tk.Label(self, text='Min:')
       lblMinute1.grid(row=6, column=2)
       
       lblSecond1 = tk.Label(self, text='Sec:')
       lblSecond1.grid(row=6, column=4)
       
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
       
       comboYears = ttk.Combobox(self, values = years, width = 4, state="readonly")
       comboYears.grid(row = 2, column = 1)
       comboYears.current(0)
       
       comboMonths = ttk.Combobox(self, values = months, width = 4, state="readonly")
       comboMonths.grid(row = 2, column = 3)
       comboMonths.current(0)

       comboGlobal = ttk.Combobox(self, values = thirtyOne, width = 4, state="readonly")
       comboGlobal.grid(row = 2, column = 5)
       comboGlobal.current(0)

       comboHour = ttk.Combobox(self, values = hour, width = 4, state="readonly")
       comboHour.grid(row = 3, column = 1)
       comboHour.current(0)

       comboMinute = ttk.Combobox(self, values = minute, width = 4, state="readonly")
       comboMinute.grid(row = 3, column = 3)
       comboMinute.current(0)

       comboSecond = ttk.Combobox(self, values = second, width = 4, state="readonly")
       comboSecond.grid(row = 3, column = 5)
       comboSecond.current(0)


       comboYears1 = ttk.Combobox(self, values = years, width = 4, state="readonly")
       comboYears1.grid(row = 5, column = 1)
       comboYears1.current(0)

       comboMonths1 = ttk.Combobox(self, values = months, width = 4, state="readonly")
       comboMonths1.grid(row = 5, column = 3)
       comboMonths1.current(0)

       comboGlobal1 = ttk.Combobox(self, values = thirtyOne, width = 4, state="readonly")
       comboGlobal1.grid(row = 5, column = 5)
       comboGlobal1.current(1)

       comboHour1 = ttk.Combobox(self, values = hour, width = 4, state="readonly")
       comboHour1.grid(row = 6, column = 1)
       comboHour1.current(0)

       comboMinute1 = ttk.Combobox(self, values = minute, width = 4, state="readonly")
       comboMinute1.grid(row = 6, column = 3)
       comboMinute1.current(0)

       comboSecond1 = ttk.Combobox(self, values = second, width = 4, state="readonly")
       comboSecond1.grid(row = 6, column = 5)
       comboSecond1.current(0)
       
       rad1=Radiobutton(self, text = "Class A", variable = varClass, value = 'a')
       rad2=Radiobutton(self, text = "Class B", variable = varClass, value = 'b')
       rad1.grid(row=4, column=6)
       rad2.grid(row=5, column=6)
       
       def callbackYears(eventObject):
            #delCombo()
           #global comboGlobal
           if (((int(comboYears.get()) % 4 == 0 and int(comboYears.get()) % 100 != 0) or int(comboYears.get()) % 400 == 0) and comboMonths.get() == 'Feb'):
               comboGlobal.config(values = leapFeb)
               comboGlobal.current(0)
           elif(comboMonths.get()=='Feb'):
               comboGlobal.config(values = feb)
               comboGlobal.current(0)
           elif (comboMonths.get()=='Jan' or comboMonths.get()=='Mar' or comboMonths.get()=='May' or comboMonths.get()=='Jul' or comboMonths.get()=='Aug' or comboMonths.get()=='Oct' or comboMonths.get()=='Dec'):
               comboGlobal.config(values = thirtyOne)
               comboGlobal.current(0)
           else:
               comboGlobal.config(values = thirty)
               comboGlobal.current(0)

       def callbackYears1(eventObject):
           print('in years 1')
            #delCombo()
           #global comboGlobal1
           if (((int(comboYears1.get()) % 4 == 0 and int(comboYears1.get()) % 100 != 0) or int(comboYears1.get()) % 400 == 0) and comboMonths1.get() == 'Feb'):
               comboGlobal1.config(values = leapFeb)
               comboGlobal1.current(0)
           elif(comboMonths1.get()=='Feb'):
               comboGlobal1.config(values = feb)
               comboGlobal1.current(0)
           elif (comboMonths1.get()=='Jan' or comboMonths1.get()=='Mar' or comboMonths1.get()=='May' or comboMonths1.get()=='Jul' or comboMonths1.get()=='Aug' or comboMonths1.get()=='Oct' or comboMonths1.get()=='Dec'):
               comboGlobal1.config(values = thirtyOne)
               comboGlobal1.current(0)
           else:
               comboGlobal1.config(values = thirty)
               comboGlobal1.current(0)


       comboYears.bind("<<ComboboxSelected>>", callbackYears)
       comboMonths.bind("<<ComboboxSelected>>", callbackYears)

       comboYears1.bind("<<ComboboxSelected>>", callbackYears1)
       comboMonths1.bind("<<ComboboxSelected>>", callbackYears1)
       
       def takeToAccP():
           accP = accountPage(self)
           accP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       bkBtn = tk.Button(self, text="Back", command = takeToAccP)
       bkBtn.grid(row=13, column=0)
       
       def browseImg():
           #root.filename = filedialog.askopenfilename(initialdir="/home/pi/Pictures", title="Select", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg"), ("all files", "*.*")))
           #lbl['text'] = root.filename
           global bindata
           root.filename =  filedialog.askopenfilename(initialdir = "/media/pi/DATA/",title = "Select Image",filetypes = (("jpeg","*.jpg"),("All files","*.*")))
           if not root.filename:
               tk.messagebox.showinfo(title='Info', message='No Image Selected!')
               print ("Nooo")
           else:
               print("Yes")
               print(root.filename)
               with open(root.filename,'rb') as f:
                   #cursor.execute("INSERT INTO images(id, imageFile) SELECT NEWID(), BulkColumn FROM OPENROWSET(BULK  'home/pi/Pictures/Rings.png', SINGLE_BLOB) as f")
                   bindata = f.read()
               
       def browseTxt():
           eTxt = enterText(self)
           eTxt.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
           
       def upLoadAll():
           if (varClass.get()==''):
               messagebox.showerror('Error', 'Class not Seleted!')
           elif (text.isspace() == 1 or text == ''):
               messagebox.showerror('Error', 'Text is empty!')
           else:
               
               
               #cursor.execute("insert into images(id, imageFile) select 99, BulkColumn from openrowset(bulk '/home/pi/Pictures/FJq57NB.png', single_blob) as f")
               #cursor.execute("insert into images(id, imageFile) values (NEWID(), ?)",(bindata[0]))
               #cursor.execute("insert into ads(userID, active, cost, startd, endd, adText, adIMG) values (?,?,?,?,?,?,?)",(userID, 1, 5, now.date(), now.date(), 'sdfasdfasdfaeffafasdfasdfasdfasd', pyodbc.Binary(bindata)))   varClass.get()
               
               startd = (comboYears.get()+'-'+comboMonths.get()+'-'+comboGlobal.get()+' '+comboHour.get()+':'+comboMinute.get()+':'+comboSecond.get())
               endd = (comboYears1.get()+'-'+comboMonths1.get()+'-'+comboGlobal1.get()+' '+comboHour1.get()+':'+comboMinute1.get()+':'+comboSecond1.get())
               dateS = datetime.datetime(int(comboYears.get()), int(monthDict[comboMonths.get()]), int(comboGlobal.get()), int(comboHour.get()), int(comboMinute.get()), int(comboSecond.get()))
               dateE = datetime.datetime(int(comboYears1.get()), int(monthDict[comboMonths1.get()]), int(comboGlobal1.get()), int(comboHour1.get()), int(comboMinute1.get()), int(comboSecond1.get()))
               print((dateE-dateS).total_seconds())
               print(startd+'      '+endd)
               costB = (((dateE-dateS).total_seconds()) /10000)
               costA = (((dateE-dateS).total_seconds()) /2000)
               print (costB)
               print("from " + comboYears.get() + "/" + str(monthDict[comboMonths.get()])+"/"+ comboGlobal.get()+"    " +comboHour.get()+":"+comboMinute.get()+":"+comboSecond.get())
               if ((dateE-dateS).total_seconds() < 0):
                   messagebox.showerror('Error', 'Start Date is bigger than End Date!')
               else:
                   try:
                       cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)

                       cursor = cnxn.cursor()
                       if (varClass.get=='a'):
                           cursor.execute('insert into a_class_ad(userid, cost, startd, endd, adstatus, adtxt, adimg) values (%s, %s, %s, %s, %s, %s, %s)', (userID, costA, dateS, dateE, 2, text, bindata))
                       elif (varClass.get()=='b'):
                           cursor.execute('insert into b_class_ad(userid, cost, startd, endd, adstatus, adtxt, adimg) values (%s, %s, %s, %s, %s, %s, %s)', (userID, costB, dateS, dateE, 2, text, bindata))
                       cnxn.commit()
                   except (pymysql.Error) as e:
                       messagebox.showerror('Error', e)
                       return None
                   finally:
                       cnxn.close()
       
       
       brwsImgBtn = Button(self, text = "Image", command = browseImg, height=4, width=10)
       brwsImgBtn.grid(row=13, column=1, columnspan=5)
       brwsTxtBtn = Button(self, text = "Text", command = browseTxt, height=4, width=10)
       brwsTxtBtn.grid(row=12, column=1,columnspan=5)
       uLoad = Button(self, text = "Upload", command = upLoadAll, height=4, width=10)
       uLoad.grid(row=13, column=6, columnspan=2)
       bkBtn = tk.Button(self, text="<--Back", command = takeToAccP, height=4, width=10)
       bkBtn.grid(row=13, column=0)

class refreshPage(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       sP = statusPage(self)
       sP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

class statusPage(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       nameID = ("Name: " + usrSql + "            " + "User ID: " + str(userID))
       label = tk.Label(self, text=nameID)
       label.pack(side="top", fill="both", expand=True)
       
       try:
           cnxn = pymysql.connect(sqlServer,sqlServerUsr,sqlServerPass,databaseName)
           mycursor = cnxn.cursor()
           
           mycursor.execute("SELECT adid, cost, startd, endd, adstatus FROM b_class_ad where userid = %s", (userID))
           
           myresult = mycursor.fetchall()
           
           mycursor.execute("SELECT adid, cost, startd, endd, adstatus FROM a_class_ad where userid = %s", (userID))
           myresult1 = mycursor.fetchall()
           
           cols = ('Id','Cost','Start Date','End Date', 'Class', 'Status')
           listBox = ttk.Treeview(self, columns=cols, show='headings')
           label = ttk.Label(self, text="High Scores", font=("Arial",30))
           for col in cols:
               listBox.heading(col, text=col)
               listBox.pack(side="top", fill="both", expand=True)
           tempList = []
           
           for x in myresult:
               if (x[4] == 1):
                   tempList.append([x[0], x[1] ,x[2], x[3], 'B', 'Active'])
               elif (x[4] == 0):
                   tempList.append([x[0], x[1] ,x[2], x[3], 'B','Expired'])
               else:
                   tempList.append([x[0], x[1] ,x[2], x[3], 'B','To be Posted'])
                   
           for e in myresult1:
               if (e[4] == 1):
                   print(e[4])
                   tempList.append([e[0], e[1] ,e[2], e[3], 'A', 'Active'])
               elif (e[4] == 0):
                   print(e[4])
                   tempList.append([e[0], e[1] ,e[2], e[3], 'A','Expired'])
               else:
                   print(e[4])
                   tempList.append([e[0], e[1] ,e[2], e[3], 'A','To be Posted'])
                   
           tempList.sort(key=lambda e: e[2], reverse=False)
           
           for i, (adid, cost, sdate, edate, classs, status) in enumerate(tempList, start=1):
               listBox.insert("", "end", values=(adid, cost, sdate, edate, classs, status))
               listBox.column('#1', minwidth=20, width = 12, stretch = True)
               listBox.column('#2', minwidth=20, width = 25, stretch = True)
               listBox.column('#3', minwidth=20, width = 120, stretch = True)
               listBox.column('#4', minwidth=20, width = 120, stretch = True)
               listBox.column('#5', minwidth=20, width = 25, stretch = True)
               listBox.column('#6', minwidth=20, width = 80, stretch = True)
       
       except (pymysql.Error) as e:
           messagebox.showerror('Error', e)
           return None
       finally:
           cnxn.close()
       
       def delAd():
           #curItem = listBox.focus()
           curItem = listBox.item(listBox.focus())
           cell_value = curItem['values']
           print(cell_value)
           try:
               cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)

               cursor = cnxn.cursor()
               cursor.execute("UPDATE "+curItem['values'][4].lower()+"_class_ad SET adstatus = '0' WHERE adid = %s;", (curItem['values'][0]))
               
               cnxn.commit()
               
               
               
           except (pymysql.Error) as e:
               messagebox.showerror('Error', e)
               return None
           finally:
               cnxn.close()
               rfP = refreshPage(self)
               rfP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       def backOut():
           accP = accountPage(self)
           accP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       btnDelAd = Button(self, text='Delete', command=delAd)
       btnDelAd.pack(side='right')
       bk= Button(self, text='<--Back', command=backOut)
       bk.pack(side='left')
       


class accountPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Account Page in")
       
       nameID = ("Name: " + usrSql + "              " + "User ID: " + str(userID))
       label = tk.Label(self, text=nameID)
       label.pack(side="top", fill="both", expand=True)
       
       label.pack(side="top", fill="both", expand=True)
       def takeToUploadP():
           uP = upLoadPage(self)
           uP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       def logOut():
           global usrSql
           global passSql
           global usrN
           global passw
           usrSql = ""
           passSql = ""
           usrN = "."
           passw = "."
           label.config(text="Logged Out!")
           up = tk.Button(self, text="Upload", command=regLogPage.lift)
           up.pack(side="left")
           rtrn = regLogPage(self)
           rtrn.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       def takeToStatusPage():
           sP = statusPage(self)
           sP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       upBtn = Button(self, text = "Upload", command = takeToUploadP, width=17, height=8)
       upBtn.pack(side="left")
       statusBtn = Button(self, text = "Status", command = takeToStatusPage, width=17, height=8)
       statusBtn.pack(side="left")
       logout = Button(self, text = "Logout", command = logOut, width=17, height=8)
       logout.pack(side="left")


index1=1
class RegPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid_columnconfigure(0, weight=1)
       nameTb = Entry(self)
       nameTb.grid(row=0, column=2, columnspan=6)
       emailTb = Entry(self)
       emailTb.grid(row=1, column=2, columnspan=6)
       passTb = Entry(self)
       passTb.grid(row=2, column=2, columnspan=6)
       confirmPassTb = Entry(self)
       confirmPassTb.grid(row=3, column=2, columnspan=6)
       
       def registerAcc():
           name = nameTb.get()
           email = emailTb.get()
           password = passTb.get()
           confirmPass = confirmPassTb.get()
           print(name)
           print(email)
           print(password)
           print(confirmPass)
           cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)
           cursor = cnxn.cursor()
           cursor.execute("SELECT email FROM usert WHERE email LIKE %s", (email))
           row = cursor.fetchone()
           if (row is None and password == confirmPass):
               cursor.execute("insert into usert(name, pass, email) values (%s, %s, %s)", (name, password, email))
               cursor.execute("insert into rstpass(email, code, date) values (%s, LPAD(FLOOR(RAND() * 999999.99), 6, '0'), now())", (email))
               cnxn.commit()
               cnxn.close()
               logP = LogPage(self)
               logP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       btnWidth = 2
       btnIpadx = 2
       btnIpady = 2
       
       def press(num, entry):
           entry.insert(tk.INSERT, num.lower())
           #content = adTxt.get(1.0, "end-1c")
           #text = content
           #print(content)
           entry.xview_moveto(1)
           
       def clrTxt():
           if (index1 == 1):
               nameTb.delete('0', END)
           elif (index1 == 2):
               email.delete('0', END)
           elif (index1 == 3):
               passTb.delete('0', END)
           elif (index1 == 4):
               confirmPassTb.delete('0', END)
       
       def delete():
           if (index1 == 1):
               nameTb.delete('%s' % tk.INSERT)
           elif (index1 == 2):
               emailTb.delete('%s' % tk.INSERT)
           elif (index1 == 3):
               passTb.delete('%s' % tk.INSERT)
           elif (index1 == 4):
               confirmPassTb.delete('%s' % tk.INSERT)
       
       def changeIndex(event, cngdIn):
           global index1
           index1 = cngdIn
           print(index1)
       
       def returnUsrTb(b):
           if (b == 1):
               print('why the fuck::::'+str(b))
               return nameTb
           elif (b == 2):
               print('why the fuck::::'+str(b))
               return emailTb
           elif (b == 3):
               print('why the fuck::::'+str(b))
               return passTb
           elif (b == 4):
               print('why the fuck::::'+str(b))
               return confirmPassTb
        
       def rLPage():
           rlP = regLogPage(self)
           rlP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       bk = Button(self,text = '<--Back', command=rLPage)
       bk.grid(row = 0 , column = 0, columnspan=2, rowspan=2)
       
       one = Button(self,text = '1' , width = btnWidth, command = lambda : press('1',returnUsrTb(index1)))
       one.grid(row = 4 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       two = Button(self,text = '2' , width = btnWidth, command = lambda : press('2',returnUsrTb(index1)))
       two.grid(row = 4, column = 1, ipadx = btnIpadx , ipady = btnIpady )

       three = Button(self,text = '3' , width = btnWidth, command = lambda : press('3',returnUsrTb(index1)))
       three.grid(row = 4 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       four = Button(self,text = '4' , width = btnWidth, command = lambda : press('4',returnUsrTb(index1)))
       four.grid(row = 4 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       five = Button(self,text = '5' , width = btnWidth, command = lambda : press('5',returnUsrTb(index1)))
       five.grid(row = 4, column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       six = Button(self,text = '6' , width = btnWidth, command = lambda : press('6',returnUsrTb(index1)))
       six.grid(row = 4 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       seven = Button(self,text = '7' , width = btnWidth, command = lambda : press('7',returnUsrTb(index1)))
       seven.grid(row = 4, column = 6, ipadx = btnIpadx, ipady = btnIpady )

       eight = Button(self,text = '8' , width = btnWidth, command = lambda : press('8',returnUsrTb(index1)))
       eight.grid(row = 4 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       nine = Button(self,text = '9' , width = btnWidth, command = lambda : press('9',returnUsrTb(index1)))
       nine.grid(row = 4 , column = 8, ipadx = btnIpadx, ipady = btnIpady )

       zero = Button(self,text = '0' , width = btnWidth, command = lambda : press('0',returnUsrTb(index1)))
       zero.grid(row = 4 , column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       #Row 2
       
       q = Button(self,text = 'Q' , width = btnWidth, command = lambda : press('Q',returnUsrTb(index1)))
       q.grid(row = 5 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       w = Button(self,text = 'W' , width = btnWidth, command = lambda : press('W',returnUsrTb(index1)))
       w.grid(row = 5 , column = 1, ipadx = btnIpadx , ipady = btnIpady )

       E = Button(self,text = 'E' , width = btnWidth, command = lambda : press('E',returnUsrTb(index1)))
       E.grid(row = 5 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       R = Button(self,text = 'R' , width = btnWidth, command = lambda : press('R',returnUsrTb(index1)))
       R.grid(row = 5 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       T = Button(self,text = 'T' , width = btnWidth, command = lambda : press('T',returnUsrTb(index1)))
       T.grid(row = 5 , column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       Y = Button(self,text = 'Y' , width = btnWidth, command = lambda : press('Y',returnUsrTb(index1)))
       Y.grid(row = 5 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       U = Button(self,text = 'U' , width = btnWidth, command = lambda : press('U',returnUsrTb(index1)))
       U.grid(row = 5 , column = 6, ipadx = btnIpadx, ipady = btnIpady )

       I = Button(self,text = 'I' , width = btnWidth, command = lambda : press('I',returnUsrTb(index1)))
       I.grid(row = 5 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       O = Button(self,text = 'O' , width = btnWidth, command = lambda : press('O',returnUsrTb(index1)))
       O.grid(row = 5, column = 8, ipadx = btnIpadx, ipady = btnIpady )

       P = Button(self,text = 'P' , width = btnWidth, command = lambda : press('P',returnUsrTb(index1)))
       P.grid(row = 5, column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       
       #Row 3



       A = Button(self,text = 'A' , width = btnWidth, command = lambda : press('A',returnUsrTb(index1)))
       A.grid(row = 6 , column = 0, ipadx = btnIpadx , ipady = btnIpady)



       S = Button(self,text = 'S' , width = btnWidth, command = lambda : press('S',returnUsrTb(index1)))
       S.grid(row = 6, column = 1, ipadx = btnIpadx , ipady = btnIpady)

       D = Button(self,text = 'D' , width = btnWidth, command = lambda : press('D',returnUsrTb(index1)))
       D.grid(row = 6 , column = 2, ipadx = btnIpadx, ipady = btnIpady)

       F = Button(self,text = 'F' , width = btnWidth, command = lambda : press('F',returnUsrTb(index1)))
       F.grid(row = 6 , column = 3, ipadx = btnIpadx , ipady = btnIpady)


       G = Button(self,text = 'G' , width = btnWidth, command = lambda : press('G',returnUsrTb(index1)))
       G.grid(row = 6 , column = 4, ipadx = btnIpadx , ipady = btnIpady)


       H = Button(self,text = 'H' , width = btnWidth, command = lambda : press('H',returnUsrTb(index1)))
       H.grid(row = 6 , column = 5, ipadx = btnIpadx , ipady = btnIpady)


       J = Button(self,text = 'J' , width = btnWidth, command = lambda : press('J',returnUsrTb(index1)))
       J.grid(row = 6 , column = 6, ipadx = btnIpadx , ipady = btnIpady)


       K = Button(self,text = 'K' , width = btnWidth, command = lambda : press('K',returnUsrTb(index1)))
       K.grid(row = 6 , column = 7, ipadx = btnIpadx , ipady = btnIpady)

       L = Button(self,text = 'L' , width = btnWidth, command = lambda : press('L',returnUsrTb(index1)))
       L.grid(row = 6 , column = 8, ipadx = btnIpadx , ipady = btnIpady)


       dot = Button(self,text = '.' , width = btnWidth, command = lambda : press('.',returnUsrTb(index1)))
       dot.grid(row = 6 , column = 9, ipadx = btnIpadx , ipady = btnIpady)


       

        # Row 4

       Z = Button(self,text = 'Z' , width = btnWidth, command = lambda : press('Z',returnUsrTb(index1)))
       Z.grid(row = 7, column = 0, ipadx = btnIpadx , ipady = btnIpady)


       X = Button(self,text = 'X' , width = btnWidth, command = lambda : press('X',returnUsrTb(index1)))
       X.grid(row = 7, column = 1, ipadx = btnIpadx , ipady = btnIpady)


       C = Button(self,text = 'C' , width = btnWidth, command = lambda : press('C',returnUsrTb(index1)))
       C.grid(row = 7, column = 2, ipadx = btnIpadx , ipady = btnIpady)


       V = Button(self,text = 'V' , width = btnWidth, command = lambda : press('V',returnUsrTb(index1)))
       V.grid(row = 7, column = 3, ipadx = btnIpadx , ipady = btnIpady)

       B = Button(self, text= 'B' , width = btnWidth , command = lambda : press('B',returnUsrTb(index1)))
       B.grid(row = 7, column = 4 , ipadx = btnIpadx ,ipady = btnIpady)


       N = Button(self,text = 'N' , width = btnWidth, command = lambda : press('N',returnUsrTb(index1)))
       N.grid(row = 7, column = 5, ipadx = btnIpadx , ipady = btnIpady)


       M = Button(self,text = 'M' , width = btnWidth, command = lambda : press('M',returnUsrTb(index1)))
       M.grid(row = 7, column = 6, ipadx = btnIpadx , ipady = btnIpady)



      

       slas = Button(self,text = '/' , width = btnWidth, command = lambda : press('/',returnUsrTb(index1)))
       slas.grid(row = 7, column = 7, ipadx = btnIpadx , ipady = btnIpady)


       q_mark = Button(self,text = '?' , width = btnWidth, command = lambda : press('?',returnUsrTb(index1)))
       q_mark.grid(row = 7, column = 8, ipadx = btnIpadx , ipady = btnIpady)


       coma = Button(self,text = ',' , width = btnWidth, command = lambda : press(',',returnUsrTb(index1)))
       coma.grid(row = 7, column = 9, ipadx = btnIpadx , ipady = btnIpady)

       #Row 5
       dot = Button(self,text = '.' , width = btnWidth, command = lambda : press('.',returnUsrTb(index1)))
       dot.grid(row = 8, column = 6, ipadx = btnIpadx , ipady = btnIpady)

       at = Button (self, text = '@', width = btnWidth, command = lambda : press('@',returnUsrTb(index1)))
       at.grid(row = 8, column = 5, ipadx = btnIpadx , ipady = btnIpady)
        
        #Row 6

       space = Button(self,text = 'Space' , width = 7, command = lambda : press(' ',returnUsrTb(index1)))
       space.grid(row = 8, column = 3, columnspan = 2 , ipadx = 6 , ipady = 3)

       open_b = Button(self,text = '(' , width = btnWidth, command = lambda : press('(',returnUsrTb(index1)))
       open_b.grid(row = 8 , column = 0 , ipadx = btnIpadx , ipady = btnIpady)

       close_b = Button(self,text = ')' , width = btnWidth, command = lambda : press(')',returnUsrTb(index1)))
       close_b.grid(row = 8 , column = 1 , ipadx = btnIpadx , ipady = btnIpady)
               
       hasht = Button(self,text = '#' , width = btnWidth, command = lambda : press('#',returnUsrTb(index1)))
       hasht.grid(row = 8, column = 2 , ipadx = btnIpadx , ipady = btnIpady)

       clear = Button(self,text = 'Clear' , width = btnWidth, command = clrTxt)
       clear.grid(row = 8, column = 7, ipadx = btnIpadx , ipady = btnIpady)

       d_colon = Button(self,text = '"' , width = btnWidth, command = lambda : press('"',returnUsrTb(index1)))
       d_colon.grid(row = 8, column = 6, ipadx = btnIpadx , ipady = btnIpady)
       
       #Row 7
       
       
       dollar = Button(self,text = '$' , width = btnWidth, command = lambda : press('$',returnUsrTb(index1)))
       dollar.grid(row = 9, column = 0 , ipadx = btnIpadx , ipady = btnIpady)
       
       plus = Button(self,text = '+' , width = btnWidth, command = lambda : press('+',returnUsrTb(index1)))
       plus.grid(row = 9, column = 1 , ipadx = btnIpadx , ipady = btnIpady)
       
       minus = Button(self,text = '-' , width = btnWidth, command = lambda : press('-',returnUsrTb(index1)))
       minus.grid(row = 9, column = 2 , ipadx = btnIpadx , ipady = btnIpady)
       
       excl = Button(self,text = '!' , width = btnWidth, command = lambda : press('!',returnUsrTb(index1)))
       excl.grid(row = 9, column = 3 , ipadx = btnIpadx , ipady = btnIpady)
       
       underscore = Button(self,text = '_' , width = btnWidth, command = lambda : press('_',returnUsrTb(index1)))
       underscore.grid(row = 9, column = 4 , ipadx = btnIpadx , ipady = btnIpady)
       
       left = Button(self,text = '<' , width = btnWidth, command = lambda : press('<',returnUsrTb(index1)))
       left.grid(row = 9, column = 5 , ipadx = btnIpadx , ipady = btnIpady)
       
       right = Button(self,text = '>' , width = btnWidth, command = lambda : press('>',returnUsrTb(index1)))
       right.grid(row = 9, column = 6 , ipadx = btnIpadx , ipady = btnIpady)
       
       delete = Button(self,text = 'Del' , width = btnWidth, command =  delete)
       delete.grid(row =9, column = 7 , ipadx = btnIpadx , ipady = btnIpady)
       nameTb.bind("<Button-1>", lambda event: changeIndex(event, 1))
       emailTb.bind("<Button-1>", lambda event: changeIndex(event, 2))
       passTb.bind("<Button-1>", lambda event: changeIndex(event, 3))
       confirmPassTb.bind("<Button-1>", lambda event: changeIndex(event, 4))
       
       registerBtn = Button(self, text = "Register", command = registerAcc, height=3, width=5)
       registerBtn.grid(row=8, column=8, columnspan=2, rowspan=2)
       

class ChangePassPage(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
               
       #label = tk.Label(self, text="This is page 1")
       #label.pack(side="top", fill="both", expand=True)
       self.grid_columnconfigure(0, weight=1)
       #self.grid_rowconfigure(0, weight=1)
       email = Entry(self)
       email.grid(column = 0, row=2, columnspan = 4)
       email.insert(0, 'Enter Email')
       
       code = Entry(self)
       code.grid(column = 5, row=2, columnspan = 4)
       code.insert(0, 'Enter code')
       pass1 = Entry(self)
       pass1.grid(column = 5, row=3, columnspan = 4)
       pass1.insert(0, 'Enter new pass')
       pass2 = Entry(self)
       pass2.grid(column = 5, row=4, columnspan = 4)
       pass2.insert(0, 'Confirm pass')
       row=''
       
       def deleteTB(event, entry):
           if (entry.get() == 'Enter Email' or entry.get() == 'Enter code' or entry.get() == 'Enter new pass' or entry().get() == 'Confirm pass'):
               entry.delete(0, END)
       
       def sendCode():
           try:
               cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)
               
               cursor = cnxn.cursor()
               
               cursor.execute("SELECT email from rstpass where email = %s", (email.get()))
               row = cursor.fetchone()[0]
               usr = row
               
               if (email.get() == usr):
                   global codeVal
                   print('in if')
                   cursor.execute("update rstpass SET code = LPAD(FLOOR(RAND() * 999999.99), 6, '0'), date = now() where email = %s", (email.get()))
                   cnxn.commit()
                   context = ssl.create_default_context()
                   cursor.execute("SELECT code FROM rstpass WHERE email LIKE %s", (email.get()))
                   row = cursor.fetchone()[0]
                   codeVal = row
                   print(row)
                   message = """\
                    Subject: EZ Ads Password Result

                    The password Reset Code si: """ + str(row)
                   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                       server.login(sender_email, 'Ezadsnoreply3')
                       server.sendmail(sender_email, email.get(), message)
                       
           except (pymysql.Error) as e:
               messagebox.showerror('Error', e)
               return None
            
           finally:
               cnxn.close()
       def rstPass():
           print(pass1.get())
           print(pass2.get())
           print(code.get())
           print(codeVal)
           if (code.get() == str(codeVal) and pass1.get() == pass2.get()):
               try:
                   cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)
                   
                   cursor = cnxn.cursor()
                   
                   cursor.execute("update usert set pass = %s where email = %s", (pass1.get(), email.get()))
                   cnxn.commit()
               
                   
                   context = ssl.create_default_context()
                   print(row)
                   message = """\
                    Subject: EZ Ads Password Result

                    Your EZ Ads password has been successfully reset!"""
                   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                       server.login(sender_email, 'Ezadsnoreply3')
                       server.sendmail(sender_email, email.get(), 'subbbb', message)
                       
               except (pymysql.Error) as e:
                   messagebox.showerror('Error', e)
                   return None
                
               finally:
                   cnxn.close()
                   email.delete(0, END)
                   pass1.delete(0, END)
                   pass2.delete(0, END)
                   code.delete(0, END)
                   
       sendCodeBtn = Button(self, text='Send Code', command = sendCode)
       sendCodeBtn.grid(column=1, row=3, columnspan=2)
       rstBtn = Button(self, text='Reset', command = rstPass, height=3, width=6)
       rstBtn.grid(column=8, row=10, columnspan=2, rowspan=2)
       email.bind("<Button-1>", lambda event: deleteTB(event, email))
       pass1.bind("<Button-1>", lambda event: deleteTB(event, pass1))
       pass2.bind("<Button-1>", lambda event: deleteTB(event, pass2))
       code.bind("<Button-1>", lambda event: deleteTB(event, code))
       
       btnWidth = 2
       btnIpadx = 2
       btnIpady = 2
       
       def press(num, entry):
           entry.insert(tk.INSERT, num.lower())
           entry.xview_moveto(1)
       
       def clrTxt():
           if (index == 1):
               email.delete('0', END)
           if (index == 2):
               code.delete('0', END)
           if (index == 3):
               pass1.delete('0', END)
           if (index == 4):
               pass2.delete('0', END)
       
       def delete():
           if (index == 1):
               code.delete('%s' % tk.INSERT)
           elif (index == 2):
               email.delete('%s' % tk.INSERT)
           elif (index == 3):
               pass1.delete('%s' % tk.INSERT)
           elif (index == 4):
               pass2.delete('%s' % tk.INSERT)
       
       
       def changeIndex(event, cngdIn):
           global index
           index = cngdIn
           if (index == 1):
               email.delete('0', END)
           if (index == 2):
               code.delete('0', END)
           if (index == 3):
               pass1.delete('0', END)
           if (index == 4):
               pass2.delete('0', END)
       
       def returnUsrTb(b):
           if (b == 1):
               return email
           elif (b == 2):
               return code
           elif (b == 3):
               return pass1
           elif (b == 4):
               return pass2
       
       def logPage():
           logP = LogPage(self)
           logP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       bk = Button(self,text = '<--Back', command=logPage)
       bk.grid(row = 0 , column = 0, columnspan=2)
       
       delBtn = Button(self,text = 'Del' , width = btnWidth, command = lambda : press(delete()))
       delBtn.grid(row = 11 , column = 7, ipadx = btnIpadx, ipady = btnIpady)
       
       one = Button(self,text = '1' , width = btnWidth, command = lambda : press('1',returnUsrTb(index)))
       one.grid(row = 6 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       two = Button(self,text = '2' , width = btnWidth, command = lambda : press('2',returnUsrTb(index)))
       two.grid(row = 6, column = 1, ipadx = btnIpadx , ipady = btnIpady )

       three = Button(self,text = '3' , width = btnWidth, command = lambda : press('3',returnUsrTb(index)))
       three.grid(row = 6 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       four = Button(self,text = '4' , width = btnWidth, command = lambda : press('4',returnUsrTb(index)))
       four.grid(row = 6 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       five = Button(self,text = '5' , width = btnWidth, command = lambda : press('5',returnUsrTb(index)))
       five.grid(row = 6, column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       six = Button(self,text = '6' , width = btnWidth, command = lambda : press('6',returnUsrTb(index)))
       six.grid(row = 6 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       seven = Button(self,text = '7' , width = btnWidth, command = lambda : press('7',returnUsrTb(index)))
       seven.grid(row = 6, column = 6, ipadx = btnIpadx, ipady = btnIpady )

       eight = Button(self,text = '8' , width = btnWidth, command = lambda : press('8',returnUsrTb(index)))
       eight.grid(row = 6 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       nine = Button(self,text = '9' , width = btnWidth, command = lambda : press('9',returnUsrTb(index)))
       nine.grid(row = 6 , column = 8, ipadx = btnIpadx, ipady = btnIpady )

       zero = Button(self,text = '0' , width = btnWidth, command = lambda : press('0',returnUsrTb(index)))
       zero.grid(row = 6 , column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       #Row 2
       
       q = Button(self,text = 'Q' , width = btnWidth, command = lambda : press('Q',returnUsrTb(index)))
       q.grid(row = 7 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       w = Button(self,text = 'W' , width = btnWidth, command = lambda : press('W',returnUsrTb(index)))
       w.grid(row = 7 , column = 1, ipadx = btnIpadx , ipady = btnIpady )

       E = Button(self,text = 'E' , width = btnWidth, command = lambda : press('E',returnUsrTb(index)))
       E.grid(row = 7 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       R = Button(self,text = 'R' , width = btnWidth, command = lambda : press('R',returnUsrTb(index)))
       R.grid(row = 7 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       T = Button(self,text = 'T' , width = btnWidth, command = lambda : press('T',returnUsrTb(index)))
       T.grid(row = 7 , column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       Y = Button(self,text = 'Y' , width = btnWidth, command = lambda : press('Y',returnUsrTb(index)))
       Y.grid(row = 7 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       U = Button(self,text = 'U' , width = btnWidth, command = lambda : press('U',returnUsrTb(index)))
       U.grid(row = 7 , column = 6, ipadx = btnIpadx, ipady = btnIpady )

       I = Button(self,text = 'I' , width = btnWidth, command = lambda : press('I',returnUsrTb(index)))
       I.grid(row = 7 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       O = Button(self,text = 'O' , width = btnWidth, command = lambda : press('O',returnUsrTb(index)))
       O.grid(row = 7, column = 8, ipadx = btnIpadx, ipady = btnIpady )

       P = Button(self,text = 'P' , width = btnWidth, command = lambda : press('P',returnUsrTb(index)))
       P.grid(row = 7, column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       
       #Row 3



       A = Button(self,text = 'A' , width = btnWidth, command = lambda : press('A',returnUsrTb(index)))
       A.grid(row = 8 , column = 0, ipadx = btnIpadx , ipady = btnIpady)



       S = Button(self,text = 'S' , width = btnWidth, command = lambda : press('S',returnUsrTb(index)))
       S.grid(row = 8, column = 1, ipadx = btnIpadx , ipady = btnIpady)

       D = Button(self,text = 'D' , width = btnWidth, command = lambda : press('D',returnUsrTb(index)))
       D.grid(row = 8 , column = 2, ipadx = btnIpadx, ipady = btnIpady)

       F = Button(self,text = 'F' , width = btnWidth, command = lambda : press('F',returnUsrTb(index)))
       F.grid(row = 8 , column = 3, ipadx = btnIpadx , ipady = btnIpady)


       G = Button(self,text = 'G' , width = btnWidth, command = lambda : press('G',returnUsrTb(index)))
       G.grid(row = 8 , column = 4, ipadx = btnIpadx , ipady = btnIpady)


       H = Button(self,text = 'H' , width = btnWidth, command = lambda : press('H',returnUsrTb(index)))
       H.grid(row = 8 , column = 5, ipadx = btnIpadx , ipady = btnIpady)


       J = Button(self,text = 'J' , width = btnWidth, command = lambda : press('J',returnUsrTb(index)))
       J.grid(row = 8 , column = 6, ipadx = btnIpadx , ipady = btnIpady)


       K = Button(self,text = 'K' , width = btnWidth, command = lambda : press('K',returnUsrTb(index)))
       K.grid(row = 8 , column = 7, ipadx = btnIpadx , ipady = btnIpady)

       L = Button(self,text = 'L' , width = btnWidth, command = lambda : press('L',returnUsrTb(index)))
       L.grid(row = 8 , column = 8, ipadx = btnIpadx , ipady = btnIpady)


       dot = Button(self,text = '.' , width = btnWidth, command = lambda : press('.',returnUsrTb(index)))
       dot.grid(row = 8, column = 9, ipadx = btnIpadx , ipady = btnIpady)


       

        # Row 4

       Z = Button(self,text = 'Z' , width = btnWidth, command = lambda : press('Z',returnUsrTb(index)))
       Z.grid(row = 9, column = 0, ipadx = btnIpadx , ipady = btnIpady)


       X = Button(self,text = 'X' , width = btnWidth, command = lambda : press('X',returnUsrTb(index)))
       X.grid(row = 9, column = 1, ipadx = btnIpadx , ipady = btnIpady)
 

       C = Button(self,text = 'C' , width = btnWidth, command = lambda : press('C',returnUsrTb(index)))
       C.grid(row = 9, column = 2, ipadx = btnIpadx , ipady = btnIpady)


       V = Button(self,text = 'V' , width = btnWidth, command = lambda : press('V',returnUsrTb(index)))
       V.grid(row = 9, column = 3, ipadx = btnIpadx , ipady = btnIpady)

       B = Button(self, text= 'B' , width = btnWidth , command = lambda : press('B',returnUsrTb(index)))
       B.grid(row = 9, column = 4 , ipadx = btnIpadx ,ipady = btnIpady)


       N = Button(self,text = 'N' , width = btnWidth, command = lambda : press('N',returnUsrTb(index)))
       N.grid(row = 9, column = 5, ipadx = btnIpadx , ipady = btnIpady)


       M = Button(self,text = 'M' , width = btnWidth, command = lambda : press('M',returnUsrTb(index)))
       M.grid(row = 9, column = 6, ipadx = btnIpadx , ipady = btnIpady)



      

       slas = Button(self,text = '/' , width = btnWidth, command = lambda : press('/',returnUsrTb(index)))
       slas.grid(row = 9, column = 7, ipadx = btnIpadx , ipady = btnIpady)


       q_mark = Button(self,text = '?' , width = btnWidth, command = lambda : press('?',returnUsrTb(index)))
       q_mark.grid(row = 9, column = 8, ipadx = btnIpadx , ipady = btnIpady)


       coma = Button(self,text = ',' , width = btnWidth, command = lambda : press(',',returnUsrTb(index)))
       coma.grid(row = 9, column = 9, ipadx = btnIpadx , ipady = btnIpady)

       #Row 5
       

       at = Button (self, text = '@', width = btnWidth, command = lambda : press('@',returnUsrTb(index)))
       at.grid(row = 10, column = 5, ipadx = btnIpadx , ipady = btnIpady)
        
        #Row 6

       space = Button(self,text = 'Space' , width = 7, command = lambda : press(' ',returnUsrTb(index)))
       space.grid(row = 10, column = 3, columnspan = 2 , ipadx = 6 , ipady = 3)

       open_b = Button(self,text = '(' , width = btnWidth, command = lambda : press('(',returnUsrTb(index)))
       open_b.grid(row = 10 , column = 0 , ipadx = btnIpadx , ipady = btnIpady)

       close_b = Button(self,text = ')' , width = btnWidth, command = lambda : press(')',returnUsrTb(index)))
       close_b.grid(row = 10 , column = 1 , ipadx = btnIpadx , ipady = btnIpady)
               
       hasht = Button(self,text = '#' , width = btnWidth, command = lambda : press('#',returnUsrTb(index)))
       hasht.grid(row = 10, column = 2 , ipadx = btnIpadx , ipady = btnIpady)

       clear = Button(self,text = 'Clear' , width = btnWidth, command = clrTxt)
       clear.grid(row = 10, column = 7, ipadx = btnIpadx , ipady = btnIpady)

       d_colon = Button(self,text = '"' , width = btnWidth, command = lambda : press('"',returnUsrTb(index)))
       d_colon.grid(row = 10, column = 6, ipadx = btnIpadx , ipady = btnIpady)
       
       #Row 7
       
       
       dollar = Button(self,text = '$' , width = btnWidth, command = lambda : press('$',returnUsrTb(index)))
       dollar.grid(row = 11, column = 0 , ipadx = btnIpadx , ipady = btnIpady)
       
       plus = Button(self,text = '+' , width = btnWidth, command = lambda : press('+',returnUsrTb(index)))
       plus.grid(row = 11, column = 1 , ipadx = btnIpadx , ipady = btnIpady)
       
       minus = Button(self,text = '-' , width = btnWidth, command = lambda : press('-',returnUsrTb(index)))
       minus.grid(row = 11, column = 2 , ipadx = btnIpadx , ipady = btnIpady)
       
       excl = Button(self,text = '!' , width = btnWidth, command = lambda : press('!',returnUsrTb(index)))
       excl.grid(row = 11, column = 3 , ipadx = btnIpadx , ipady = btnIpady)
       
       underscore = Button(self,text = '_' , width = btnWidth, command = lambda : press('_',returnUsrTb(index)))
       underscore.grid(row = 11, column = 4 , ipadx = btnIpadx , ipady = btnIpady)
       
       left = Button(self,text = '<' , width = btnWidth, command = lambda : press('<',returnUsrTb(index)))
       left.grid(row =11, column = 5 , ipadx = btnIpadx , ipady = btnIpady)
       
       right = Button(self,text = '>' , width = btnWidth, command = lambda : press('>',returnUsrTb(index)))
       right.grid(row = 11, column = 6 , ipadx = btnIpadx , ipady = btnIpady)
       
       email.bind("<Button-1>", lambda event: changeIndex(event, 1))
       code.bind("<Button-1>", lambda event: changeIndex(event, 2))
       pass1.bind("<Button-1>", lambda event: changeIndex(event, 3))
       pass2.bind("<Button-1>", lambda event: changeIndex(event, 4))
       
index = 2 
class LogPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid_columnconfigure(3, weight=1)
       self.grid_rowconfigure(1, weight=1)
       usrTb = Entry(self, name='usrTb')
       usrTb.grid(row=0, column=2, columnspan=5)
       passTb = Entry(self)
       passTb.grid(row=1, column=2, columnspan=5)
       if (usrN == usrSql and passSql == passw):
           label.config(text="Logged In")
       else:
           #label.config(text="Logged Out")
           print("in else")
       def printCom():
           global usrSql
           global passSql
           global userID
           usrN = usrTb.get()
           passw = passTb.get()
           try:
               cnxn = pymysql.connect(sqlServer, sqlServerUsr, sqlServerPass, databaseName)
               cursor = cnxn.cursor()
               cursor.execute("SELECT email from usert where email = %s and pass = %s", (usrN, passw))
               row = cursor.fetchone()[0]
               usrSql = row
               cursor.execute("SELECT pass from usert where email = %s and pass = %s", (usrN, passw))        
               row = cursor.fetchone()[0]
               passSql = row
               cursor.execute("SELECT id from usert where email = %s and pass = %s", (usrN, passw))        
               row = cursor.fetchone()[0]
               userID = int(row)
               print(usrN)
               print(passw)
               print(usrSql)
               print(passSql)
               if (usrN == usrSql and passSql == passw):
                   #label.config(text="Logged In")
                   accP = accountPage(self)
                   accP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
               else:
                   label.config(text="Logged Out")
                   
           except (pymysql.Error) as e:
                   messagebox.showerror('Error', e)
                   return None
                
           finally:
              cnxn.close()
                
       def takeToRstPage():
           rstP = ChangePassPage(self)
           rstP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       def backOut():
           regLogP = regLogPage(self)
           regLogP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       
       rst = Button(self, text="Reset", command=takeToRstPage)
       rst.grid(row=0, column=5, columnspan=5)
       prn = Button(self, text="Login", command=printCom, width = 5, height  = 3)
       prn.grid(row=6, column=8, columnspan=2, rowspan=2)
       bk = Button(self, text='<--Back', command=backOut)
       bk.grid(row=0, column=0, columnspan=2)
       btnWidth = 2
       btnIpadx = 2
       btnIpady = 2
       def press(num, entry):
           entry.insert(tk.INSERT, num.lower())
           #content = adTxt.get(1.0, "end-1c")
           #text = content
           #print(content)
           entry.xview_moveto(1)
           
       def clrTxt():
           if (index == 1):
               usrTb.delete('0', END)
           if (index == 2):
               passTb.delete('0', END)
       
       def delete():
           if (index == 1):
               usrTb.delete('%s' % tk.INSERT)
           elif (index == 2):
               passTb.delete('%s' % tk.INSERT)
       
       
       def changeIndex(event, cngdIn):
           global index
           index = cngdIn
           print(index)
       
       def returnUsrTb(b):
           if (b == 1):
               return usrTb
           elif (b == 2):
               return passTb
           
       one = Button(self,text = '1' , width = btnWidth, command = lambda : press('1',returnUsrTb(index)))
       one.grid(row = 2 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       two = Button(self,text = '2' , width = btnWidth, command = lambda : press('2',returnUsrTb(index)))
       two.grid(row = 2, column = 1, ipadx = btnIpadx , ipady = btnIpady )

       three = Button(self,text = '3' , width = btnWidth, command = lambda : press('3',returnUsrTb(index)))
       three.grid(row = 2 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       four = Button(self,text = '4' , width = btnWidth, command = lambda : press('4',returnUsrTb(index)))
       four.grid(row = 2 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       five = Button(self,text = '5' , width = btnWidth, command = lambda : press('5',returnUsrTb(index)))
       five.grid(row = 2, column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       six = Button(self,text = '6' , width = btnWidth, command = lambda : press('6',returnUsrTb(index)))
       six.grid(row = 2 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       seven = Button(self,text = '7' , width = btnWidth, command = lambda : press('7',returnUsrTb(index)))
       seven.grid(row = 2, column = 6, ipadx = btnIpadx, ipady = btnIpady )

       eight = Button(self,text = '8' , width = btnWidth, command = lambda : press('8',returnUsrTb(index)))
       eight.grid(row = 2 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       nine = Button(self,text = '9' , width = btnWidth, command = lambda : press('9',returnUsrTb(index)))
       nine.grid(row = 2 , column = 8, ipadx = btnIpadx, ipady = btnIpady )

       zero = Button(self,text = '0' , width = btnWidth, command = lambda : press('0',returnUsrTb(index)))
       zero.grid(row = 2 , column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       #Row 2
       
       q = Button(self,text = 'Q' , width = btnWidth, command = lambda : press('Q',returnUsrTb(index)))
       q.grid(row = 3 , column = 0, ipadx = btnIpadx, ipady = btnIpady)
       
       w = Button(self,text = 'W' , width = btnWidth, command = lambda : press('W',returnUsrTb(index)))
       w.grid(row = 3 , column = 1, ipadx = btnIpadx , ipady = btnIpady )

       E = Button(self,text = 'E' , width = btnWidth, command = lambda : press('E',returnUsrTb(index)))
       E.grid(row = 3 , column = 2, ipadx = btnIpadx , ipady = btnIpady )

       R = Button(self,text = 'R' , width = btnWidth, command = lambda : press('R',returnUsrTb(index)))
       R.grid(row = 3 , column = 3, ipadx = btnIpadx , ipady = btnIpady )

       T = Button(self,text = 'T' , width = btnWidth, command = lambda : press('T',returnUsrTb(index)))
       T.grid(row = 3 , column = 4, ipadx = btnIpadx, ipady = btnIpady )
       
       Y = Button(self,text = 'Y' , width = btnWidth, command = lambda : press('Y',returnUsrTb(index)))
       Y.grid(row = 3 , column = 5, ipadx = btnIpadx, ipady = btnIpady )
       
       U = Button(self,text = 'U' , width = btnWidth, command = lambda : press('U',returnUsrTb(index)))
       U.grid(row = 3 , column = 6, ipadx = btnIpadx, ipady = btnIpady )

       I = Button(self,text = 'I' , width = btnWidth, command = lambda : press('I',returnUsrTb(index)))
       I.grid(row = 3 , column = 7, ipadx = btnIpadx, ipady = btnIpady )

       O = Button(self,text = 'O' , width = btnWidth, command = lambda : press('O',returnUsrTb(index)))
       O.grid(row = 3, column = 8, ipadx = btnIpadx, ipady = btnIpady )

       P = Button(self,text = 'P' , width = btnWidth, command = lambda : press('P',returnUsrTb(index)))
       P.grid(row = 3, column = 9, ipadx = btnIpadx, ipady = btnIpady )
       
       
       #Row 3



       A = Button(self,text = 'A' , width = btnWidth, command = lambda : press('A',returnUsrTb(index)))
       A.grid(row = 4 , column = 0, ipadx = btnIpadx , ipady = btnIpady)



       S = Button(self,text = 'S' , width = btnWidth, command = lambda : press('S',returnUsrTb(index)))
       S.grid(row = 4, column = 1, ipadx = btnIpadx , ipady = btnIpady)

       D = Button(self,text = 'D' , width = btnWidth, command = lambda : press('D',returnUsrTb(index)))
       D.grid(row = 4 , column = 2, ipadx = btnIpadx, ipady = btnIpady)

       F = Button(self,text = 'F' , width = btnWidth, command = lambda : press('F',returnUsrTb(index)))
       F.grid(row = 4 , column = 3, ipadx = btnIpadx , ipady = btnIpady)


       G = Button(self,text = 'G' , width = btnWidth, command = lambda : press('G',returnUsrTb(index)))
       G.grid(row = 4 , column = 4, ipadx = btnIpadx , ipady = btnIpady)


       H = Button(self,text = 'H' , width = btnWidth, command = lambda : press('H',returnUsrTb(index)))
       H.grid(row = 4 , column = 5, ipadx = btnIpadx , ipady = btnIpady)


       J = Button(self,text = 'J' , width = btnWidth, command = lambda : press('J',returnUsrTb(index)))
       J.grid(row = 4 , column = 6, ipadx = btnIpadx , ipady = btnIpady)


       K = Button(self,text = 'K' , width = btnWidth, command = lambda : press('K',returnUsrTb(index)))
       K.grid(row = 4 , column = 7, ipadx = btnIpadx , ipady = btnIpady)

       L = Button(self,text = 'L' , width = btnWidth, command = lambda : press('L',returnUsrTb(index)))
       L.grid(row = 4 , column = 8, ipadx = btnIpadx , ipady = btnIpady)


       semi_co = Button(self,text = ';' , width = btnWidth, command = lambda : press(';',returnUsrTb(index)))
       semi_co.grid(row = 4 , column = 9, ipadx = btnIpadx , ipady = btnIpady)


       

        # Row 4

       Z = Button(self,text = 'Z' , width = btnWidth, command = lambda : press('Z',returnUsrTb(index)))
       Z.grid(row = 5, column = 0, ipadx = btnIpadx , ipady = btnIpady)


       X = Button(self,text = 'X' , width = btnWidth, command = lambda : press('X',returnUsrTb(index)))
       X.grid(row = 5, column = 1, ipadx = btnIpadx , ipady = btnIpady)


       C = Button(self,text = 'C' , width = btnWidth, command = lambda : press('C',returnUsrTb(index)))
       C.grid(row = 5, column = 2, ipadx = btnIpadx , ipady = btnIpady)


       V = Button(self,text = 'V' , width = btnWidth, command = lambda : press('V',returnUsrTb(index)))
       V.grid(row = 5, column = 3, ipadx = btnIpadx , ipady = btnIpady)

       B = Button(self, text= 'B' , width = btnWidth , command = lambda : press('B',returnUsrTb(index)))
       B.grid(row = 5, column = 4 , ipadx = btnIpadx ,ipady = btnIpady)


       N = Button(self,text = 'N' , width = btnWidth, command = lambda : press('N',returnUsrTb(index)))
       N.grid(row = 5, column = 5, ipadx = btnIpadx , ipady = btnIpady)


       M = Button(self,text = 'M' , width = btnWidth, command = lambda : press('M',returnUsrTb(index)))
       M.grid(row = 5, column = 6, ipadx = btnIpadx , ipady = btnIpady)



      

       slas = Button(self,text = '/' , width = btnWidth, command = lambda : press('/',returnUsrTb(index)))
       slas.grid(row = 5, column = 7, ipadx = btnIpadx , ipady = btnIpady)


       q_mark = Button(self,text = '?' , width = btnWidth, command = lambda : press('?',returnUsrTb(index)))
       q_mark.grid(row = 5, column = 8, ipadx = btnIpadx , ipady = btnIpady)


       coma = Button(self,text = ',' , width = btnWidth, command = lambda : press(',',returnUsrTb(index)))
       coma.grid(row = 5, column = 9, ipadx = btnIpadx , ipady = btnIpady)

       #Row 5
       dot = Button(self,text = '.' , width = btnWidth, command = lambda : press('.',returnUsrTb(index)))
       dot.grid(row = 6, column = 6, ipadx = btnIpadx , ipady = btnIpady)

       at = Button (self, text = '@', width = btnWidth, command = lambda : press('@',returnUsrTb(index)))
       at.grid(row = 6, column = 5, ipadx = btnIpadx , ipady = btnIpady)
        
        #Row 6

       space = Button(self,text = 'Space' , width = 7, command = lambda : press(' ',returnUsrTb(index)))
       space.grid(row = 6, column = 3, columnspan = 2 , ipadx = 6 , ipady = 3)

       open_b = Button(self,text = '(' , width = btnWidth, command = lambda : press('(',returnUsrTb(index)))
       open_b.grid(row = 6 , column = 0 , ipadx = btnIpadx , ipady = btnIpady)

       close_b = Button(self,text = ')' , width = btnWidth, command = lambda : press(')',returnUsrTb(index)))
       close_b.grid(row = 6 , column = 1 , ipadx = btnIpadx , ipady = btnIpady)
               
       hasht = Button(self,text = '#' , width = btnWidth, command = lambda : press('#',returnUsrTb(index)))
       hasht.grid(row = 6, column = 2 , ipadx = btnIpadx , ipady = btnIpady)

       clear = Button(self,text = 'Clear' , width = btnWidth, command = clrTxt)
       clear.grid(row = 6, column = 7, ipadx = btnIpadx , ipady = btnIpady)

       d_colon = Button(self,text = '"' , width = btnWidth, command = lambda : press('"',returnUsrTb(index)))
       d_colon.grid(row = 6, column = 6, ipadx = btnIpadx , ipady = btnIpady)
       
       #Row 7
       
       
       dollar = Button(self,text = '$' , width = btnWidth, command = lambda : press('$',returnUsrTb(index)))
       dollar.grid(row = 7, column = 0 , ipadx = btnIpadx , ipady = btnIpady)
       
       plus = Button(self,text = '+' , width = btnWidth, command = lambda : press('+',returnUsrTb(index)))
       plus.grid(row = 7, column = 1 , ipadx = btnIpadx , ipady = btnIpady)
       
       minus = Button(self,text = '-' , width = btnWidth, command = lambda : press('-',returnUsrTb(index)))
       minus.grid(row = 7, column = 2 , ipadx = btnIpadx , ipady = btnIpady)
       
       excl = Button(self,text = '!' , width = btnWidth, command = lambda : press('!',returnUsrTb(index)))
       excl.grid(row = 7, column = 3 , ipadx = btnIpadx , ipady = btnIpady)
       
       underscore = Button(self,text = '_' , width = btnWidth, command = lambda : press('_',returnUsrTb(index)))
       underscore.grid(row = 7, column = 4 , ipadx = btnIpadx , ipady = btnIpady)
       
       left = Button(self,text = '<' , width = btnWidth, command = lambda : press('<',returnUsrTb(index)))
       left.grid(row = 7, column = 5 , ipadx = btnIpadx , ipady = btnIpady)
       
       right = Button(self,text = '>' , width = btnWidth, command = lambda : press('>',returnUsrTb(index)))
       right.grid(row = 7, column = 6 , ipadx = btnIpadx , ipady = btnIpady)
       
       delete = Button(self,text = 'Del' , width = btnWidth, command =  delete)
       delete.grid(row =7, column = 7 , ipadx = btnIpadx , ipady = btnIpady)
       usrTb.bind("<Button-1>", lambda event: changeIndex(event, 1))
       passTb.bind("<Button-1>", lambda event: changeIndex(event, 2))


class regLogPage(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to EZ Ads")
       label.pack(side="top", fill="both", expand=True)
       def takeToLogP():
           logP = LogPage(self)
           logP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       def takeToRegP():
           regP = RegPage(self)
           regP.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       loginBtn = Button(self, text = "Login", command = takeToLogP, width=25, height=10)
       loginBtn.pack(side="left")
       regBtn = Button(self, text = "Register", command = takeToRegP, width=25, height=10)
       regBtn.pack(side = "right")
       
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        pLR = regLogPage(self)
        #p1 = Page1(self)
        
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        #p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        #p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pLR.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #upLoadPage = tk.Button(buttonframe, text="Login", command=p1.lift)
        #delete = tk.Button(buttonframe, text="Upload", command=p2.lift)
        
        #----------------------------------------------------------------
        #b3 = tk.Button(buttonframe, text="Delete", command=p3.lift)

        #upLoadPage.pack(side="left")
        #delete.pack(side="left")
        
        #b3.pack(side="left")

        pLR.show()





if __name__ == "__main__":

    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("480x320")
    #root.attributes('-fullscreen', True)
    root.mainloop()
