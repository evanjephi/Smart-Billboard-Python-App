import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pyodbc
#import mysql.connector
import sys
from PIL import Image
import base64
import PIL.Image
sqlString = 'DRIVER=FreeTDS;SERVER=192.168.0.26;PORT=49170;DATABASE=adsDB;UID=sa;PWD=access;TDS_Version=8.0;'
imgRows = []
#cnxn = pyodbc.connect(sqlString)

#cursor = cnxn.cursor()

imgObj =  open('/home/pi/Pictures/eye.png','rb')
imgReader = imgObj.read()
#for row in imgReader:
   # element1 = row[0]
  #  element2 = row[1]
 #   element3 = row[2]
#    imgRows.append(element[1], element[2])


#cursor.execute("insert into images(id, imageFile) values (NEWID(), ?)",(pyodbc.Binary(bindata)))

#cnxn.commit()
#cnxn.close()

print ("What Dumass??")













