from django import forms
from django.forms import formset_factory

from .models import Employee

class TipsForm(forms.ModelForm):
    listOfEmployees = []
    employees = Employee.objects.order_by('hours')
    for employee in employees:
        listOfEmployees.append(employee)
    employee = listOfEmployees.pop()    
    # for employee in employees:
    #     employee.hours = forms.FloatField()
    
    hours = forms.FloatField(label=f"{employee.name}'s hours", max_value=999)
    
    class Meta:
        model = Employee
        fields = ['hours']

