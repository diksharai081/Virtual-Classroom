#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

print"""
<html>
<head>
</head>
<body>
<div class="col-sm-4">
<form class="i wow bounceInDown" action="adminlogcode.py" method="post" onsubmit="return formvalidation()">
<legend style="font-size:40px;" class="text-black">logIn</legend>
<br/>
<div class="form-group">
<label class="text-black">Email</label>
<input type="text" class="form-control" name="email"/>
</div>  </br>
<div class="form-group">
<label class="text-black">Password</label>
<input type="password" class="form-control"  name="pass"/>
</div>  </br>
<button type="submit" class="btn btn-primary btn-lg" >LogIn</button>
</form>
</div>
</body>
</html>"""