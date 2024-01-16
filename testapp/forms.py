from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import entropy,siteuser,photopost

class usercreation(UserCreationForm):
    # myname=forms.CharField(max_length=100,required=False)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class entropyform(forms.ModelForm):
    class Meta:
        model=entropy
        fields='__all__'
        labels={'rmssd':'rmssd','sd1':'sd1','sd2':'sd2','s':'s','sd1sd2':'sd1/sd2'}

class profileform(forms.ModelForm):
    class Meta:
        model=siteuser
        fields=['profile']

class photoform(forms.Form):
    photo=forms.ImageField()