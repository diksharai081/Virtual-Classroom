#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("text1")
b=form.getvalue("text2")
c=form.getvalue("text3")

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()

sel="select * from registration where password='%s'"%(a)
cursor.execute(sel)
data=cursor.fetchone()

if data[3]==a:
  print "<script>window.location.href='profile.py';alert('password change');</script>"
else:
  print "old pass not match"

  
if b==c:
  up="update registration set password='%s' where password='%s'"%(b,a)
  cursor.execute(up)
  db.commit()
  print "<script>window.location.href='profile.py';alert('password change');</script>"
else:
  print "new and confirm not match"
