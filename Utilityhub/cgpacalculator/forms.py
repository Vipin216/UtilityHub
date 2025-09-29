from django import forms 
from .models import GPA

class GPAForm(forms.ModelForm):
    class Meta:
        model = GPA
        fields = ['credit','grade']