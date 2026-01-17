from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
#from linux import pardus

from linux.models import Linux
import user
from .forms import LinuxForm
from django.contrib import messages
from .models import Linux,Pardus
import os
from django.contrib.auth.decorators import login_required
from linux.pardus import ip
#import psutil
from linux.pardus import sonuc5

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")   


@login_required(login_url="user:login")
def linuxDashboard(request):
    linuxs = Linux.objects.filter(author = request.user)
    context = {
        "linuxs":linuxs
    }
    return render(request, "linuxdashboard.html",context)


@login_required(login_url="user:login")
def linuxAddArticle(request):
    form = LinuxForm(request.POST or None)
    
    if form.is_valid():
        linux = form.save(commit=False)
        
        linux.author = request.user
        linux.save()
        
        messages.success(request,"Pardus Bilgisayar basariyla eklendi")
        return redirect("index")
    
    return render(request, "linuxaddarticle.html",{"form":form})

from django.core.files import File



@login_required(login_url="user:login")
def linuxdetail(request,id):
    #linux = Linux.objects.filter(id = id).first()
    linux = get_object_or_404(Linux,id = id)
    #linux = sonuc5
    #print (linux)
    #linuxAddArticle(linux)
    return render(request, "linuxdetail.html", {"linux":linux})

#def linuxdetails(request,id):
    #article = Article.objects.filter(id = id).first()
#    linux = get_object_or_404(Linux,ip = id)
def __init__(self):
    self.cpu = psutil.cpu_percent()    
def view_cpu(self):
        cpu_info = self.cpu
        return cpu_info    



@login_required(login_url="user:login")
def linuxs(request):
    return render(request, "linuxs.html")



@login_required(login_url="user:login")
def updateLinux(request,id):
    linux = get_object_or_404(Linux,id = id)
    form = LinuxForm(request.POST or None,instance= linux)
    if form.is_valid():
        linux = form.save(commit=False)
        linux.author = request.user
        linux.save()
        messages.success(request,"Pardus Bilgisayari Basarili Bir Sekilde Guncellendi")
        return redirect("linux:linuxdashboard")
    
    return render(request,"linuxupdate.html",{"form":form})

@login_required(login_url="user:login")
def deleteLinux(request,id):
    linux = get_object_or_404(Linux,id = id)
    linux.delete()
    messages.success(request,"Pardus Bilgisayari basariyla silindi")
    return redirect("linux:linuxdashboard")


# Create a Python file object using open() and the with statement
#with open('\linux\pardus.py', 'w') as f:
 #    myfile = File(f)
  #   myfile.write('Hello World')
   #  linux = Linux.objects.filter(id = id).first()
#render(request, "pardus.py", {"linux":linux})

#myfile.closed
#True
#f.closed
#True