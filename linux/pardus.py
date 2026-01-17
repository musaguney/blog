from tabnanny import verbose
from unicodedata import name
from django.db import models
from urllib import request
import paramiko
import time
import linux
from linux.models import Linux
from linux.views import Linux
#from linux.views import linuxdetail, linuxs
#import linux.pardus import views

#def __init__(self):
 #       self.view = Linux()
#Burasi bilgilerin girildigi bolum
ip = "192.168.43.114"
kullanici = 'musa'
sifre = 'q'
port = "22"
BilgisayarKomut = 'pwd'
BilgisayarKullanicilarinAdi = "awk -F':' '$3>=500 && $3<=60000 {print $1 " "}' /etc/passwd"
BilgisayarHostname = "uname -n"
BilgisayarIp = "ip -br a"
BilgisayarToplamRam = "grep MemTotal /proc/meminfo"
BilgisayarToplamBosRam = "grep MemFree /proc/meminfo"
BilgisayarDiskToplam = "df -h"
BilgisayarCPU = "lscpu |grep name && lscpu | grep MHz"
#BilgisayarCPUName = "lscpu | grep name"



#Burasi verilen bilgilere gore baglanti kuran yer
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,kullanici,sifre,timeout = 10)

#komut1= 
stdin,stdout,stderr = ssh.exec_command(BilgisayarKomut)
sonuc10 = stdout.read()
print("verilen Komut")
print(sonuc10.decode("utf-8"))

#komut1=KullanicilarinAdi
stdin,stdout,stderr = ssh.exec_command(BilgisayarKullanicilarinAdi)
sonuc = stdout.read()
print("kullanicilarin adi")
print(sonuc.decode("utf-8"))

#komut1= bilgisayarin Hostname
stdin,stdout,stderr = ssh.exec_command(BilgisayarHostname)
sonuc2 = stdout.read()
print("bilgisayarin Hostname")
print(sonuc2.decode("utf-8"))

#komut1= bilgisayarin ip adresleri 
stdin,stdout,stderr = ssh.exec_command(BilgisayarIp)
sonuc3 = stdout.read()
print("bilgisayarin ip adresleri")
print("")
print(sonuc3.decode("utf-8"))





#komut1= bilgisayarin toplam ram miktari GB
stdin,stdout,stderr = ssh.exec_command(BilgisayarToplamRam)
sonuc4 = stdout.read()
degistir = sonuc4.decode("utf-8")
degistir2 = degistir.split()
degistir4 = degistir2[1]
strings = [str(integer) for integer in degistir4]
a_string = "".join(strings)
an_integer = int(a_string)

RamGB = round(an_integer / 1024**2, 3)
print("bilgisayarin toplam ram miktari GB")
print(RamGB)
print("")

#komut1= bilgisayarin toplam bos ram miktari GB
stdin,stdout,stderr = ssh.exec_command(BilgisayarToplamBosRam)
sonuc49 = stdout.read()
degistir9 = sonuc49.decode("utf-8")
degistir29 = degistir9.split()
degistir49 = degistir29[1]
strings9 = [str(integer9) for integer9 in degistir49]
a_string9 = "".join(strings9)
an_integer9 = int(a_string9)

BosRamGB = round(an_integer9 / 1024**2, 3)
print("bilgisayarin toplam bos ram miktari GB")
print(BosRamGB)
print("")

#komut1= bilgisayarin toplam % disk kullanimi 
stdin,stdout,stderr = ssh.exec_command(BilgisayarDiskToplam)
sonuc5 = stdout.read()
print("bilgisayarin toplam  disk kullanimi")
print(sonuc5.decode("utf-8"))

#komut1= bilgisayarin toplam CPU kullanimi 
stdin,stdout,stderr = ssh.exec_command(BilgisayarCPU)
sonuc7 = stdout.read()
print("bilgisayarin toplam CPU miktari")
print(sonuc7.decode("utf-8"))
time.sleep(0.5)  

def post(self, request):
    if request.POST.get('op') == "delete":
            result = self.delete_user_ldap(request.POST.get('uid'), request.POST.get('ou'), request.POST.get('dc'))
            return JsonResponse({"result": result})

ssh.close()




