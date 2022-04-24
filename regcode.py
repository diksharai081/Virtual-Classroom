#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("text1")
b=form.getvalue("text2")
c=form.getvalue("text3")
d=form.getvalue("text4")
e=form.getvalue("text5")
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()
#print "okk"
import datetime

datetime=datetime.datetime.now()


ins="insert into registration(name,email,password,gander,city,datetime)            values('%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,datetime)
cursor.execute(ins)
db.commit()
print "<script>window.location.href='registration.py';alert('data insert successfully');</script>"




