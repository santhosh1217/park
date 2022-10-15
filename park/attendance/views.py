from django.shortcuts import render

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



