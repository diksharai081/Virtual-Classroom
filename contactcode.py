#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import cgi,cgitb
form=cgi.FieldStorage()
a=form.getvalue("text1")
b=form.getvalue("text2")
c=form.getvalue("text3")
d=form.getvalue("text4")
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()
#print "Check Connection okk  "

ins="insert into contact(name,email,subject,massege)values('%s','%s','%s','%s')"%(a,b,c,d)
cursor.execute(ins)
db.commit()
print "<script>window.location.href='contact.py';alert('contact data saved successfully');</script>"