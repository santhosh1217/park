from django.shortcuts import render
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
    message = {"year": "first year","department":"computer science "}
    return render(request,"attendance.html",message)

def cse_second(request):
    message = {"year": "second year","department":"computer science "}
    return render(request,"attendance.html",message)

def cse_third(request):
    message = {"year": "third year","department":"computer science "}
    return render(request,"attendance.html",message)

def cse_final(request):
    message = {"year": "final year","department":"computer science "}
    return render(request,"attendance.html",message)

#it
def it_first(request):
    message = {"year": "first year","department":"information technology "}
    return render(request,"attendance.html",message)

def it_second(request):
    message = {"year": "second year","department":"information technology "}
    return render(request,"attendance.html",message)

def it_third(request):
    message = {"year": "third year","department":"information technology"}
    return render(request,"attendance.html",message)

def it_final(request):
    message = {"year": "final year","department":"information technology"}
    return render(request,"attendance.html",message)

#ece
def ece_first(request):
    message = {"year": "first year","department":"electronics and communication engineering"}
    return render(request,"attendance.html",message)

def ece_second(request):
    message = {"year": "second year","department":"electronics and communication engineering"}
    return render(request,"attendance.html",message)

def ece_third(request):
    message = {"year": "third year","department":"electronics and communication engineering"}
    return render(request,"attendance.html",message)

def ece_final(request):
    message = {"year": "final year","department":"electronics and communication engineering"}
    return render(request,"attendance.html",message)

#mech
def mech_first(request):
    message = {"year": "first year","department":"mechanical"}
    return render(request,"attendance.html",message)

def mech_second(request):
    message = {"year": "second year","department":"mechanical"}
    return render(request,"attendance.html",message)

def mech_third(request):
    message = {"year": "third year","department":"mechanical"}
    return render(request,"attendance.html",message)

def mech_final(request):
    message = {"year": "final year","department":"mechanical"}
    return render(request,"attendance.html",message)


def civil_first(request):
    message = {"year": "first year","department":"civil"}
    return render(request,"attendance.html",message)

def civil_second(request):
    message = {"year": "second year","department":"civil"}
    return render(request,"attendance.html",message)

def civil_third(request):
    message = {"year": "third year","department":"civil"}
    return render(request,"attendance.html",message)

def civil_final(request):
    message = {"year": "final year","department":"civil"}
    return render(request,"attendance.html",message)


def eee_first(request):
    message = {"year": "first year","department":"electrical and electronics engineering"}
    return render(request,"attendance.html",message)

def eee_second(request):
    message = {"year": "second year","department":"electrical and electronics engineering"}
    return render(request,"attendance.html",message)

def eee_third(request):
    message = {"year": "third year","department":"electrical and electronics engineering"}
    return render(request,"attendance.html",message)

def eee_final(request):
    message = {"year": "final year","department":"electrical and electronics engineering"}
    return render(request,"attendance.html",message)


def cse1_admin(request):
    mydata = models.cse1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def cse2_admin(request):
    mydata = models.cse2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def cse3_admin(request):
    data = models.cse3.objects.all()
    return render(request,"addstudent.html",{"mydata":data})
def cse4_admin(request):
    mydata = models.cse4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def it1_admin(request):
    mydata = models.it1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def it2_admin(request):
    mydata = models.it2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def it3_admin(request):
    mydata = models.it3.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def it4_admin(request):
    mydata = models.it4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def ece1_admin(request):
    mydata = models.ece1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def ece2_admin(request):
    mydata = models.ece2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def ece3_admin(request):
    mydata = models.ece3.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def ece4_admin(request):
    mydata = models.ece4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def eee1_admin(request):
    mydata = models.eee1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def eee2_admin(request):
    mydata = models.eee2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def eee3_admin(request):
    mydata = models.eee3.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def eee4_admin(request):
    mydata = models.eee4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def mech1_admin(request):
    mydata = models.mech1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def mech2_admin(request):
    mydata = models.mech2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def mech3_admin(request):
    mydata = models.mech3.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def mech4_admin(request):
    mydata = models.mech4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def civil1_admin(request):
    mydata = models.civil1.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def civil2_admin(request):
    mydata = models.civil2.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})
def civil3_admin(request):
    mydata = models.civil3.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def civil4_admin(request):
    mydata = models.civil4.objects.all()
    return render(request,"addstudent.html",{"datas":mydata})

def cse1_adddata(request):
    obj = models.cse1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def cse2_adddata(request):
    obj = models.cse2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def cse3_adddata(request):
    obj = models.cse3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def cse4_adddata(request):
    obj = models.cse4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def it1_adddata(request):
    obj = models.it1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def it2_adddata(request):
    obj = models.it2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def it3_adddata(request):
    obj = models.it3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def it4_adddata(request):
    obj = models.it4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def ece1_adddata(request):
    obj = models.ece1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def ece2_adddata(request):
    obj = models.ece2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def ece3_adddata(request):
    obj = models.ece3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def ece4_adddata(request):
    obj = models.ece4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def eee1_adddata(request):
    obj = models.eee1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def eee2_adddata(request):
    obj = models.eee2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def eee3_adddata(request):
    obj = models.eee3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def eee4_adddata(request):
    obj = models.eee4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def mech1_adddata(request):
    obj = models.mech1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def mech2_adddata(request):
    obj = models.mech2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def mech3_adddata(request):
    obj = models.mech3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def mech4_adddata(request):
    obj = models.mech4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def civil1_adddata(request):
    obj = models.civil1()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def civil2_adddata(request):
    obj = models.civil2()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def civil3_adddata(request):
    obj = models.civil3()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)

def civil4_adddata(request):
    obj = models.civil4()
    obj.name = request.POST["nam"]
    obj.reg = request.POST["rnumber"]
    obj.s_mobile = request.POST["snumber"]
    obj.p_mobile = request.POST["pnumber"]
    obj.save()
    return render(request,"addstudent.html",)



