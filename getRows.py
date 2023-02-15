import pymysql

mydb = pymysql.connect("mysqltpj.ddns.net","root","root","adsdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT adid, cost, startd, endd, adstatus FROM b_class_ad where userid = 1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[2])