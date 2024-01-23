from . models import task
from django import forms

class toddoform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']
