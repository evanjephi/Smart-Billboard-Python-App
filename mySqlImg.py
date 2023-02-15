import pymysql

import base64

f = open('/home/pi/Pictures/maxresdefault.jpg', 'rb')
photo = f.read()
f.close()

conn = pymysql.connect("mysqltpj.ddns.net", "root", "root", "adsdb")
cursor = conn.cursor();
#with open('/home/pi/Pictures/newTestlel.jpg', 'rb') as image:
#    imager = image.read()
s = "x"
sqls = ("insert into usert (name, email, pass) values (%s, %s, %s)")

#cursor.execute("insert into testimg(id, img) values (?,?)",(2, imager))
#cursor.execute("INSERT INTO testimg (id, img) VALUES (%s, %s)", (10, imager)) 
cursor.execute("INSERT INTO usert (name, email, pass) VALUES (%s, %s, %s)", (s, s, s))
conn.commit();
conn.close()
