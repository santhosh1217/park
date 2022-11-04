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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path("<str:id>/departments",views.login,name="login"),
    path("<str:id>/admin",views.login,name="login"),
    path("",views.institute_login,name="home"),
    path("signup",views.signup),
    path("submit",views.submit),
    path("<str:id>/home",views.home),
    
   
    #######################################################################  UPDATE  ###################################
    path("<str:user>/cse/1/admin/update/<int:id>",views.update,name="updatecse1"),
    path("<str:user>/cse/2/admin/update/<int:id>",views.update,name="updatecse1"),
    path("<str:user>/cse/3/admin/update/<int:id>",views.update,name="updatecse1"),
    path("<str:user>/cse/4/admin/update/<int:id>",views.update,name="updatecse1"),
    path("<str:user>/it/1/admin/update/<int:id>",views.update,name="updateit1"),
    path("<str:user>/it/2/admin/update/<int:id>",views.update,name="updateit1"),
    path("<str:user>/it/3/admin/update/<int:id>",views.update,name="updateit1"),
    path("<str:user>/it/4/admin/update/<int:id>",views.update,name="updateit1"),
    path("<str:user>/ece/1/admin/update/<int:id>",views.update,name="updateece1"),
    path("<str:user>/ece/2/admin/update/<int:id>",views.update,name="updateece1"),
    path("<str:user>/ece/3/admin/update/<int:id>",views.update,name="updateece1"),
    path("<str:user>/ece/4/admin/update/<int:id>",views.update,name="updateece1"),
    path("<str:user>/mech/1/admin/update/<int:id>",views.update,name="updatemech1"),
    path("<str:user>/mech/2/admin/update/<int:id>",views.update,name="updatemech1"),
    path("<str:user>/mech/3/admin/update/<int:id>",views.update,name="updatemech1"),
    path("<str:user>/mech/4/admin/update/<int:id>",views.update,name="updatemech1"),
    path("<str:user>/eee/1/admin/update/<int:id>",views.update,name="updateeee"),
    path("<str:user>/eee/2/admin/update/<int:id>",views.update,name="updateeee"),
    path("<str:user>/eee/3/admin/update/<int:id>",views.update,name="updateeee"),
    path("<str:user>/eee/4/admin/update/<int:id>",views.update,name="updateeee"),
    path("<str:user>/civil/1/admin/update/<int:id>",views.update,name="updatecivil"),
    path("<str:user>/civil/2/admin/update/<int:id>",views.update,name="updatecivil"),
    path("<str:user>/civil/3/admin/update/<int:id>",views.update,name="updatecivil"),
    path("<str:user>/civil/4/admin/update/<int:id>",views.update,name="updatecivil"),


