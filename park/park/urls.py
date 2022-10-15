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
from django.contrib import admin
from django.urls import path
from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.login),
    path("department/",views.dep),

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
]
