from django import forms
from .models import User

class authenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']