#############################################################################  DELETE  ##################################
    path("<str:user>/cse/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/cse/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/cse/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/cse/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/it/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/it/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/it/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/it/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/ece/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/ece/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/ece/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/ece/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/mech/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/mech/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/mech/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/mech/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/eee/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/eee/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/eee/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/eee/4/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/civil/1/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/civil/2/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/civil/3/admin/delete/<int:id>",views.delete,name="delete"),
    path("<str:user>/civil/4/admin/delete/<int:id>",views.delete,name="delete"),

    path("<str:user>/cse",views.year),
    path("<str:user>/it",views.year),
    path("<str:user>/ece",views.year),
    path("<str:user>/eee",views.year),
    path("<str:user>/mech",views.year),
    path("<str:user>/civil",views.year),

    path("<str:user>/cse/1/",views.department),
    path("<str:user>/cse/2/", views.department),
    path("<str:user>/cse/3/", views.department),
    path("<str:user>/cse/4/", views.department),

    path("<str:user>/ece/1/", views.department),
    path("<str:user>/ece/2/", views.department),
    path("<str:user>/ece/3/", views.department),
    path("<str:user>/ece/4/", views.department),

    path("<str:user>/it/1/", views.department),
    path("<str:user>/it/2/", views.department),
    path("<str:user>/it/3/", views.department),
    path("<str:user>/it/4/", views.department),

    path("<str:user>/mech/1/", views.department),
    path("<str:user>/mech/2/", views.department),
    path("<str:user>/mech/3/", views.department),
    path("<str:user>/mech/4/", views.department),

    path("<str:user>/eee/1/", views.department),
    path("<str:user>/eee/2/", views.department),
    path("<str:user>/eee/3/", views.department),
    path("<str:user>/eee/4/", views.department),

    path("<str:user>/civil/1/", views.department),
    path("<str:user>/civil/2/", views.department),
    path("<str:user>/civil/3/", views.department),
    path("<str:user>/civil/4/", views.department),

    path("<str:user>/cse/1/admin/",views.admin,name="cse1"),
    path("<str:user>/cse/2/admin/", views.admin,name="cse2"),
    path("<str:user>/cse/3/admin/", views.admin,name="cse3"),
    path("<str:user>/cse/4/admin/", views.admin,name="cse4"),

    path("<str:user>/it/1/admin/", views.admin,name="it1"),
    path("<str:user>/it/2/admin/", views.admin,name="it2"),
    path("<str:user>/it/3/admin/", views.admin,name="it3"),
    path("<str:user>/it/4/admin/", views.admin,name="it4"),

    path("<str:user>/eee/1/admin/", views.admin,name="eee1"),
    path("<str:user>/eee/2/admin/", views.admin,name="eee2"),
    path("<str:user>/eee/3/admin/", views.admin,name="eee3"),
    path("<str:user>/eee/4/admin/", views.admin,name="eee4"),
    path("<str:user>/ece/1/admin/", views.admin,name="ece1"),
    path("<str:user>/ece/2/admin/", views.admin,name="ece2"),
    path("<str:user>/ece/3/admin/", views.admin,name="ece3"),
    path("<str:user>/ece/4/admin/", views.admin,name="ece4"),

    path("<str:user>/mech/1/admin/", views.admin,name="mech1"),
    path("<str:user>/mech/2/admin/", views.admin,name="mech2"),
    path("<str:user>/mech/3/admin/", views.admin,name="mech3"),
    path("<str:user>/mech/4/admin/", views.admin,name="mech4"),

    path("<str:user>/civil/1/admin/", views.admin,name="civil1"),
    path("<str:user>/civil/2/admin/", views.admin,name="civil2"),
    path("<str:user>/civil/3/admin/", views.admin,name="civil3"),
    path("<str:user>/civil/4/admin/", views.admin,name="civil4"),

    path("<str:user>/cse/1/admin/adddata",views.adddata),
    path("<str:user>/cse/2/admin/adddata", views.adddata),
    path("<str:user>/cse/3/admin/adddata", views.adddata),
    path("<str:user>/cse/4/admin/adddata", views.adddata),

    path("<str:user>/it/1/admin/adddata", views.adddata),
    path("<str:user>/it/2/admin/adddata", views.adddata),
    path("<str:user>/it/3/admin/adddata", views.adddata),
    path("<str:user>/it/4/admin/adddata", views.adddata),

    path("<str:user>/ece/1/admin/adddata", views.adddata),
    path("<str:user>/ece/2/admin/adddata", views.adddata),
    path("<str:user>/ece/3/admin/adddata", views.adddata),
    path("<str:user>/ece/4/admin/adddata", views.adddata),

    path("<str:user>/eee/1/admin/adddata", views.adddata),
    path("<str:user>/eee/2/admin/adddata", views.adddata),
    path("<str:user>/eee/3/admin/adddata", views.adddata),
    path("<str:user>/eee/4/admin/adddata", views.adddata),

    path("<str:user>/mech/1/admin/adddata", views.adddata),
    path("<str:user>/mech/2/admin/adddata", views.adddata),
    path("<str:user>/mech/3/admin/adddata", views.adddata),
    path("<str:user>/mech/4/admin/adddata", views.adddata),

    path("<str:user>/civil/1/admin/adddata", views.adddata),
    path("<str:user>/civil/2/admin/adddata", views.adddata),
    path("<str:user>/civil/3/admin/adddata", views.adddata),
    path("<str:user>/civil/4/admin/adddata", views.adddata),

    path("<str:user>/cse/third/submit/",views.cse3_submit),



]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
