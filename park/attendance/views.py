from django.shortcuts import render, redirect
from attendance import models

# Create your views here.


def login(request):
    return render(request, "login.html")


def dep(request):
    username = request.POST['u']
    password = request.POST['p']
    print(username+password)

    if username=="park" and password=="7122":

        return render(request, "department.html")

    else:
        data = {"msg": "invalid"}
        return render(request, "login.html",{"msg": "invalid"})


def year(request):

    return render(request, "year.html")

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

def cse1_adddata(request):
    obj = models.cse1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/cse/year/first/admin")

def cse2_adddata(request):
    obj = models.cse2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/cse/year/second/admin")

def cse3_adddata(request):
    obj = models.cse3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/cse/year/third/admin")

def cse4_adddata(request):
    obj = models.cse4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/cse/year/final/admin")

def it1_adddata(request):
    obj = models.it1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/it/year/first/admin")

def it2_adddata(request):
    obj = models.it2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/it/year/second/admin")

def it3_adddata(request):
    obj = models.it3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/it/year/third/admin")

def it4_adddata(request):
    obj = models.it4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/it/year/final/admin")

def ece1_adddata(request):
    obj = models.ece1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/ece/year/first/admin")

def ece2_adddata(request):
    obj = models.ece2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/ece/year/second/admin")

def ece3_adddata(request):
    obj = models.ece3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/ece/year/third/admin")

def ece4_adddata(request):
    obj = models.ece4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/ece/year/final/admin")

def eee1_adddata(request):
    obj = models.eee1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/eee/year/first/admin")

def eee2_adddata(request):
    obj = models.eee2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/eee/year/second/admin")

def eee3_adddata(request):
    obj = models.eee3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/eee/year/third/admin")

def eee4_adddata(request):
    obj = models.eee4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/eee/year/final/admin")

def mech1_adddata(request):
    obj = models.mech1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/mech/year/first/admin")

def mech2_adddata(request):
    obj = models.mech2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/mech/year/second/admin")

def mech3_adddata(request):
    obj = models.mech3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/mech/year/third/admin")

def mech4_adddata(request):
    obj = models.mech4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/mech/year/final/admin")

def civil1_adddata(request):
    obj = models.civil1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/civil/year/first/admin")

def civil2_adddata(request):
    obj = models.civil2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/civil/year/second/admin")

def civil3_adddata(request):
    obj = models.civil3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/civil/year/third/admin")

def civil4_adddata(request):
    obj = models.civil4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return redirect("http://127.0.0.1:8000/department/civil/year/final/admin")



