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
    path("department/",views.dep),
    #update
    path("department/cse/year/first/update/<int:id>",views.updatecse1,name="updatecse1"),
    path("department/cse/year/second/update/<int:id>",views.updatecse2,name="updatecse1"),
    path("department/cse/year/third/update/<int:id>",views.updatecse3,name="updatecse1"),
    path("department/cse/year/final/update/<int:id>",views.updatecse4,name="updatecse1"),
    path("department/it/year/first/update/<int:id>",views.updateit1,name="updateit1"),
    path("department/it/year/second/update/<int:id>",views.updateit2,name="updateit1"),
    path("department/it/year/third/update/<int:id>",views.updateit3,name="updateit1"),
    path("department/it/year/final/update/<int:id>",views.updateit4,name="updateit1"),
    path("department/ece/year/first/update/<int:id>",views.updateece1,name="updateece1"),
    path("department/ece/year/second/update/<int:id>",views.updateece2,name="updateece1"),
    path("department/ece/year/third/update/<int:id>",views.updateece3,name="updateece1"),
    path("department/ece/year/final/update/<int:id>",views.updateece4,name="updateece1"),
    path("department/mech/year/first/update/<int:id>",views.updatemech1,name="updatemech1"),
    path("department/mech/year/second/update/<int:id>",views.updatemech2,name="updatemech1"),
    path("department/mech/year/third/update/<int:id>",views.updatemech3,name="updatemech1"),
    path("department/mech/year/final/update/<int:id>",views.updatemech4,name="updatemech1"),
    path("department/eee/year/first/update/<int:id>",views.updateeee1,name="updateeee"),
    path("department/eee/year/second/update/<int:id>",views.updateeee2,name="updateeee"),
    path("department/eee/year/third/update/<int:id>",views.updateeee3,name="updateeee"),
    path("department/eee/year/final/update/<int:id>",views.updateeee4,name="updateeee"),
    path("department/civil/year/first/update/<int:id>",views.updatecivil1,name="updatecivil"),
    path("department/civil/year/second/update/<int:id>",views.updatecivil2,name="updatecivil"),
    path("department/civil/year/third/update/<int:id>",views.updatecivil3,name="updatecivil"),
    path("department/civil/year/final/update/<int:id>",views.updatecivil4,name="updatecivil"),


    # delete
    path("department/cse/year/first/delete/<int:id>",views.deletecse1,name="delete"),
    path("department/cse/year/second/delete/<int:id>",views.deletecse2,name="delete"),
    path("department/cse/year/third/delete/<int:id>",views.deletecse3,name="delete"),
    path("department/cse/year/final/delete/<int:id>",views.deletecse4,name="delete"),
    path("department/it/year/first/delete/<int:id>",views.deleteit1,name="delete"),
    path("department/it/year/second/delete/<int:id>",views.deleteit2,name="delete"),
    path("department/it/year/third/delete/<int:id>",views.deleteit3,name="delete"),
    path("department/it/year/final/delete/<int:id>",views.deleteit4,name="delete"),
    path("department/ece/year/first/delete/<int:id>",views.deleteece1,name="delete"),
    path("department/ece/year/second/delete/<int:id>",views.deleteece2,name="delete"),
    path("department/ece/year/third/delete/<int:id>",views.deleteece3,name="delete"),
    path("department/ece/year/final/delete/<int:id>",views.deleteece4,name="delete"),
    path("department/mech/year/first/delete/<int:id>",views.deletemech1,name="delete"),
    path("department/mech/year/second/delete/<int:id>",views.deletemech2,name="delete"),
    path("department/mech/year/third/delete/<int:id>",views.deletemech3,name="delete"),
    path("department/mech/year/final/delete/<int:id>",views.deletemech4,name="delete"),
    path("department/eee/year/first/delete/<int:id>",views.deleteeee1,name="delete"),
    path("department/eee/year/second/delete/<int:id>",views.deleteeee2,name="delete"),
    path("department/eee/year/third/delete/<int:id>",views.deleteeee3,name="delete"),
    path("department/eee/year/final/delete/<int:id>",views.deleteeee4,name="delete"),
    path("department/civil/year/first/delete/<int:id>",views.deletecivil1,name="delete"),
    path("department/civil/year/second/delete/<int:id>",views.deletecivil2,name="delete"),
    path("department/civil/year/third/delete/<int:id>",views.deletecivil3,name="delete"),
    path("department/civil/year/final/delete/<int:id>",views.deletecivil4,name="delete"),

    path("department/cse/year/",views.year),
    path("department/it/year/",views.year),
    path("department/ece/year/",views.year),
    path("department/eee/year/",views.year),
    path("department/mech/year/",views.year),
    path("department/civil/year/",views.year),

    path("department/cse/year/first/",views.cse_first),
    path("department/cse/year/second/", views.cse_second),
    path("department/cse/year/third/", views.cse_third),
    path("department/cse/year/final/", views.cse_final),

    path("department/ece/year/first/", views.ece_first),
    path("department/ece/year/second/", views.ece_second),
    path("department/ece/year/third/", views.ece_third),
    path("department/ece/year/final/", views.ece_final),

    path("department/it/year/first/", views.it_first),
    path("department/it/year/second/", views.it_second),
    path("department/it/year/third/", views.it_third),
    path("department/it/year/final/", views.it_final),

    path("department/mech/year/first/", views.mech_first),
    path("department/mech/year/second/", views.mech_second),
    path("department/mech/year/third/", views.mech_third),
    path("department/mech/year/final/", views.mech_final),

    path("department/eee/year/first/", views.eee_first),
    path("department/eee/year/second/", views.eee_second),
    path("department/eee/year/third/", views.eee_third),
    path("department/eee/year/final/", views.eee_final),

    path("department/civil/year/first/", views.civil_first),
    path("department/civil/year/second/", views.civil_second),
    path("department/civil/year/third/", views.civil_third),
    path("department/civil/year/final/", views.civil_final),

    path("department/cse/year/first/admin",views.cse1_admin,name="cse1"),
    path("department/cse/year/second/admin", views.cse2_admin,name="cse2"),
    path("department/cse/year/third/admin", views.cse3_admin,name="cse3"),
    path("department/cse/year/final/admin", views.cse4_admin,name="cse4"),

    path("department/it/year/first/admin", views.it1_admin,name="it1"),
    path("department/it/year/second/admin", views.it2_admin,name="it2"),
    path("department/it/year/third/admin", views.it3_admin,name="it3"),
    path("department/it/year/final/admin", views.it4_admin,name="it4"),

    path("department/eee/year/first/admin", views.eee1_admin,name="eee1"),
    path("department/eee/year/second/admin", views.eee2_admin,name="eee2"),
    path("department/eee/year/third/admin", views.eee3_admin,name="eee3"),
    path("department/eee/year/final/admin", views.eee4_admin,name="eee4"),

    path("department/ece/year/first/admin", views.ece1_admin,name="ece1"),
    path("department/ece/year/second/admin", views.ece2_admin,name="ece2"),
    path("department/ece/year/third/admin", views.ece3_admin,name="ece3"),
    path("department/ece/year/final/admin", views.ece4_admin,name="ece4"),

    path("department/mech/year/first/admin", views.mech1_admin,name="mech1"),
    path("department/mech/year/second/admin", views.mech2_admin,name="mech2"),
    path("department/mech/year/third/admin", views.mech3_admin,name="mech3"),
    path("department/mech/year/final/admin", views.mech4_admin,name="mech4"),

    path("department/civil/year/first/admin", views.civil1_admin,name="civil1"),
    path("department/civil/year/second/admin", views.civil2_admin,name="civil2"),
    path("department/civil/year/third/admin", views.civil3_admin,name="civil3"),
    path("department/civil/year/final/admin", views.civil4_admin,name="civil4"),

    path("department/cse/year/first/adddata",views.cse1_adddata),
    path("department/cse/year/second/adddata", views.cse2_adddata),
    path("department/cse/year/third/adddata", views.cse3_adddata),
    path("department/cse/year/final/adddata", views.cse4_adddata),

    path("department/it/year/first/adddata", views.it1_adddata),
    path("department/it/year/second/adddata", views.it2_adddata),
    path("department/it/year/third/adddata", views.it3_adddata),
    path("department/it/year/final/adddata", views.it4_adddata),

    path("department/ece/year/first/adddata", views.ece1_adddata),
    path("department/ece/year/second/adddata", views.ece2_adddata),
    path("department/ece/year/third/adddata", views.ece3_adddata),
    path("department/ece/year/final/adddata", views.ece4_adddata),

    path("department/eee/year/first/adddata", views.eee1_adddata),
    path("department/eee/year/second/adddata", views.eee2_adddata),
    path("department/eee/year/third/adddata", views.eee3_adddata),
    path("department/eee/year/final/adddata", views.eee4_adddata),

    path("department/mech/year/first/adddata", views.mech1_adddata),
    path("department/mech/year/second/adddata", views.mech2_adddata),
    path("department/mech/year/third/adddata", views.mech3_adddata),
    path("department/mech/year/final/adddata", views.mech4_adddata),

    path("department/civil/year/first/adddata", views.civil1_adddata),
    path("department/civil/year/second/adddata", views.civil2_adddata),
    path("department/civil/year/third/adddata", views.civil3_adddata),
    path("department/civil/year/final/adddata", views.civil4_adddata),



]
