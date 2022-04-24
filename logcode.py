#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("email")
b=form.getvalue("pass")

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()

sel="select * from registration where email='%s'"%(a)
cursor.execute(sel)
data=cursor.fetchone()

if data[2]==a:
  print "<script>window.location.href='profile.py?id=%s';alert('login success');</script>"%(a)
else:
  print "login failed"