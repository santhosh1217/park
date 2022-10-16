import re
from django.shortcuts import redirect, render
from attendance import models

# Create your views here.


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

def table(request):
    data=models.cse3.objects.all()
    if(data!=''):
        return render(request,'index.html',{'mydata':data})
    else:
        return render(request,'index.html')


#cse
def cse_first(request):
    record = models.cse1.objects.all()
    message = {"year": "first year","department":"computer science","detial":record }
    return render(request,"attendance.html",message)

def cse_second(request):
    record = models.cse2.objects.all()
    message = {"year": "second year","department":"computer science ","detial":record}
    return render(request,"attendance.html",message)

def cse_third(request):
    record = models.cse3.objects.all()
    message = {"year": "third year","department":"computer science","detial":record}
    return render(request,"attendance.html",message)

def cse_final(request):
    record = models.cse4.objects.all()
    message = {"year": "final year","department":"computer science ","detial":record}
    return render(request,"attendance.html",message)

#it
def it_first(request):
    record = models.it1.objects.all()
    message = {"year": "first year","department":"information technology ","detial":record}
    return render(request,"attendance.html",message)

def it_second(request):
    record = models.it2.objects.all()
    message = {"year": "second year","department":"information technology ","detial":record}
    return render(request,"attendance.html",message)

def it_third(request):
    record = models.it3.objects.all()
    message = {"year": "third year","department":"information technology","detial":record}
    return render(request,"attendance.html",message)

def it_final(request):
    record = models.it4.objects.all()
    message = {"year": "final year","department":"information technology","detial":record}
    return render(request,"attendance.html",message)

#ece
def ece_first(request):
    record = models.ece1.objects.all()
    message = {"year": "first year","department":"electronics and communication engineering","detial":record}
    return render(request,"attendance.html",message)

def ece_second(request):
    record = models.ece2.objects.all()
    message = {"year": "second year","department":"electronics and communication engineering","detial":record}
    return render(request,"attendance.html",message)

def ece_third(request):
    record = models.ece3.objects.all()
    message = {"year": "third year","department":"electronics and communication engineering","detial":record}
    return render(request,"attendance.html",message)

def ece_final(request):
    record = models.ece4.objects.all()
    message = {"year": "final year","department":"electronics and communication engineering","detial":record}
    return render(request,"attendance.html",message)

#mech
def mech_first(request):
    record = models.mech1.objects.all()
    message = {"year": "first year","department":"mechanical","detial":record}
    return render(request,"attendance.html",message)

def mech_second(request):
    record = models.mech2.objects.all()
    message = {"year": "second year","department":"mechanical","detial":record}
    return render(request,"attendance.html",message)

def mech_third(request):
    record = models.mech3.objects.all()
    message = {"year": "third year","department":"mechanical","detial":record}
    return render(request,"attendance.html",message)

def mech_final(request):
    record = models.mech4.objects.all()
    message = {"year": "final year","department":"mechanical","detial":record}
    return render(request,"attendance.html",message)


def civil_first(request):
    record = models.civil1.objects.all()
    message = {"year": "first year","department":"civil","detial":record}
    return render(request,"attendance.html",message)

def civil_second(request):
    record = models.civil2.objects.all()
    message = {"year": "second year","department":"civil","detial":record}
    return render(request,"attendance.html",message)

def civil_third(request):
    record = models.civil3.objects.all()
    message = {"year": "third year","department":"civil","detial":record}
    return render(request,"attendance.html",message)

def civil_final(request):
    record = models.civil4.objects.all()
    message = {"year": "final year","department":"civil","detial":record}
    return render(request,"attendance.html",message)


def eee_first(request):
    record = models.eee1.objects.all()
    message = {"year": "first year","department":"electrical and electronics engineering","detial":record}
    return render(request,"attendance.html",message)

def eee_second(request):
    record = models.eee2.objects.all()
    message = {"year": "second year","department":"electrical and electronics engineering","detial":record}
    return render(request,"attendance.html",message)

