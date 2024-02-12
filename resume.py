

def enter_html1(outputdata):
    ugdata=[]
    ugcgpa=[]
    pudata=[]
    pucgpa=[]
    scdata=[]
    sccgpa=[]
    pskills=[]
    wskills=[]
    courses=[]
    courselist=[]
    prodata=[]
    protools=[]
    prodes=[]
    prodata2=[]
    protools2=[]
    prodes2=[]
    databases=[]
    p1=[]
    w1=[]
    o1=[]
    d1=[]
    operatingsys=[]
    obj=[]
    obj=outputdata[6].split(':')
    ugdata=outputdata[7].split(',')
    ugcgpa=outputdata[8].split(':')
    pudata=outputdata[9].split(',')
    pucgpa=outputdata[10].split(':')
    scdata=outputdata[11].split(',')
    sccgpa=outputdata[12].split(':')
    pskills=outputdata[13].split(":")
    p1=pskills[1].split(",")
    wskills=outputdata[14].split(":")
    w1=wskills[1].split(",")
    databases=outputdata[15].split(":")
    d1=databases[1].split(",")
    operatingsys=outputdata[16].split(":")
    o1=operatingsys[1].split(",")
    courses=outputdata[17].split(':')
    courselist=courses[1].split(",")
    prodata=outputdata[18].split(':')
    protools=outputdata[19].split(':')
    prodes=outputdata[20].split(':')
    prodata2=outputdata[21].split(':')
    protools2=outputdata[22].split(':')
    prodes2=outputdata[23].split(':')
    html_text=f"""
<!DOCTYPE html>
<html>
<head>
	<title>{outputdata[0]}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<style type="text/css">
	:root{{
	--bgcolor:#beb8ac;
	--blue:#2fb7fe;
	--black:#3D3F42;
	--white:white;
	--gray:white;
	--lightgray:black;
}}
*{{
	margin: 0px;
	padding: 0px;
	box-sizing: border-box;
	font-family: monospace;
}}
body{{
	background: var(--bgcolor);
}}
.clearfix{{
	clear: both;
}}
.resume-box{{
	width: 800px;
	height: 1000px;
	margin: 100px auto;
	background: var(--white);
	box-shadow: 5px 21px 20px 20px #3d3f4238;
}}
.left-section{{
	background: var(--black);
	width: 250px;
	height: 1000px;
	float: left;
}}
.profile{{
	overflow: hidden;
	position: relative;
}}
.blue-box{{
      width: 257px;
    height: 250px;
    background: var(--blue);
    margin-left: -100px;
    transform: rotateZ(48deg);
    margin-top: -178px;
    
}}
.profile-img{{
	    position: absolute;
    z-index: 9;
    width: 120px;
    height: 120px;
    transform: translate(-50%, -50%);
    left: 50%;
    top: 50%;
    border-radius: 50%;
    border: 3px solid var(--gray);
}}
.name{{
    color: var(--gray);
    text-align: center;
    margin-top: -4px;
    font-size: 30px;
    letter-spacing: 2px;
    font-weight: 400;
    text-transform: uppercase;
}}
.name span{{
	color: var(--blue);
}}
.n-p{{
	width: 180px;
    margin: 0 auto;
    text-align: center;
    padding: 7px;
    border-bottom: 1px solid var(--gray);
    border-top: 1px solid var(--gray);
    color: var(--gray);
    margin-top: 11px;
    text-transform: uppercase;
}}
.info{{
	margin-top: 50px;
}}
.heading{{
	width: 180px;
    margin: 0 auto;
    padding: 2px;
    border-bottom: 1px solid var(--gray);
    border-top: 1px solid var(--gray);
    color: var(--gray);
    margin-top: 11px;
    text-transform: uppercase;
    font-size: 18px;
}}
.p1{{
	color: var(--gray);
	width: 184px;
	margin: 0 auto;
	margin-top: 25px;
	font-size: 15px;
    line-height: 14px;
}}
.p1 span{{
	font-size: 12px;
}}
.span1 img{{
	background: white;
    width: 30px;
    padding: 6px;
    border-radius: 16px;
    float: left;
    margin-right: 10px;
}}
.right-section{{
	padding: 40px 30px;
    background: var(--white);
    width: 68%;
    float: left;
    height: 1000px;
}}
.right-heading img{{
	background: #3d3f42;
    width: 36px;
    padding: 7px;
    border-radius: 17px;
    float: left;
    display: inline-block;
    margin-top: -6px;
}}
.p2{{
    margin: 0 auto;
    padding: 2px;
    border-bottom: 1px solid var(--lightgray);
    border-top: 1px solid var(--lightgray);
    color: var(--black);
    text-transform: uppercase;
    font-size: 18px;
    font-weight: bolder;
    margin-left: 50px;
    line-height: 18px;
}}
.p3{{
	margin-top: 20px;
	color: var(--lightgray);
	text-align: justify;
	word-spacing: -4px;
}}
.p3::first-letter{{
	text-transform: uppercase;
}}

.left{{
	width: 25%;
	float: left;
}}
.right{{
	width: 75%;
	float: left;
}}
.lr-box{{
	margin-top: 20px;
	margin-bottom: 20px;
}}
.p4{{
	font-size: 14px;
	font-weight: 600;
}}
.p5{{
	font-size: 12px;
	color: var(--lightgray);
}}
.p5::first-letter{{
	text-transform: uppercase;
}}
.s-box{{
	width: 50%;
    float: left;
    padding: 20px 20px 20px 0px;
}}
#progress {{
    background: #333;
    border-radius: 13px;
    height: 8px;
    width: 100%;
}}

#progress:after {{
    content: '';
    display: block;
    background: var(--blue);
    width: 50%;
    height: 100%;
    border-radius: 9px;
}}
#progress1 {{
    background: #333;
    border-radius: 13px;
    height: 8px;
    width: 100%;
}}

#progress1:after {{
    content: '';
    display: block;
    background: var(--blue);
    width: 40%;
    height: 100%;
    border-radius: 9px;
}}
#progress2 {{
    background: #333;
    border-radius: 13px;
    height: 8px;
    width: 100%;
}}

#progress2:after {{
    content: '';
    display: block;
    background: var(--blue);
    width: 80%;
    height: 100%;
    border-radius: 9px;
}}

#progress3 {{
    background: #333;
    border-radius: 13px;
    height: 8px;
    width: 100%;
}}

#progress3:after {{
    content: '';
    display: block;
    background: var(--blue);
    width: 90%;
    height: 100%;
    border-radius: 9px;
}}
.p6{{
	margin-top: 10px;
	margin-bottom: 10px;
	text-transform: uppercase;
}}
.h-img{{
	margin-top: 25px;
    width: 45px;
    margin-right: 45px;
}}
.reinfo{{
            color: white;
            margin-left: 35px;
            font-size: xx-large;
            text-align: center;
        }}
        .reinfo1{{
            color: white;
            margin-left: 255px;
            margin-top: 10px;
            font-size: large;
        }}
		@media print {{
	    .no-print, .no-print * {{ display: none !important; }}
		}}
		.resume1{{
background-color:#581B98;
height: 200px;
width:100%;
}}
.button{{
            margin-left: 45%;
            margin-top: 10px;
            text-align: center;
            width:200px;
            font-size: xx-large;
            background-color: white;
        }}
		.navbar {{
            overflow: hidden;
            background-color: #581B98;
            font-family: Arial;
          }}
          .navbar a {{
            float: left;
            font-size: 40px;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
          
          }}
          .li {{
            float: left;
            font-size: 16px;
            color: rgb(13, 13, 13);
            padding: 14px 16px;
            text-decoration: none;
            font-size: 30px;
          }}
          .dropdown {{
            float: left;
            overflow: hidden;
          }}
          .dropdown .dropbtn {{
            font-size: 40px;
            border: none;
            outline: none;
            color: white;
            padding: 14px 16px;
            background-color: inherit;
            font-family: inherit; /* Important for vertical align on mobile phones */
            margin: 0; /* Important for vertical align on mobile phones */
          }}
          .navbar a:hover, .dropdown:hover .dropbtn {{
            background-color: #8e4fd2;
          }}
          .dropdown-content {{
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
          }}
          .dropdown-content a {{
            float: none;
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display:block;
            text-align: left;
          }}
          .dropdown-content a:hover {{
            background-color: #ddd;
          }}
          .dropdown:hover .dropdown-content {{
            display: block;
          }}
</style>
<body>
	<div class="navbar no-print">
         <a href="/resume" style="font-size: 40px;"><i class="fa fa-arrow-left" aria-hidden="true" style="color:white"></i></a>
         <div class="dropdown">
          <button class="dropbtn">Instructions<i class="fa fa-caret-down"></i>
          </button>
          <div class="dropdown-content">
            <ol class="li"><li>To "Edit" the resume ,you can just point the mouse pointer and just edit the text</li>
                <li>To "Delete" you can just select the lines to be deleted and press "Delete key"</li>
               </ol>
          </div>
    </div>
	  <div class="dropdown">
		<button class="dropbtn" onclick="window.print()">Print as PDF
		</button>
		</div>
</div>
<div class="resume-box" contenteditable="true">
	
	<div class="left-section">
		<div class="profile">
			<div class="blue-box"></div>
			</div>
		<h2 class="name">{outputdata[0]}<br></h2>
		<p class="n-p">Student</p>


		<div class="info">
			<p class="heading">Info</p>
			<p class="p1"><span class="span1"><img src="././static/images/location.png"></span>Address<span> <br>{outputdata[5]}</span></p>
			<p class="p1"><span class="span1"><img src="././static/images/call.png"></span>Phone<span> <br>{outputdata[1]}</span></p>
			<p class="p1"><span class="span1"><img src="././static/images/mail.png"></span>Email<span> <br>{outputdata[2]}</span></p>
		</div>

		<div class="info">
			<p class="heading">Social</p>
			
			
			<p class="p1"><span class="span1"><img src="././static/images/linkedin.png"></span>Linkdin<span> <br>{outputdata[3]}</span></p>
			<p class="p1"><span class="span1"><img src="././static/images/facebook.png"></span>Github<span> <br>{outputdata[4]}</span></p>
		</div>
<div class="info">
			<p class="heading">Certifications</p>
			
			
			<p class="p1">{courselist[0]}</p>
			<p class="p1">{courselist[1]}</p>
		</div>
	</div>

	<div class="right-section">
		<div class="right-heading">
			<img src="././static/images/user.png">
			<p class="p2">Objective</p>
		</div>
		<p class="p3">{obj[1]}</p>

		
		

<div class="clearfix"></div>
		<br><br>
		<div class="right-heading">
			<img src="././static/images/pencil.png">
			<p class="p2">Project Details</p>
		</div>
		<div class="clearfix"></div>
		<div class="lr-box">
		<div class="left">
			<p class="p4">Title</p>
			<p class="p5">Tools:</p>
			<p class="p5">Description:</p>
		</div>

		<div class="right">
			<p class="p4"style="text-transform: capitalize;">{prodata[1]}</p>
			<p class="p5"style="text-transform: uppercase;">{protools[1]}</p>
			<p class="p5">{prodes[1]}</p>
		</div>
		<div class="clearfix"></div>
		</div>
        <br/>
		<div class="clearfix"></div>
		<div class="lr-box">
		<div class="left">
			<p class="p4">Title</p>
			<p class="p5">Tools:</p>
			<p class="p5">Description:</p>
		</div>

		<div class="right">
			<p class="p4"style="text-transform: capitalize;">{prodata2[1]}</p>
			<p class="p5"style="text-transform: uppercase;">{protools2[1]}</p>
			<p class="p5">{prodes2[1]}</p>
		</div>
		<div class="clearfix"></div>
		</div>

		<br>
		<div class="right-heading">
			<img src="././static/images/edu.png">
			<p class="p2">Education</p>
		</div>
		<div class="clearfix"></div>
		<div class="lr-box">
		<div class="left">
			<p class="p4">{ugdata[4]}</p>
			<p class="p5" style="text-transform: capitalize;">{ugdata[3]}</p>
		</div>

		<div class="right">
			<p class="p4" style="text-transform: capitalize;">{ugdata[0]} - {ugdata[1]}</p>
			<p class="p5" style="text-transform: capitalize;">{ugdata[2]}</p>
			<p class="p5" style="text-transform: capitalize;">{ugcgpa[1]}</p>
		</div>
		<div class="clearfix"></div>
		</div>

		<div class="lr-box">
		<div class="left">
			<p class="p4">{pudata[3]}</p>
			<p class="p5">{pudata[2]}</p>
		</div>

		<div class="right">
			<p class="p4" style="text-transform: capitalize;">{pudata[0]}</p>
			<p class="p5" style="text-transform: capitalize;">{pudata[1]}</p>
			<p class="p5" style="text-transform: capitalize;" >{pucgpa[1]}</p>
		</div>
		<div class="clearfix"></div>
		</div>

	<div class="lr-box">
		<div class="left">
			<p class="p4">{scdata[3]}</p>
			<p class="p5">{scdata[2]}</p>
		</div>

		<div class="right">
			<p class="p4" style="text-transform: capitalize;">{scdata[0]}</p>
			<p class="p5" style="text-transform: capitalize;">{scdata[1]}</p>
			<p class="p5" style="text-transform: capitalize;">{sccgpa[1]}</p>
		</div>
		<div class="clearfix"></div>
		</div>

		<br>
		<div class="right-heading">
			<img src="././static/images/edu.png">
			<p class="p2">Skills</p>
		</div>
		<div class="clearfix"></div>
		<div class="s-box">
			<p class="p4">Programming Languages</p>
			<p class="p6">{p1[0]}</p>
			<p class="p6">{p1[2]}</p>
			<p class="p6">{p1[1]}</p>
		</div>
		<div class="s-box">
		<p class="p4">Web Technologies</p>
			<p class="p6">{w1[0]}</p>
			<p class="p6">{w1[1]}</p>
		</div>
		<div class="clearfix"></div>
		<div class="s-box">
		<p class="p4">Database Management</p>
			<p class="p6">{d1[0]}</p>
			<p class="p6">{d1[1]}</p>
		</div>
		<div class="s-box">
		<p class="p4">Operating System</p>
			<p class="p6">{o1[0]}</p>
			<p class="p6">{o1[1]}</p>
		</div>
		<div class="clearfix"></div>
		<br><br>

		
	</div>
		<div class="clearfix"></div>
</div>
</body>
</html>"""
    with open('./templates/temp.html','w') as f:
        f.write(html_text)



