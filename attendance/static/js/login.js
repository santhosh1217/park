var btn=document.getElementById('btn')
document.getElementById("type").value = "admin";

function leftClick() 
{

	btn.style.left='0';
	document.getElementById("type").value = "admin";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/06/Student.png)";
	
}

function rightClick() 
{
    
	btn.style.left='110px';
	document.getElementById("type").value= "staff";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/07/Aging.png)";
	
}
function chck()
{
	document.getElementById("log").action = '';
	var id = document.getElementById("us").value;
	if (document.getElementById("type").value != "admin")
	{
		alert("staff login");
		document.getElementById("log").action =id+ "/departments";
	}
	else
	{
		alert("admin login");
		document.getElementById("log").action =id+ "/admin";
	}
}