def eee_third(request):
    record = models.eee3.objects.all()
    message = {"year": "third year","department":"electrical and electronics engineering","detial":record}
    return render(request,"attendance.html",message)

def eee_final(request):
    record = models.eee4.objects.all()
    message = {"year": "final year","department":"electrical and electronics engineering","detial":record}
    return render(request,"attendance.html",message)













def cse1_admin(request):
    data = models.cse1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def cse2_admin(request):
    data = models.cse2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def cse3_admin(request):
    data = models.cse3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def cse4_admin(request):
    data = models.cse4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def it1_admin(request):
    data = models.it1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def it2_admin(request):
    data = models.it2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def it3_admin(request):
    data = models.it3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def it4_admin(request):
    data = models.it4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def ece1_admin(request):
    data = models.ece1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def ece2_admin(request):
    data = models.ece2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def ece3_admin(request):
    data = models.ece3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def ece4_admin(request):
    data = models.ece4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def eee1_admin(request):
    data = models.eee1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def eee2_admin(request):
    data = models.eee2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def eee3_admin(request):
    data = models.eee3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def eee4_admin(request):
    data = models.eee4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def mech1_admin(request):
    data = models.mech1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def mech2_admin(request):
    data = models.mech2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def mech3_admin(request):
    data = models.mech3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def mech4_admin(request):
    data = models.mech4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def civil1_admin(request):
    data = models.civil1.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def civil2_admin(request):
    data = models.civil2.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def civil3_admin(request):
    data = models.civil3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def civil4_admin(request):
    data = models.civil4.objects.all()
    return render(request,"addstudent.html",{"mydata":data})

def updatecse1(request,id):    
    obj=models.cse1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/cse/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecse2(request,id):    
    obj=models.cse2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/cse/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecse3(request,id):    
    obj=models.cse3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/cse/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecse4(request,id):    
    obj=models.cse4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/cse/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateit1(request,id):    
    obj=models.it1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/it/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateit2(request,id):    
    obj=models.it2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/it/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateit3(request,id):    
    obj=models.it3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/it/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateit4(request,id):    
    obj=models.it4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/it/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateece1(request,id):    
    obj=models.ece1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/ece/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateece2(request,id):    
    obj=models.ece2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/ece/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateece3(request,id):    
    obj=models.ece3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/ece/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateece4(request,id):    
    obj=models.ece4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/ece/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatemech1(request,id):    
    obj=models.mech1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/mech/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatemech2(request,id):    
    obj=models.mech2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/mech/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatemech3(request,id):    
    obj=models.mech3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/mech/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatemech4(request,id):    
    obj=models.mech4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/mech/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateeee1(request,id):    
    obj=models.eee1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/eee/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateeee2(request,id):    
    obj=models.eee2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/eee/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateeee3(request,id):    
    obj=models.eee3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/eee/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updateeee4(request,id):    
    obj=models.eee4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/eee/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecivil1(request,id):    
    obj=models.civil1.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/civil/first/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecivil2(request,id):    
    obj=models.civil2.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/civil/second/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecivil3(request,id):    
    obj=models.civil3.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/civil/third/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
def updatecivil4(request,id):    
    obj=models.civil4.objects.get(id=id)
    if request.method=='POST':
        obj.name = request.POST["sname"]
        obj.reg = request.POST["regnum"]
        obj.s_mobile = request.POST["s_number"]
        obj.p_mobile = request.POST["p_number"]
        obj.save()
        return redirect("http://127.0.0.1:8000/civil/final/admin/")
    print(obj)
 
    return render(request,"update.html",{'data':obj}) 
 
def deletecse1(request,id):
        mydata=models.cse1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('cse1')
def deletecse2(request,id):
        mydata=models.cse2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('cse2')
def deletecse3(request,id):
        mydata=models.cse3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect("cse3")
def deletecse4(request,id):
        mydata=models.cse4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('cse4')
def deleteit1(request,id):
        mydata=models.it1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('it1')
