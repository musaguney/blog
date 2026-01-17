from socket import fromshare
from django import forms
from .models import Linux

class LinuxForm(forms.ModelForm):
    class Meta:
        model = Linux
        fields = ["ipadi","kullaniciadi","sifreadi","portadi","komutadi"]
        