from .models import Clent
from django import forms

class ClentForm(forms.ModelForm):
    class Meta:
        model=Clent
        exclude=[""]
