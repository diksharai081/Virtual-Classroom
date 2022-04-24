#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("id")


import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","online_virtual_classroom")
cursor=db.cursor()

sel="select * from admin where id=%s"%(a)
cursor.execute(sel)
data=cursor.fetchone()

print"""
<html>
<head>
<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link href="../css/bootstrap.min.css" rel="stylesheet" />
		<script src="../js/jquery-3.3.1.slim.min.js"></script>
		<script src="../js/popper.min.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
         <style>
		      #a{
				  background:linear-gradient(white);
			  }
			  .carousel-item img
			  {
				  height:450px;
				  width:100%
			  }
			  #aa{
				  height:500px;
				  background-image:url(image/a6.jpg);
				  background-size:100% 100%;
			  }
			  #b{
	background:linear-gradient(#f5f6f7,#f5f6f7);
              }
	
	</style>
		</head>
<body style="background:#e7eaed">
<div class="container-fluid" >
<!-- header row-->

<!--title-->


<!--navbar-->
<div class="row">
<div class="col-sm-12 p-0">

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="dashboard.py">Dashboard</a>
 
  <div class="collapse navbar-collapse " id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active ">
        <a class="navbar-brand" href="allregistration.py">All Registration<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="navbar-brand" href="allfeedback.py">All Feedback</a>
      </li>
      <li class="nav-item">
        <a class="navbar-brand" href="allcontact.py">All CONTACT</a>
      </li> 
	  <li class="nav-item">
        <a class="navbar-brand" href="changepass.py">Change Password</a>
      </li>
	  <li class="nav-item">
        <a class="navbar-brand" href="logout.py">Log Out</a>
      </li>
      
    </ul>
  </div>
</nav>
</div>
<div class="col-sm-12">
<div class="col-sm-12 text-center" style="padding-top:10px;color:red;"><h1> change password</h1></div>
	<form action="adminchangepasscode.py" method="post">
	    <input type="hidden" name="id" value="1"/>
		<input type="text" placeholder="current Password" name='opass' class="form-control"/><br/>
		<input type="text"  placeholder="New Password" name='npass'class="form-control"/><br/>
		<input type="text"  placeholder="Confirm Password"name='cpass'class="form-control"/><br/>
		<button class="btn btn-lg btn-info"> Change Password</button>
	</form>

</div>
</div><br/>
</div>
</body>
</html>"""