def enter_html2(outputdata):
    ugdata=[]
    ugcgpa=[]
    pudata=[]
    pucgpa=[]
    scdata=[]
    sccgpa=[]
    pskills=[]
    wskills=[]
    courses=[]
    courselist=[]
    prodata=[]
    protools=[]
    prodes=[]
    databases=[]
    p1=[]
    w1=[]
    o1=[]
    d1=[]
    operatingsys=[]
    obj=[]
    obj=outputdata[6].split(':')
    ugdata=outputdata[7].split(',')
    ugcgpa=outputdata[8].split(':')
    pudata=outputdata[9].split(',')
    pucgpa=outputdata[10].split(':')
    scdata=outputdata[11].split(',')
    sccgpa=outputdata[12].split(':')
    pskills=outputdata[13].split(":")
    p1=pskills[1].split(",")
    wskills=outputdata[14].split(":")
    w1=wskills[1].split(",")
    databases=outputdata[15].split(":")
    d1=databases[1].split(",")
    operatingsys=outputdata[16].split(":")
    o1=operatingsys[1].split(",")
    courses=outputdata[17].split(':')
    courselist=courses[1].split(",")
    prodata=outputdata[18].split(':')
    protools=outputdata[19].split(':')
    prodes=outputdata[20].split(':')
    html_text=f"""
<!DOCTYPE html>
<html>
<head>
	<title>{outputdata[0]}</title>

	
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<style type="text/css">body{{
	margin: 0px;
	padding: 0px;
	background-image: radial-gradient(#c7c7c7 25%, #c7c7c7 74%);
	height: 100vh;
	font-family: system-ui;

}}
.clearfix{{
	clear: both;
}}
.main{{
	height: 1150px;
	width: 800px;
	background-color: white;
	box-shadow: 5px 7px 15px 5px #b9b6b6;
	margin: 20px auto;

}}

.top-section{{
	background-color:#151b29;
	text-align: center;
	padding: 20px;
}}
.profile{{
	width: 150px;
	border-radius: 50%;
}}
.p1{{
	color: white;
	font-size: 40px;
	font-weight: bold;
	margin: 0px;
	margin-top: 10px;
}}
.p1 span{{
	font-weight: 100;
	color: #121111;
}}
.p2{{
	font-size: 25px;
	color: #121111;
	margin: 0px;
	margin-top: 10px;
}}
.col-div-4{{
	width: 35%;
	float: left;

}}
.col-div-8{{
	width: 62%;
	float: left;
}}
.line{{
	border-left: 1px solid #121111;
  height: 950px;
  width: 2%;
  margin-top: 30px;
  float:left;
}}
.content-box{{
	padding: 20px;
}}
.head{{
	font-size: 25px;
	text-transform: uppercase;
	font-weight: 600;
}}
.p3{{
	color: #121111;
	margin-bottom: -5px;
	font-size: 17px;
}}
.p3::first-letter{{
	text-transform: capitalize;
}}
.fa{{
	color: #151b29;
}}
.skills{{
	margin-left: -20px;
	margin-bottom: 0px;
	text-transform: uppercase;
}}
.skills li{{
	padding: 5px;
}}
.skills li span{{
	color: #121111;
	font-size: 15px;
}}
.p-4{{
	
	color: #121111;
	font-size: 17px;
}}
.p-4::first-letter{{
	text-transform: capitalize;
}}
.p-1{{
	
	color: #121111;
	font-size: 20px;
	text-transform: capitalize;
}}
 .reinfo{{
            color: white;
            margin-left: 35px;
            font-size: xx-large;
            text-align: center;
        }}
        .reinfo1{{
            color: white;
            margin-left: 255px;
            font-size: large;
       }}
	    @media print {{
	    .no-print, .no-print * {{ display: none !important; }}
		}}
		.button{{
            margin-left: 45%;
            margin-top: 10px;
            text-align: center;
            width:200px;
            font-size: xx-large;
            background-color: white;
        }}.resume1{{
background-color:#581B98;
height: 200px;
width:100%;
}}
.navbar {{
            overflow: hidden;
            background-color: #581B98;
            font-family: Arial;
          }}
          .navbar a {{
            float: left;
            font-size: 40px;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
          
          }}
          .li {{
            float: left;
            font-size: 16px;
            color: rgb(13, 13, 13);
            padding: 14px 16px;
            text-decoration: none;
            font-size: 30px;
          }}
          .dropdown {{
            float: left;
            overflow: hidden;
          }}
          .dropdown .dropbtn {{
            font-size: 40px;
            border: none;
            outline: none;
            color: white;
            padding: 14px 16px;
            background-color: inherit;
            font-family: inherit; /* Important for vertical align on mobile phones */
            margin: 0; /* Important for vertical align on mobile phones */
          }}
          .navbar a:hover, .dropdown:hover .dropbtn {{
            background-color: #8e4fd2;
          }}
          .dropdown-content {{
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
          }}
          .dropdown-content a {{
            float: none;
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display:block;
            text-align: left;
          }}
          .dropdown-content a:hover {{
            background-color: #ddd;
          }}
          .dropdown:hover .dropdown-content {{
            display: block;
          }}
        
		</style>
<body>
 <div class="navbar no-print">
        <a href="/resume" style="font-size: 40px;"><i class="fa fa-arrow-left" aria-hidden="true" style="color:white"></i></a>
         <div class="dropdown">
          <button class="dropbtn">Instructions<i class="fa fa-caret-down" style="color:white"></i>
          </button>
          <div class="dropdown-content">
            <ol class="li"><li>To "Edit" the resume ,you can just point the mouse pointer and just edit the text</li>
                <li>To "Delete" you can just select the lines to be deleted and press "Delete key"</li>
               </ol>
          </div>
    </div>
	  <div class="dropdown">
		<button class="dropbtn" onclick="window.print()">Print as PDF
		</button>
		</div>
	</div>
	<div class="main" contenteditable="true">
		<div class="top-section">
			<p class="p1" style="text-transform: uppercase;">{outputdata[0]}</p>
			<p class="p2">Student</p>
		</div>
		<div class="clearfix"></div>

		<div class="col-div-4">
			<div class="content-box" style="padding-left: 40px;">

				
			<p class="head">Contact</p>
			<p class="p3"><i class="fa fa-phone" aria-hidden="true"></i> &nbsp;&nbsp;{outputdata[1]}</p>
			<p class="p3"><i class="fa fa-envelope" aria-hidden="true"></i> &nbsp;&nbsp;{outputdata[2]}</p>
			<p class="p3"><i class="fa fa-home" aria-hidden="true"></i> &nbsp;&nbsp;{outputdata[5]}</p>
			

			<br/>
			<p class="head">Skills</p>
			<ul class="skills">
				<li><span>{p1[0]}</span></li>
				<li><span>{p1[1]}</span></li>
				<li><span>{p1[2]}</span></li>
				<li><span>{w1[0]}</span></li>
				<li><span>{w1[1]}</span></li>
				<li><span>{w1[2]}</span></li>

			</ul>

			<br/>
			<p class="head">certifications</p>
				<p class="p3" style=" text-transform: capitalize;">{courselist[0]}</p>
				<p class="p3" style=" text-transform: capitalize;">{courselist[1]}</p>
			<br/>
			<p class="head">Languages</p>
			<p class="p3">Hindi</p>
			<p class="p3">English</p>
			</div>
		</div>
		<div class="line"></div>
		<div class="col-div-8">
			<div class="content-box">
			<p class="head">profile</p>
			<p class="p3">{obj[1]}<br/></p>
			<br/>
			<p class="head">PROJECTS</p>

			<p style=" text-transform: capitalize; font-size: 20px;">{prodata[1]}</p>
			<p class="p-4">{protools[1]}</p>
			<p class="p-4">{prodes[1]}</p>

			
			<br/>

			<p class="head">Education</p>
			<p class="p-1">{ugdata[0]} - {ugdata[1]} ({ugdata[4]})</p>
			<p class="p-4" style=" text-transform: capitalize;">{ugdata[2]}, {ugdata[3]}</p>
			<p class="p-4">{ugcgpa[1]}</p>
			<p class="p-1">{pudata[0]} ({pudata[3]})</p>
			<p class="p-4" style=" text-transform: capitalize;">{pudata[1]}, {pudata[2]}</p>
			<p class="p-4">{pucgpa[1]}</p>
			<p class="p-1">{scdata[0]} ({scdata[3]})</p>
			<p class="p-4" style=" text-transform: capitalize;">{scdata[1]}, {scdata[2]}</p>
			<p class="p-4">{sccgpa[1]}</p>


			</div>
		</div>

		<div class="clearfix"></div>

	</div>
		<br/>
</body>
</html>"""
    with open('./templates/temp1.html','w') as f:
        f.write(html_text)




