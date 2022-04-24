#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("txt1")
b=form.getvalue("txt2")
c=form.getvalue("txt3")
d=form.getvalue("txt4")


import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()

import datetime

datetime=datetime.datetime.now()


ins="insert into feedback(name,email,subject,idea,datetime)            values('%s','%s','%s','%s','%s')"%(a,b,c,d,datetime)
cursor.execute(ins)
db.commit()
print "<script>window.location.href='home2.py';alert('data insert successfully');</script>"



