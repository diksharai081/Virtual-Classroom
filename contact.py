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
		<style>
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
		input[type="text"]{
border-bottom:2px solid black;
border-top:0px solid red;
border-left:0px solid red;
border-right:0px solid red;
//background:transparent;
}
input[type="email"]{
border-bottom:2px solid black;
border-top:0px solid red;
border-left:0px solid red;
border-right:0px solid red;
background:transparent;
}
		</style>
		
</head>

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
	<div class="col-sm-12 p-0">
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
<div class="row ">
	<div class="col-sm-12 p-0">
	<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.901356265095!2d80.93581361456495!3d26.874874968188774!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399bfd90f852511b%3A0xea3004cdf494ecbb!2sDigiCoders+Technologies+Private+Limited!5e0!3m2!1sen!2sin!4v1565089137672!5m2!1sen!2sin" width="100%" height="500px" frameborder="0" style="border:0" allowfullscreen></iframe>
	</div>
	</div>
	<div class="row"style="background-image:url('image/wall1.jpg');opacity:0.9;;background-size:100% 100%;">
	<div class="col-sm-1"></div>
	<div class="col-sm-5" style="margin-top:50px;">
	<form class="i wow bounceInDown" onsubmit="return formvalidation()" action="contactcode.py" method="post">
<legend style="font-size:40px;font-weight:bold;" class="text-light">Contact Form</legend>
<div class="form-group">
<label class="text-light">Name</label>
<input type="text" font style="white" class="form-control" name="text1" id="t1"/>
</div>

<div class="form-group">
<label class="text-light">Email</label>
<input type="text" class="form-control" name="text2" id="t2"/>
</div>  
		
<div class="form-group">
<label class="text-light">Subject</label>
<input type="text" class="form-control" name="text3" id="t3"/>
</div>  

<div class="form-group">
<label class="text-light">Massege</label>
<input type="text" class="form-control" name="text4" id="t4"/>
</div>
<button type="submit" class="btn btn-primary btn-lg" >Submit</button>
</div>
</form>
&emsp;
	<div class="col-sm-5 ">
	<div class="card w-500" style="margin-top:100px; border:none;">
  <div class="card-body" >
    <p style="font-size:38px;font-weight:bold;">Contact Information</p><br/><br/>
	<p style="font-size:18px;font-weight:bold;">Website:&nbsp; WWW.virtulclasses.com</p><br/>
    	<p style="font-size:18px;font-weight:bold;">Contact No:&nbsp; 3452771868</p><br/>
    	<p style="font-size:18px;font-weight:bold;">Email Id:&nbsp; virtualclasses081@gmail.com</p><br/>
  </div>
</div>
	</div>
	<div class="col-sm-1"></div> 
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

<body>
</html>"""