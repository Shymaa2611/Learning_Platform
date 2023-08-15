from .models import Course
from django import forms
class courseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'