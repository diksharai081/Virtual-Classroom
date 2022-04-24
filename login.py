#!F:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
print """<html>
<head>

<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link href="css/bootstrap.min.css" rel="stylesheet" />
		<script src="js/jquery-3.3.1.slim.min.js"></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
		</head>
		<style>
		
		.a{
height:700px;
width:100%;
background:url(image\5.jpg);
background-size:100% 100%;
position:fixed;
}

.i{
width:400px;
margin-top:30px;
font-size:20px;
}
input[type="text"]{
border-bottom:2px solid black;
border-top:0px solid red;
border-left:0px solid red;
border-right:0px solid red;
background:transparent;
}
input[type="email"]{
border-bottom:2px solid black;
border-top:0px solid red;
border-left:0px solid red;
border-right:0px solid red;
background:transparent;
}
.navbar-brand
		{
			text-transform:capitalize;
			padding:15px 40px;
			margin:0px 20px;
			
		}
		.navbar-brand:hover{
			color:white;
			background-color:blue;
			border-radius:40px 40px 40px 40px;
		}
		</style>
<body>

<div class="container-fluid">
<div class="row bg-dark text-white" style="position:sticky;top:0%;z-index:999">

		<div  class="col-sm-4">
		
		<h5><i class="fa fa-circle" style="font-size:10px; color:red;" ></i>&nbsp;Live</h5>
		</div>
		<div  class="col-sm-5" style="text-align:center;">
		<h5><i class="fa fa-phone" style="color:#03fc1c;"></i>&nbsp;Phone no:3244463776</h5>
		</div>
		<div  class="col-sm-3">
		<h5>Email:diksharai081@gmail.com </h5>
		</div></div>
<div class="row" style="position:sticky;top:4%;z-index:999;">
	<div class="col-sm-12 bg-info text-white text-center">
	<h1>ONLINE VIRTUAL CLASSROOM</h1>
	</div>
	</div>
	<div class="row p-0" style="position:sticky;top:12%;z-index:999;">
	<div class="col-sm-12 p-0 ">
	<nav class="navbar navbar-expand-lg bg-light">
  <h5><a class="navbar-brand" href="home2.py">Home</a></h5>
  <button class="navbar-toggler bg-info " type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
     
      <li class="nav-item ">
       <h5> <a class="navbar-brand about" href="about.py">About</a></h5>
      </li>
       <li class="nav-item">
       <h5> <a class="navbar-brand" href="gallery.py">gallery</a></h5>
      </li>
	   <li class="nav-item">
       <h5> <a class="navbar-brand" href="classes.py">classes</a></h5>
      </li>
	   <li class="nav-item">
      <h5>  <a class="navbar-brand" href="registration.py">registration</a></h5>
      </li>
      <li class="nav-item">
        <h5><a class="navbar-brand" href="login.py">login</a></h5>
      </li> <li class="nav-item">
       <h5> <a class="navbar-brand" href="contact.py">contact</a></h5>
      </li>
    </ul></div>
</nav></div>
	</div>
	<div class="row" style="background-image:url('image/wall5.jpg');background-size:100% 100%;">
<div class="col-sm-4"></div>
<div class="col-sm-4">
<form class="i wow bounceInDown" action="logcode.py" method="post" onsubmit="return formvalidation()">
<legend style="font-size:40px;font-weight:bold;" class="text-black">SignIn</legend>
<br/>
<div class="form-group">
<label class="text-black">Email</label>
<input type="text" class="form-control" id="t2" name="email"/>
</div>  
<div class="form-group">
<label class="text-black">Password</label>
<input style="border:none;border-bottom:2px solid black;background:transparent;" type="password"  class="form-control" id="t3" name="pass"/>
</div>  
<center><button type="submit" class="btn btn-primary btn-lg" >LogIn</button></center>
</form>
</div>
<div class="col-sm-4"></div>
</div>

<div class="row bg-dark text-white">
<div class="col-sm-5 px-5"></br>

<h2>About</h2>
<i class="fa fa-map-marker fa-1x" style="height:20px; width:20px;">&emsp;</i>
Near - Tewa, Manjhanpur, Kaushambi<br/>
<li class="fa fa-phone fa-1x">&emsp; 7607101498 </li></br>
<i class="fa fa-send fa-1x" > &emsp;</i> diksharai081@email.com <br/></br>
<h4>Follow Us</h4>
<a href="https://twitter.com/login" target="_blank"><li class="fa fa-twitter fa-1x">&emsp; &emsp; </li></a>
<a href="https://facebook.com/login" target="_blank"><li class="fa fa-facebook fa-1x">&emsp; &emsp; </li></a>
<a href="https://www.instagram.com/accounts/login/" target="_blank"><li class="fa fa-instagram fa-1x">&emsp; &emsp; </li></a>
<a href="https://www.youtube.com/login/" target="_blank"><i class="fa fa-youtube fa-1x" ></i></a>
</div>
<div class="col-sm-3"><br/>
<h3>Links</h3>
<ul><a href="home2.py"><li><font size="3">Home</li></a>
<a href="about.py"><li>About</li></a>
<a href="gallery.py"><li>Gallery</li></a>
<a href="classes.py"><li>Classes</li></a>
<a href="registration.py"><li>Registration</li></a>
<a href="login.py"><li>LogIn</li></a>
<a href="contact.py"><li>Contact</li></a></br></font>
</ul>
</div>
<div class="col-sm-4"><br/>

<h3>Support</h3><br/>
<h6>How to use the teacher Dashboard to mana...</br>
how to create recurring class schedules</br>
How to convert word or powerpoint files to...</br>
How to use the virtual classroom..</br>
how to schrdule an upcoming virtual class..
</h6>
</div>
</div>
<div class="row">
<div class="col-sm-6 bg-dark text-white text-center" style="font-weight:bold;">
Diksharai <i class="fa fa-copyright fa-1x" ></i> 2019All rights reserved
</div>
<div class="col-sm-6 bg-dark text-white text-center" style="font-weight:bold;">
 Powered By - Diksha Rai (MJPGP Kaushambi)
</div>
</div>
	</div>
</body>
</html>"""