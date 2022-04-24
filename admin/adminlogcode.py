#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("email")
b=form.getvalue("pass")

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()

sel="select * from admin where email='%s'"%(a)
cursor.execute(sel)
data=cursor.fetchone()


if data[1]==a:
  print "<script>window.location.href='dashboard.py?id=%s';alert('login success');</script>"%(data[0])
else:
  print "login failed"
  
  
  