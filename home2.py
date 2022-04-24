#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
print """
<html>
<head>
<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link href="css/bootstrap.min.css" rel="stylesheet" />
		<script src="js/jquery-3.3.1.slim.min.js"></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
		<style>
		.carousel-item img
		{
		height:500px;
		width:100%;
		}
		.btn
		{
		height:50px;
		
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
		
</head>
<body>
<div class="container-fluid">
		<div class="row bg-dark text-white" style="position:sticky;top:0%;z-index:999;">
		<div  class="col-sm-4">
		<h5><i class="fa fa-circle" style="font-size:10px; color:red;"> </i>&nbsp;Live</h5>
		</div>
		<div  class="col-sm-5" >
		<h5><i class="fa fa-phone" style="color:#03fc1c;"></i>&nbsp;Phone no:7607101498</h5>
		</div>
		<div  class="col-sm-3">
		<h5>Email:diksharai081@gmail.com </h5>
		</div></div>
<div class="row" style="position:sticky;top:4%;z-index:999;">
	<div class="col-sm-12 bg-info text-white text-center">
	<h1>ONLINE VIRTUAL CLASSROOM</h1>
	</div>
	</div>
	<div class="row" style="position:sticky;top:12%;z-index:999;">
	<div class="col-sm-12 p-0">
	<nav class="navbar navbar-expand-lg bg-light">
  <h5><a class="navbar-brand" href="home2.py">Home</a></h5>
  <button class="navbar-toggler bg-info " type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"></button>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
     
      <li class="nav-item ">
       <h5> <a class="navbar-brand" href="about.py">About</a></h5>
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
    </ul>
    </div>
</nav>
	</div>
	</div>
  <div class="row">
  <div class="col-sm-12 p-0">

  <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="image/w23.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="image/w21.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="image/w27.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div></div></div>
<div class="row">
	<div class="col-sm-12 bg-dark text-white text-center">
	<h1 style="margin:30px 0px 20px 0px;">Popular Classes News</h1>
	</div>
	</div>
	<div class="row">
	<div class="col-sm-12 text-black bg-light">
	<h3 class="text-center text-primary" style="font-weight:bold;">HTML</h3>
	<marquee><h4 style="color:red;">Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript</h4></marquee>
	<h3  class="text-center text-primary" style="font-weight:bold;">CSS</h3>
	<marquee><h4 style="color:red;">
	Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript
	</h4></marquee>
				</div></div>
				<div class="row">
				<div class="col-sm-2"></div>
				<div class="col-sm-2">
	<a href="classes.py"><button type="button" class="btn btn-primary btn-lg"> &nbsp;&nbsp;&nbsp;&nbsp; Pdf  &nbsp;&nbsp;&nbsp;&nbsp;</button></a> </div>
<div class="col-sm-2">	
<a href="classes.py"><button type="button" class="btn btn-primary btn-lg">   &nbsp;&nbsp;&nbsp;&nbsp;notes &nbsp;&nbsp;&nbsp;&nbsp; </button></a></div>
<div class="col-sm-2">
	<a href="classes.py"><button type="button" class="btn btn-primary btn-lg"> &nbsp;&nbsp;&nbsp;&nbsp;books  &nbsp;&nbsp;&nbsp;&nbsp;</button></a></div>
	<div class="col-sm-2">
<a href="classes.py"><button type="button" class="btn btn-primary btn-lg"> &nbsp;&nbsp;&nbsp;&nbsp;video &nbsp;&nbsp;&nbsp;&nbsp;</button></a>
	</div>
	<div class="col-sm-2"></div>
	</div><br/>
	<div class="row">
	<div class="col-sm-12 bg-info text-dark text-center" style="background-image:url('image/wall5.jpg');">
	<h1 style="margin:20px 0px 40px 0px;">Send Your Idea</h1>
	
	</div>
	<div class="col-sm-12 p-0">
		<form action="homecode.py" method="post" style="background-image:url('image/wall5.jpg');margin:0px 0px 0px 0px;padding:40px;">
  <div class="form-row">
    <div class="form-group col-md-4 ">
     Name <input type="text" name="txt1"  class="form-control" id="name" placeholder="your name.."/>
    </div>
    <div class="form-group col-md-4">
    Mobile  <input type="number" name="txt2" class="form-control" id="number" placeholder="your number"/>
    </div>
	<div class="form-group col-md-4">
    Subject  <input type="text" class="form-control" name="txt3" id="subject" placeholder="subject"/>
    </div>
  </div>
  <div class="form-row">
    <div class="form-group col-md-6" style="margin:0px 0px 50px 0px;">
    Send Idea 
   
	<textarea class="form-control" id="idea" placeholder="type your idea" name="txt4"></textarea>
	 </div>
 &emsp; &emsp; &emsp;
  <button  class="btn btn-primary" style="height:50px;margin-top:25px;">Submit</button></div>
</form>
	</div>
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