def deleteit2(request,id):
        mydata=models.it2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('it2')
def deleteit3(request,id):
        mydata=models.it3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('it3')
def deleteit4(request,id):
        mydata=models.it4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('it4')
def deleteece1(request,id):
        mydata=models.ece1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('ece1')
def deleteece2(request,id):
        mydata=models.ece2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('ece2')
def deleteece3(request,id):
        mydata=models.ece3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('ece3')
def deleteece4(request,id):
        mydata=models.ece4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('ece4')
def deletemech1(request,id):
        mydata=models.mech1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('mech1')
def deletemech2(request,id):
        mydata=models.mech2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('mech2')
def deletemech3(request,id):
        mydata=models.mech3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('mech3')
def deletemech4(request,id):
        mydata=models.mech4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('mech4')
def deleteeee1(request,id):
        mydata=models.eee1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('eee1')
def deleteeee2(request,id):
        mydata=models.eee2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('eee2')
def deleteeee3(request,id):
        mydata=models.eee3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('eee3')
def deleteeee4(request,id):
        mydata=models.eee4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('eee4')
def deletecivil1(request,id):
        mydata=models.civil1.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('civil1')
def deletecivil2(request,id):
        mydata=models.civil2.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('civil2')
def deletecivil3(request,id):
        mydata=models.civil3.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('civil3')
def deletecivil4(request,id):
        mydata=models.civil4.objects.get(id=id)
        print(mydata)
        mydata.delete()
        return redirect('civi4')
def cse1_adddata(request):
    obj = models.cse1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/cse/first/admin/')

def cse2_adddata(request):  
    obj = models.cse2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/cse/second/admin/')

def cse3_adddata(request):    
    obj = models.cse3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    print("path "+str(request.get_full_path))
    return redirect('http://127.0.0.1:8000/cse/third/admin/')


def cse4_adddata(request):     
    obj = models.cse4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    print("path "+str(request.get_full_path))
    return redirect('http://127.0.0.1:8000/cse/final/admin/')

def it1_adddata(request):  
    obj = models.it1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/it/first/admin/')

def it2_adddata(request):
    obj = models.it2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/it/second/admin/')

def it3_adddata(request):
    obj = models.it3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/it/third/admin/')

def it4_adddata(request):
    obj = models.it4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/it/final/admin/')

def ece1_adddata(request):
    obj = models.ece1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/ece/first/admin/')

def ece2_adddata(request):
    obj = models.ece2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/ece/second/admin/')
def ece3_adddata(request):
    obj = models.ece3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/ece/third/admin/')

def ece4_adddata(request):
    obj = models.ece4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/ece/final/admin/')

def eee1_adddata(request):
    obj = models.eee1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/eee/first/admin/')

def eee2_adddata(request):
    obj = models.eee2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/eee/second/admin/')

def eee3_adddata(request):
    obj = models.eee3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/eee/third/admin/')

def eee4_adddata(request):
    obj = models.eee4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/eee/final/admin/')

def mech1_adddata(request):
    obj = models.mech1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/mech/first/admin/')

def mech2_adddata(request):
    obj = models.mech2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/mech/second/admin/')

def mech3_adddata(request):
    obj = models.mech3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/mech/third/admin/')

def mech4_adddata(request):
    obj = models.mech4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/mech/final/admin/')

def civil1_adddata(request):
    obj = models.civil1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/civil/first/admin/')

def civil2_adddata(request):
    obj = models.civil2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/civil/second/admin/')

def civil3_adddata(request):
    obj = models.civil3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/civil/third/admin/')

def civil4_adddata(request):
    obj = models.civil4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect('http://127.0.0.1:8000/civil/final/admin/')

def cse3_submit(request):
    obj = models.cse3.objects.all()
    for i in obj:
        print(i.name)
        print(i.reg)
        if models.cse3.objects.get(name = str(request.POST[str(i.reg)])):

            print(str(request.POST(str(i.reg))))


    return redirect("http://127.0.0.1:8000/cse/third/")


    



