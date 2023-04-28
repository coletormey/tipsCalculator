from django import forms
from django.forms import formset_factory

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']

    def clean(self):
        data = self.cleaned_data
        name = data.get('name')
        qs = Employee.objects.filter(name__icontains=name)
        if qs.exists():
            self.add_error('name', f'"{name}" is already in use')
        return data

class HoursForm(forms.ModelForm):    
    class Meta():
        model = Employee
        fields = ['hours']


    def clean(self):
        data = self.cleaned_data
        hours = data.get('hours')
        return hours






class EmployeeFormOld(forms.Form):
    # def __init__(self, listOfEmployees, *args, **kwargs):
    #     super(TipsForm, self).__init__(*args, **kwargs)
    #     employee = listOfEmployees.pop()
    #     employee.hours = forms.FloatField(label=f"{employee.name}'s hours", max_value=999)
    #     while listOfEmployees:
            
    #         if listOfEmployees:
    #             employee = listOfEmployees.pop()
    #         else:
    #             break

    name = forms.CharField()
    hours = 0

    # def clean_name(self):
    #     cleaned_data = self.cleaned_data #dictionary
    #     print("cleaned_data", cleaned_data)
    #     name = str(cleaned_data.get('name'))
    #     if name.lower().strip() == "cole":
    #         raise forms.ValidationError("This name already exists!")
    #     print("name", name)
    #     return name
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        name = str(cleaned_data.get('name'))
        content = cleaned_data.get()
        if name.lower().strip() == "cole":
            self.add_error('name', 'This name is taken!')
            # raise forms.ValidationError("This name already exists!")
        return cleaned_data
    

