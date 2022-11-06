from os import link
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from attendance import models
from twilio.rest import Client
from django.contrib import messages
import random

def institute_login(request):
    if (request.method!='POST'):
        return render(request,"login.html")

def signup(request):
    return render(request,"institute signup.html")

######################################### sign up form validation #####################################################

def submit(request):
    obj =  models.college()
    obj.username = request.POST["username"]
    obj.password = request.POST['password']
    obj.name = request.POST["instituteName"]
    obj.logo = request.FILES.get("logo","game")
    if models.college.objects.filter(username=request.POST["username"]).exists():
             return render(request,"institute signup.html",{"msg":"username exist"})
    else:
        if request.POST['password'] == request.POST['confirmPassword']:

            if models.college.objects.filter(name=request.POST["instituteName"]).exists():
                return render(request,"institute signup.html",{"msg":"institute name already exists"})
            else:
                obj.save()
                return redirect("home")
        else:
            return render(request,"institute signup.html",{"msg":"password not match"})

        
    
################################################################# login ############################################################

def login(request,id):
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']
        if request.POST["type"] == "admin":

            print("admin")
            if models.college.objects.filter(username=user).exists():
                obj = models.college.objects.get(username=user)
          
                if obj.password == passw:
                    if models.Staff.objects.filter(staffCollege=obj.name).exists():
                        print(obj.name)
                        data=models.Staff.objects.filter(staffCollege=obj.name)
                        return render(request,"addstaff.html",{"mydata":data})
                    else:
                        print("hellooo")
                        return render(request,"addstaff.html")
                
                else:
                    messages.info(request,"2")
                    return redirect("home")

            else:
                messages.info(request,"1")
                return redirect("home")


        else:
            print("staff")
            if  models.Staff.objects.filter(staffUsername=user).exists():
                obj =  models.Staff.objects.get(staffUsername=user)

                if obj.staffPassword == passw:
              
                    
                    obj1 = models.college.objects.get(name = obj.staffCollege)
                    return render(request,"department.html",{"name":obj1.name,"logo":obj1.logo.url})

                else:
                    messages.info(request,"4")
                    return redirect("home")

            else:
                messages.info(request,"3")
                return redirect("home")


    else:
                print(id)
                obj = models.college.objects.get(username=id)
                data=models.Staff.objects.filter(staffCollege=obj.name)
                return render(request,"addstaff.html",{"mydata":data})


    



##############################################################    years #############################################################

def year(request,user,department):
    return render(request, "year.html",{"link":department})

############################################################## attendance ########################################################

def department(request,user,department,year):
    obj = models.Staff.objects.get(staffUsername=user)
    obj1 = models.college.objects.get(name=obj.staffCollege)
    student = models.Student.objects.filter(department=department,year=year,clg = obj1.name)
    years = {"1":"first year","2":"second year","3":"third year","4":"final year"}
    dep = {"cse":"computer science","it":"information technology","ece":"electronics and communication ","eee":"electrical and electronics","mech":"mechanical","civil":"civil"}
    message = {"department":dep.get(str(department)),"year": years.get(str(year)),"logo":obj1.logo.url,"college":obj1.name,"detial":student}
    return render(request,"attendance.html",message)

                                        # # # ' ' 'STAFF ' ' ' # # #

############################################################ ADD DATA ################################################################

def addstaffs(request,id):
    url=request.get_full_path()
    data=models.Staff.objects.all()
    obj=models.Staff()
    if request.method=='POST':

        if models.Staff.objects.filter(staffUsername=request.POST["s_username"]).exists():
            messages.info(request,"username exists")
            return redirect("admin",id)
        else:        
            obj.staffName = request.POST["s_name"]
            obj.staffDep = request.POST["s_dep"]
            obj.staffPosition = request.POST["s_position"]
            obj.staffUsername = request.POST["s_username"]
            obj.staffPassword= request.POST["s_password"]
            obj1 = models.college.objects.get(username=id)
            obj.staffCollege = obj1.name
            obj.save()
            return redirect("admin",id)

########################################################### UPDATE ################################################################### 

def staff_update(request,id,users):
    if request.method == "POST":
       
        obj=models.Staff.objects.get(id=id)
        obj.staffName = request.POST["s_name"]
        obj.staffDep = request.POST["s_dep"]
        obj.staffPosition = request.POST["s_position"]
        obj.staffUsername = request.POST["s_username"]
        obj.staffPassword= request.POST["s_password"]
        obj.save()
        return redirect("admin",users)
    
    else:
   
        obj=models.Staff.objects.get(id=id)
        return render(request,"updateStaff.html",{"data":obj})


########################################################## DELETE ###################################################################

def staff_delete(request,id,users):
    print("deleted")
    url=request.get_full_path()
    mydata=models.Staff.objects.get(id=id)
    mydata.delete()
    return redirect("admin",users)


                                             # # # " " " STUDENT " " " # # #


##############################################################  ADMIN  ###############################################

def admin(request,user,department,year):
    obj = models.Staff.objects.get(staffUsername=user)
    obj1 = models.college.objects.get(name=obj.staffCollege) 
    detial = models.Student.objects.filter(department=department,year=year,clg = obj1.name) 
    return render(request,"addstudent.html",{"logo":obj1.logo.url,"mydata":detial})

############################################################ UPDATE   ###############################################

def update(request,id,user,department,year):
    if request.method=='POST':
        obj = models.Student.objects.get(id=id)
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save() 
        return redirect("studentAdmin",user,department,year)
    else:
        obj = models.Student.objects.get(id=id)
        return render(request,"update.html",{"data":obj})   

######################################################### DELETE ##################################################

def delete(request,id,user,department,year):
    obj = models.Student.objects.get(id = id)
    obj.delete()
    return redirect("studentAdmin",user,department,year)

######################################################### ADD DATA  ##############################################

def adddata(request,user,department,year):
    obj1 = models.Staff.objects.get(staffUsername=user) 
    obj2 = models.Student()
    obj2.name = request.POST["names"]
    obj2.reg = request.POST["r_number"]
    obj2.s_mobile = request.POST["s_number"]
    obj2.p_mobile = request.POST["p_number"]
    obj2.clg = str(obj1.staffCollege)
    obj2.department = str(department) 
    obj2.year = str(year)
    obj2.save()
    return redirect("studentAdmin",user,department,year)

##########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   SUBMIT   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################
def cse3_submit(request,user):
    l =[]
    obj = models.cse3.objects.all()
    msg = Client("AC1ba7a196df0d06c089b7c582e7e0f19a","f9f7b1ecb04399300072ccc218ee63bf")
    otp= int(random.randint(1000,9999))
    msg.messages.create(body="you marked as absent",from_="+13148347594",to="+919361072610")
    for i in obj:
        if request.POST.get(str(i.id),False):
            print("present student :"+i.name)
            i.attendance=True
            l.append(i.name)
    print(l)
    return redirect("cse_first")