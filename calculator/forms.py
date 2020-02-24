from django import forms
from .models import calc
class CalcForm(forms.ModelForm):
    operation_type = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ]
    operations = forms.CharField(label="Choose operation", widget=forms.Select(choices=operation_type))
    class Meta:
        model = calc
        fields = ('x','y','operations',)