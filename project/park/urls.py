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
   
    #update
    path("cse/first/admin/update/<int:id>",views.updatecse1,name="updatecse1"),
    path("cse/second/admin/update/<int:id>",views.updatecse2,name="updatecse1"),
    path("cse/third/admin/update/<int:id>",views.updatecse3,name="updatecse1"),
    path("cse/final/admin/update/<int:id>",views.updatecse4,name="updatecse1"),
    path("it/first/admin/update/<int:id>",views.updateit1,name="updateit1"),
    path("it/second/admin/update/<int:id>",views.updateit2,name="updateit1"),
    path("it/third/admin/update/<int:id>",views.updateit3,name="updateit1"),
    path("it/final/admin/update/<int:id>",views.updateit4,name="updateit1"),
    path("ece/first/admin/update/<int:id>",views.updateece1,name="updateece1"),
    path("ece/second/admin/update/<int:id>",views.updateece2,name="updateece1"),
    path("ece/third/admin/update/<int:id>",views.updateece3,name="updateece1"),
    path("ece/final/admin/update/<int:id>",views.updateece4,name="updateece1"),
    path("mech/first/admin/update/<int:id>",views.updatemech1,name="updatemech1"),
    path("mech/second/admin/update/<int:id>",views.updatemech2,name="updatemech1"),
    path("mech/third/admin/update/<int:id>",views.updatemech3,name="updatemech1"),
    path("mech/final/admin/update/<int:id>",views.updatemech4,name="updatemech1"),
    path("eee/first/admin/update/<int:id>",views.updateeee1,name="updateeee"),
    path("eee/second/admin/update/<int:id>",views.updateeee2,name="updateeee"),
    path("eee/third/admin/update/<int:id>",views.updateeee3,name="updateeee"),
    path("eee/final/admin/update/<int:id>",views.updateeee4,name="updateeee"),
    path("civil/first/admin/update/<int:id>",views.updatecivil1,name="updatecivil"),
    path("civil/second/admin/update/<int:id>",views.updatecivil2,name="updatecivil"),
    path("civil/third/admin/update/<int:id>",views.updatecivil3,name="updatecivil"),
    path("civil/final/admin/update/<int:id>",views.updatecivil4,name="updatecivil"),


    # delete
    path("cse/first/admin/delete/<int:id>",views.deletecse1,name="delete"),
    path("cse/second/admin/delete/<int:id>",views.deletecse2,name="delete"),
    path("cse/third/admin/delete/<int:id>",views.deletecse3,name="delete"),
    path("cse/final/admin/delete/<int:id>",views.deletecse4,name="delete"),
    path("it/first/admin/delete/<int:id>",views.deleteit1,name="delete"),
    path("it/second/admin/delete/<int:id>",views.deleteit2,name="delete"),
    path("it/third/admin/delete/<int:id>",views.deleteit3,name="delete"),
    path("it/final/admin/delete/<int:id>",views.deleteit4,name="delete"),
    path("ece/first/admin/delete/<int:id>",views.deleteece1,name="delete"),
    path("ece/second/admin/delete/<int:id>",views.deleteece2,name="delete"),
    path("ece/third/admin/delete/<int:id>",views.deleteece3,name="delete"),
    path("ece/final/admin/delete/<int:id>",views.deleteece4,name="delete"),
    path("mech/first/admin/delete/<int:id>",views.deletemech1,name="delete"),
    path("mech/second/admin/delete/<int:id>",views.deletemech2,name="delete"),
    path("mech/third/admin/delete/<int:id>",views.deletemech3,name="delete"),
    path("mech/final/admin/delete/<int:id>",views.deletemech4,name="delete"),
    path("eee/first/admin/delete/<int:id>",views.deleteeee1,name="delete"),
    path("eee/second/admin/delete/<int:id>",views.deleteeee2,name="delete"),
    path("eee/third/admin/delete/<int:id>",views.deleteeee3,name="delete"),
    path("eee/final/admin/delete/<int:id>",views.deleteeee4,name="delete"),
    path("civil/first/admin/delete/<int:id>",views.deletecivil1,name="delete"),
    path("civil/second/admin/delete/<int:id>",views.deletecivil2,name="delete"),
    path("civil/third/admin/delete/<int:id>",views.deletecivil3,name="delete"),
    path("civil/final/admin/delete/<int:id>",views.deletecivil4,name="delete"),

    path("cse",views.year),
    path("it",views.year),
    path("ece",views.year),
    path("eee",views.year),
    path("mech",views.year),
    path("civil",views.year),

    path("cse/first/",views.cse_first),
    path("cse/second/", views.cse_second),
    path("cse/third/", views.cse_third),
    path("cse/final/", views.cse_final),

    path("ece/first/", views.ece_first),
    path("ece/second/", views.ece_second),
    path("ece/third/", views.ece_third),
    path("ece/final/", views.ece_final),

    path("it/first/", views.it_first),
    path("it/second/", views.it_second),
    path("it/third/", views.it_third),
    path("it/final/", views.it_final),

    path("mech/first/", views.mech_first),
    path("mech/second/", views.mech_second),
    path("mech/third/", views.mech_third),
    path("mech/final/", views.mech_final),

    path("eee/first/", views.eee_first),
    path("eee/second/", views.eee_second),
    path("eee/third/", views.eee_third),
    path("eee/final/", views.eee_final),

    path("civil/first/", views.civil_first),
    path("civil/second/", views.civil_second),
    path("civil/third/", views.civil_third),
    path("civil/final/", views.civil_final),

    path("cse/first/admin/",views.cse1_admin,name="cse1"),
    path("cse/second/admin/", views.cse2_admin,name="cse2"),
    path("cse/third/admin/", views.cse3_admin,name="cse3"),
    path("cse/final/admin/", views.cse4_admin,name="cse4"),

    path("it/first/admin/", views.it1_admin,name="it1"),
    path("it/second/admin/", views.it2_admin,name="it2"),
    path("it/third/admin/", views.it3_admin,name="it3"),
    path("it/final/admin/", views.it4_admin,name="it4"),

    path("eee/first/admin/", views.eee1_admin,name="eee1"),
    path("eee/second/admin/", views.eee2_admin,name="eee2"),
    path("eee/third/admin/", views.eee3_admin,name="eee3"),
    path("eee/final/admin/", views.eee4_admin,name="eee4"),

    path("ece/first/admin/", views.ece1_admin,name="ece1"),
    path("ece/second/admin/", views.ece2_admin,name="ece2"),
    path("ece/third/admin/", views.ece3_admin,name="ece3"),
    path("ece/final/admin/", views.ece4_admin,name="ece4"),

    path("mech/first/admin/", views.mech1_admin,name="mech1"),
    path("mech/second/admin/", views.mech2_admin,name="mech2"),
    path("mech/third/admin/", views.mech3_admin,name="mech3"),
    path("mech/final/admin/", views.mech4_admin,name="mech4"),

    path("civil/first/admin/", views.civil1_admin,name="civil1"),
    path("civil/second/admin/", views.civil2_admin,name="civil2"),
    path("civil/third/admin/", views.civil3_admin,name="civil3"),
    path("civil/final/admin/", views.civil4_admin,name="civil4"),

    path("cse/first/admin/adddata",views.cse1_adddata),
    path("cse/second/admin/adddata", views.cse2_adddata),
    path("cse/third/admin/adddata", views.cse3_adddata),
    path("cse/final/admin/adddata", views.cse4_adddata),

    path("it/first/admin/adddata", views.it1_adddata),
    path("it/second/admin/adddata", views.it2_adddata),
    path("it/third/admin/adddata", views.it3_adddata),
    path("it/final/admin/adddata", views.it4_adddata),

    path("ece/first/admin/adddata", views.ece1_adddata),
    path("ece/second/admin/adddata", views.ece2_adddata),
    path("ece/third/admin/adddata", views.ece3_adddata),
    path("ece/final/admin/adddata", views.ece4_adddata),

    path("eee/first/admin/adddata", views.eee1_adddata),
    path("eee/second/admin/adddata", views.eee2_adddata),
    path("eee/third/admin/adddata", views.eee3_adddata),
    path("eee/final/admin/adddata", views.eee4_adddata),

    path("mech/first/admin/adddata", views.mech1_adddata),
    path("mech/second/admin/adddata", views.mech2_adddata),
    path("mech/third/admin/adddata", views.mech3_adddata),
    path("mech/final/admin/adddata", views.mech4_adddata),

    path("civil/first/admin/adddata", views.civil1_adddata),
    path("civil/second/admin/adddata", views.civil2_adddata),
    path("civil/third/admin/adddata", views.civil3_adddata),
    path("civil/final/admin/adddata", views.civil4_adddata),
    path("cse/third/submit/",views.cse3_submit),



]
