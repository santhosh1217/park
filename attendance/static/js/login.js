var btn=document.getElementById('btn')
document.getElementById("type").value = "admin";

function leftClick() {
	
	btn.style.left='0';
	document.getElementById("type").value = "admin";
	document.getElementById("log").action = "admin";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/06/Student.png)";
	
}

function rightClick() {
	
	btn.style.left='110px';
	document.getElementById("type").value= "staff";
	document.getElementById("log").action = "departments";
	
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/07/Aging.png)";
	
}