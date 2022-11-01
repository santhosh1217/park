from os import link
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from attendance import models
from twilio.rest import Client
import random

def login(request):
    if request.method == "POST":
        username = request.POST['u']
        password = request.POST['p']
        if username=="park" and password=="7122":
            return render(request, "department.html")
        else:
            data = {"msg": "invalid"}
            return render(request,"login.html",{"msg": "invalid"})
    else:
        return render(request, "login.html")

def year(request):
    return render(request, "year.html",{"link":str(request.path)})

def department(request):
    dep = request.get_full_path()
    url_list = dep.split('/')
    dic={"cse1":models.cse1,"cse2":models.cse2,"cse3":models.cse3,"cse4":models.cse4,"it1":models.it1,"it2":models.it2,"it3":models.it3,"it4":models.it4,"ece1":models.ece1,"ece2":models.ece2,"ece3":models.ece3,"ece4":models.ece4,"eee1":models.eee1,"eee2":models.eee2,"eee3":models.eee3,"eee4":models.eee4,"mech1":models.mech1,"mech2":models.mech2,"mech3":models.mech3,"mech4":models.mech4,"civil1":models.civil1,"civil2":models.civil2,"civil3":models.civil3,"civil4":models.civil4}
    urlatt=str(url_list[1]+url_list[2])
    year = {"1":"first year","2":"second year","3":"third year","4":"final year"}
    depart = {"cse":"computer science","it":"information technology","ece":"electronics and communication ","eee":"electrical and electronics","mech":"mechanical","civil":"civil"}
    record = dic.get(urlatt).objects.all()
    message = {"year": year.get(url_list[2]),"department":depart.get(url_list[1]),"detial":record }
    return render(request,"attendance.html",message)
##############################################################  ADMIN  ###############################################
def admin(request):
    url=request.get_full_path()
    url_list=url.split("/")
    dic={"cse1":models.cse1,"cse2":models.cse2,"cse3":models.cse3,"cse4":models.cse4,"it1":models.it1,"it2":models.it2,"it3":models.it3,"it4":models.it4,"ece1":models.ece1,"ece2":models.ece2,"ece3":models.ece3,"ece4":models.ece4,"eee1":models.eee1,"eee2":models.eee2,"eee3":models.eee3,"eee4":models.eee4,"mech1":models.mech1,"mech2":models.mech2,"mech3":models.mech3,"mech4":models.mech4,"civil1":models.civil1,"civil2":models.civil2,"civil3":models.civil3,"civil4":models.civil4}
    urlatt=str(url_list[1]+url_list[2])   
    obj=dic.get(urlatt).objects.all()
    print(obj)
    return render(request,"addstudent.html",{"mydata":obj})
##################################################################    UPDATE   #######################################
def update(request,id):
    url=request.get_full_path()
    url_list=url.split("/")
    dic={"cse1":models.cse1,"cse2":models.cse2,"cse3":models.cse3,"cse4":models.cse4,"it1":models.it1,"it2":models.it2,"it3":models.it3,"it4":models.it4,"ece1":models.ece1,"ece2":models.ece2,"ece3":models.ece3,"ece4":models.ece4,"eee1":models.eee1,"eee2":models.eee2,"eee3":models.eee3,"eee4":models.eee4,"mech1":models.mech1,"mech2":models.mech2,"mech3":models.mech3,"mech4":models.mech4,"civil1":models.civil1,"civil2":models.civil2,"civil3":models.civil3,"civil4":models.civil4}
    urlatt=str(url_list[1]+url_list[2])   
    obj=dic.get(urlatt).objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect(urlatt)
    print(obj)
    return render(request,"update.html",{'data':obj}) 
######################################################### DELETE ##################################################
def delete(request,id):
       url=request.get_full_path()
       url_list=url.split("/")
       dic={"cse1":models.cse1,"cse2":models.cse2,"cse3":models.cse3,"cse4":models.cse4,"it1":models.it1,"it2":models.it2,"it3":models.it3,"it4":models.it4,"ece1":models.ece1,"ece2":models.ece2,"ece3":models.ece3,"ece4":models.ece4,"eee1":models.eee1,"eee2":models.eee2,"eee3":models.eee3,"eee4":models.eee4,"mech1":models.mech1,"mech2":models.mech2,"mech3":models.mech3,"mech4":models.mech4,"civil1":models.civil1,"civil2":models.civil2,"civil3":models.civil3,"civil4":models.civil4}
       urlatt=str(url_list[1]+url_list[2])
       mydata=dic.get(urlatt).objects.get(id=id)
       mydata.delete()
       return redirect(urlatt)
##############################################################  ADD DATA  #######################################################
def adddata(request):
    url=request.get_full_path()
    url_list=url.split("/")
    urlatt=str(url_list[1]+url_list[2]) 
    print(urlatt)
    dic={"cse1":models.cse1(),"cse2":models.cse2(),"cse3":models.cse3,"cse4":models.cse4,"it1":models.it1,"it2":models.it2,"it3":models.it3,"it4":models.it4,"ece1":models.ece1,"ece2":models.ece2,"ece3":models.ece3,"ece4":models.ece4,"eee1":models.eee1,"eee2":models.eee2,"eee3":models.eee3,"eee4":models.eee4,"mech1":models.mech1,"mech2":models.mech2,"mech3":models.mech3,"mech4":models.mech4,"civil1":models.civil1,"civil2":models.civil2,"civil3":models.civil3,"civil4":models.civil4}
    obj = dic.get(urlatt)
    print(obj)
    if request.method=="POST":
        obj.name = request.POST["names"]
        obj.reg = request.POST["r_number"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect(urlatt)
##########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   SUBMIT   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################
def cse3_submit(request):
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