def enter_html3(outputdata):
    ugdata=[]
    ugcgpa=[]
    pudata=[]
    pucgpa=[]
    scdata=[]
    sccgpa=[]
    pskills=[]
    wskills=[]
    courses=[]
    courselist=[]
    prodata=[]
    protools=[]
    prodes=[]
    databases=[]
    p1=[]
    w1=[]
    o1=[]
    d1=[]
    operatingsys=[]
    prodata2=[]
    protools2=[]
    prodes2=[]
    experience=[]
    exp=[]
    obj=[]
    obj=outputdata[6].split(':')
    ugdata=outputdata[7].split(',')
    ugcgpa=outputdata[8].split(':')
    pudata=outputdata[9].split(',')
    pucgpa=outputdata[10].split(':')
    scdata=outputdata[11].split(',')
    sccgpa=outputdata[12].split(':')
    pskills=outputdata[13].split(":")
    p1=pskills[1].split(",")
    wskills=outputdata[14].split(":")
    w1=wskills[1].split(",")
    databases=outputdata[15].split(":")
    d1=databases[1].split(",")
    operatingsys=outputdata[16].split(":")
    o1=operatingsys[1].split(",")
    courses=outputdata[17].split(':')
    courselist=courses[1].split(",")
    prodata=outputdata[18].split(':')
    protools=outputdata[19].split(':')
    prodes=outputdata[20].split(':')
    prodata2=outputdata[21].split(':')
    protools2=outputdata[22].split(':')
    prodes2=outputdata[23].split(':')
    experience=outputdata[24].split(":")
    exp=experience[1].split(",")
    html_text=f"""<!Doctype HTML><html>
	<head>
	<title>{outputdata[0]}</title>
	<link rel="stylesheet" type="text/css" href="static/style.css"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	</head>
	<body style="background: #E0E0E0;">
   <div class="navbar no-print">
        <a href="/resume" style="font-size: 40px;"><i class="fa fa-arrow-left" aria-hidden="true"></i></a>
         <div class="dropdown">
          <button class="dropbtn">Instructions<i class="fa fa-caret-down"></i>
          </button>
          <div class="dropdown-content">
            <ol class="li"><li>To "Edit" the resume ,you can just point the mouse pointer and just edit the text</li>
                <li>To "Delete" you can just select the lines to be deleted and press "Delete key"</li>
               </ol>
          </div>
    </div>
	  <div class="dropdown">
		<button class="dropbtn" onclick="window.print()">Print as PDF
		</button>
		</div>
</div>
	<div class="box-outer" contenteditable="true">
		<div class="resume-box">
			<div>
				<div class="col-sm-6">
					
					<h1 class="name">{outputdata[0]}<br/></h1>
					<p class="name_p">Student</p>
				</div>
				<div class="col-sm-6">
					<div style="float: left;">
						<p class="contat_p">
							<i class="fa fa-home fontfa"></i>
							&nbsp; {outputdata[5]} &nbsp;
							<i class="fa fa-envelope fontfa"></i>
							&nbsp; Email : {outputdata[2]} &nbsp;
							<i class="fa fa-phone fontfa"></i>
							&nbsp; Phone {outputdata[1]}
						</p>
					</div>
				</div>
				<div class="clearfix"></div>
				<br/>
				<hr/>
				<br/>
				<h1 class="head">Objective</h1>
				<p class="para-2">
					{obj[1]}
				</p>
			</div>
			<hr/>
			<br/>

			<div class="box-1">
				<div class="content">
					<h1 class="head">Education</h1>
					<br/>
					<ul>
						<li>
							<p class="para-1">({ugdata[4]})<br/>{ugdata[0]}<br/>{ugdata[1]}</p>
							<p class="para-2">{ugcgpa[1]}</p>
						</li>
						<li>
							<p class="para-1">({pudata[3]})<br/>{pudata[0]}</p>
							<p class="para-2">{pucgpa[1]}</p>
						</li>
						<li>
							<p class="para-1">({scdata[3]})<br/>{scdata[0]}</p>
							<p class="para-2">{sccgpa[1]}</p>
						</li>
				
					</ul>

					<h1 class="head">Skills</h1>
					<br/>
					<ul>
						<li>
							<p class="para-2">{p1[0]}</p>
						</li>
						<li>
							<p class="para-2">{p1[1]}</p>
							
						</li>
						<li>
							<p class="para-2">{w1[0]}</p>
							
						</li>
						<li>
							<p class="para-2">{w1[1]}</p>
							
						</li>
					</ul>
				</div>
			</div>
			<div class="box-2">
				<div class="content-2">
					<h1 class="head">Project Details</h1>
					<br/>
					<ul>
						<li>
							<p class="para-1">{prodata[1]}</p>
							<p class="para-2">
								{protools[1]}
							</p>
							<p class="para-2">
								{prodes[1]}
							</p>
						</li>
				</div>
			</div>
			<div class="box-2">
				<div class="content-2">
					<h1 class="head">Work Experience</h1>
					<br/>
					<ul>
						<li>
							<p class="para-1">{exp[0]}</p>
							<p class="para-2">
								{exp[1]}
							</p>
							<p class="para-2">
								{exp[2]}
							</p>
						</li>
				</div>
			</div>
			<div class="box-2">
				<div class="content-2">
					<h1 class="head">Certifications</h1>
					<br/>
					<ul>
						<li>
							<p class="para-1">{courselist[0]}</p>
							
						</li>
						<li>
						<p class="para-1">{courselist[1]}</p>
							</li>
					</ul>
				</div>
			</div>
		</div>
		<div class="clearfix"></div>
	</div>
	</body>
	</html>"""
    with open('./templates/temp3.html','w') as f1:
        f1.write(html_text)

