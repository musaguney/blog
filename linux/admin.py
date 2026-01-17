from django.contrib import admin
from .models import Linux,Pardus
# Register your models here.
@admin.register(Linux)
class LinuxAdmin(admin.ModelAdmin):
    list_display = ["kullaniciadi","ipadi","author","dateadi"]
    list_display_links = ["kullaniciadi","ipadi","dateadi"]
    search_fields = ["kullaniciadi"]
    
    list_filter = ["dateadi"]
    
    class Meta:
        model = Linux
        
@admin.register(Pardus)
class LinuxAdmin(admin.ModelAdmin):
    list_display = ["ip","kullanicilarinAdi","hostname"]
    list_display_links = ["ip","kullanicilarinAdi","hostname"]
    search_fields = ["kullanicilarinAdi"]
    
    list_filter = ["ip"]
    
    class Meta:
        model = Pardus