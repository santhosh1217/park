"""park URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from attendance import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.login,name="login"),
   
    #######################################################################  UPDATE  ###################################
    path("cse/1/admin/update/<int:id>",views.update,name="updatecse1"),
    path("cse/2/admin/update/<int:id>",views.update,name="updatecse1"),
    path("cse/3/admin/update/<int:id>",views.update,name="updatecse1"),
    path("cse/4/admin/update/<int:id>",views.update,name="updatecse1"),
    path("it/1/admin/update/<int:id>",views.update,name="updateit1"),
    path("it/2/admin/update/<int:id>",views.update,name="updateit1"),
    path("it/3/admin/update/<int:id>",views.update,name="updateit1"),
    path("it/4/admin/update/<int:id>",views.update,name="updateit1"),
    path("ece/1/admin/update/<int:id>",views.update,name="updateece1"),
    path("ece/2/admin/update/<int:id>",views.update,name="updateece1"),
    path("ece/3/admin/update/<int:id>",views.update,name="updateece1"),
    path("ece/4/admin/update/<int:id>",views.update,name="updateece1"),
    path("mech/1/admin/update/<int:id>",views.update,name="updatemech1"),
    path("mech/2/admin/update/<int:id>",views.update,name="updatemech1"),
    path("mech/3/admin/update/<int:id>",views.update,name="updatemech1"),
    path("mech/4/admin/update/<int:id>",views.update,name="updatemech1"),
    path("eee/1/admin/update/<int:id>",views.update,name="updateeee"),
    path("eee/2/admin/update/<int:id>",views.update,name="updateeee"),
    path("eee/3/admin/update/<int:id>",views.update,name="updateeee"),
    path("eee/4/admin/update/<int:id>",views.update,name="updateeee"),
    path("civil/1/admin/update/<int:id>",views.update,name="updatecivil"),
    path("civil/2/admin/update/<int:id>",views.update,name="updatecivil"),
    path("civil/3/admin/update/<int:id>",views.update,name="updatecivil"),
    path("civil/4/admin/update/<int:id>",views.update,name="updatecivil"),


#############################################################################  DELETE  ##################################
    path("cse/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("cse/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("cse/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("cse/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("it/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("it/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("it/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("it/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("ece/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("ece/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("ece/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("ece/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("mech/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("mech/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("mech/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("mech/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("eee/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("eee/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("eee/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("eee/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("civil/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("civil/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("civil/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("civil/4/admin/delete/<int:id>",views.delete,name="delete"),

    path("cse",views.year),
    path("it",views.year),
    path("ece",views.year),
    path("eee",views.year),
    path("mech",views.year),
    path("civil",views.year),

    path("cse/1/",views.department),
    path("cse/2/", views.department),
    path("cse/3/", views.department),
    path("cse/4/", views.department),

    path("ece/1/", views.department),
    path("ece/2/", views.department),
    path("ece/3/", views.department),
    path("ece/4/", views.department),

    path("it/1/", views.department),
    path("it/2/", views.department),
    path("it/3/", views.department),
    path("it/4/", views.department),

    path("mech/1/", views.department),
    path("mech/2/", views.department),
    path("mech/3/", views.department),
    path("mech/4/", views.department),

    path("eee/1/", views.department),
    path("eee/2/", views.department),
    path("eee/3/", views.department),
    path("eee/4/", views.department),

    path("civil/1/", views.department),
    path("civil/2/", views.department),
    path("civil/3/", views.department),
    path("civil/4/", views.department),

    path("cse/1/admin/",views.admin,name="cse1"),
    path("cse/2/admin/", views.admin,name="cse2"),
    path("cse/3/admin/", views.admin,name="cse3"),
    path("cse/4/admin/", views.admin,name="cse4"),

    path("it/1/admin/", views.admin,name="it1"),
    path("it/2/admin/", views.admin,name="it2"),
    path("it/3/admin/", views.admin,name="it3"),
    path("it/4/admin/", views.admin,name="it4"),

    path("eee/1/admin/", views.admin,name="eee1"),
    path("eee/2/admin/", views.admin,name="eee2"),
    path("eee/3/admin/", views.admin,name="eee3"),
    path("eee/4/admin/", views.admin,name="eee4"),
    path("ece/1/admin/", views.admin,name="ece1"),
    path("ece/2/admin/", views.admin,name="ece2"),
    path("ece/3/admin/", views.admin,name="ece3"),
    path("ece/4/admin/", views.admin,name="ece4"),

    path("mech/1/admin/", views.admin,name="mech1"),
    path("mech/2/admin/", views.admin,name="mech2"),
    path("mech/3/admin/", views.admin,name="mech3"),
    path("mech/4/admin/", views.admin,name="mech4"),

    path("civil/1/admin/", views.admin,name="civil1"),
    path("civil/2/admin/", views.admin,name="civil2"),
    path("civil/3/admin/", views.admin,name="civil3"),
    path("civil/4/admin/", views.admin,name="civil4"),

    path("cse/1/admin/adddata",views.adddata),
    path("cse/2/admin/adddata", views.adddata),
    path("cse/3/admin/adddata", views.adddata),
    path("cse/4/admin/adddata", views.adddata),

    path("it/1/admin/adddata", views.adddata),
    path("it/2/admin/adddata", views.adddata),
    path("it/3/admin/adddata", views.adddata),
    path("it/4/admin/adddata", views.adddata),

    path("ece/1/admin/adddata", views.adddata),
    path("ece/2/admin/adddata", views.adddata),
    path("ece/3/admin/adddata", views.adddata),
    path("ece/4/admin/adddata", views.adddata),

    path("eee/1/admin/adddata", views.adddata),
    path("eee/2/admin/adddata", views.adddata),
    path("eee/3/admin/adddata", views.adddata),
    path("eee/4/admin/adddata", views.adddata),

    path("mech/1/admin/adddata", views.adddata),
    path("mech/2/admin/adddata", views.adddata),
    path("mech/3/admin/adddata", views.adddata),
    path("mech/4/admin/adddata", views.adddata),

    path("civil/1/admin/adddata", views.adddata),
    path("civil/2/admin/adddata", views.adddata),
    path("civil/3/admin/adddata", views.adddata),
    path("civil/4/admin/adddata", views.adddata),

    path("cse/third/submit/",views.cse3_submit),



]