"""outputdata=['priyanka.c', '1vi19cs074', '9483106792', 'priyankachandrashekar2001@gmail.com', 'https://linkedin.com/priyanka', 
'github.com/priyanka', '#332/3,hallashalli road, varthur, bangalore', 
'objective:i intend to be part of an organization where i can constantly learn and develop my technical and management skills and make best use of it for the growth of the organization',
 'btech,computer science and engineering, vemana institute of technology,bangalore,2019-2023', 'ug cgpa: 9.15', 
'12th, rjs pu college,bangalore,2019', '12th cgpa: 90.50', '10th, lady vailankanni high school, bangalore, 2017', '10th cgpa: 79.68',
 'programming: python,java,advanced java', 'webtech: html,css,js', 'database: mysql,sql,mongod',
  'operatingsys:linux,window', 'courses: AICTE student learning assessment, spoken tutorial', 
'title: farm management system', 'tools used: html',
 'description: the objective of the project is to provide farmers a platform to display and sell their farm products and for the customers to buy these products at lower price without the third party being invloved.', 'title2: Music player', ' tools used2: xml, java', 'tools used2:xml,java', 'description2: the objective of the project is to provide users with an application that allows them to listen to songs/audio in offline mode.', 
'experience: java developer, 6d, I had worked on a client project where the project was 89% better than the existing system. ']
enter_html1(outputdata)
enter_html2(outputdata)
enter_html3(outputdata)"""