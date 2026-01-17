from django.contrib import admin
from django.urls import path

from linux import pardus
from . import views

app_name = "linux"


urlpatterns = [
    path('linuxdashboard/',views.linuxDashboard,name = "linuxdashboard"),
    path('',views.linuxs,name = "linuxs"),
    path('linuxaddarticle/',views.linuxAddArticle,name = "linuxaddarticle"),
    path('linux/<int:id>',views.linuxdetail,name = "linuxdetail"),
    path('linuxupdate/<int:id>',views.updateLinux,name = "linuxupdate"),
    path('linuxdelete/<int:id>',views.deleteLinux,name = "linuxdelete"),   
]

#path('linuxdetail/<str:id>', views.pardusv, name="ip")
    #path('linuxdetail/', views.pardusv, name="BilgisayarCPU")