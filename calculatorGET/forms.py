from django import forms
from .models import CalcGET
class CalcForm(forms.ModelForm):
    operation_type = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ]
    operations = forms.CharField(label="Choose operation", widget=forms.Select(choices=operation_type))
    class Meta:
        model = CalcGET
        fields = ('x','y','operations',)