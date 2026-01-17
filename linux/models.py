from django.db import models
import os
import importlib.machinery
import importlib.util
# Create your models here.

class Linux(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="Admin" )
    ipadi = models.GenericIPAddressField(max_length= 100,verbose_name="Ip adresi" )
    kullaniciadi = models.CharField(max_length= 100,verbose_name="User Adi" )
    sifreadi = models.CharField(max_length= 100,verbose_name="Sifre" )
    portadi = models.CharField(max_length= 100,verbose_name="Port Numarasi" )
    komutadi = models.CharField(max_length= 200,verbose_name="Calistirilmasi istenen komut" )
    dateadi = models.DateTimeField(auto_now_add=True,verbose_name="olusturulma tarihi" )
    def __str__(self):
        return self.kullaniciadi
    
    
    
class Pardus(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="Admin" )
    komut = models.CharField(max_length= 10000,verbose_name="komut" )
    kullanicilarinAdi = models.CharField(max_length= 10000,verbose_name="kullanicilarinAdi" )
    hostname = models.CharField(max_length= 10000,verbose_name="hostname" )
    ip = models.CharField(max_length= 10000,verbose_name="ip" )
    toplamRam = models.CharField(max_length= 10000,verbose_name="toplamRam" )
    toplamBosRam = models.CharField(max_length= 10000,verbose_name="toplamBosRam" )
    diskToplam = models.CharField(max_length= 10000,verbose_name="diskToplam" )
    cPU = models.CharField(max_length= 10000,verbose_name="cPU" )
    def __str__(self):
        return self.kullaniciadi    
 

   
"""# Import mymodule
loader = importlib.machinery.SourceFileLoader( 'pardus', './pardus' )
spec = importlib.util.spec_from_loader( 'pardus', loader )
pardus = importlib.util.module_from_spec( spec )
loader.exec_module( pardus )

# Use mymodule
pardus.say_hello()"""