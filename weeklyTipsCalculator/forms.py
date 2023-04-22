from django import forms
from django.forms import formset_factory

from .models import Employee

class TipsForm(forms.ModelForm):
    def __init__(self, listOfEmployees, *args, **kwargs):
        super(TipsForm, self).__init__(*args, **kwargs)
        employee = listOfEmployees.pop()
        employee.hours = forms.FloatField(label=f"{employee.name}'s hours", max_value=999)
        while listOfEmployees:
            
            if listOfEmployees:
                employee = listOfEmployees.pop()
            else:
                break
    
    class Meta:
        model = Employee
        fields = ['hours']

