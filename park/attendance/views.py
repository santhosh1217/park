from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "login.html")




def dep(request):
    username = request.POST['u']
    password = request.POST['p']
    print(username+password)

    if username=="park" and password=="1234":
        data = {"msg": "invalid"}
        return render(request, "department.html",data)

    else:

        return render(request, "login.html")



def year(request):
    return render(request, "year.html")
