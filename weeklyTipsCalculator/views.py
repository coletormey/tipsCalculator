from django.shortcuts import render, redirect
from django.forms import formset_factory

from .models import Employee
from .forms import EmployeeForm, HoursForm

# Create your views here.
def index(request):
    '''The home page for weeklyTipsCalculator'''
    return render(request, 'weeklyTipsCalculator/index.html')

def employees(request):
    # Display all employees
    employees = Employee.objects.order_by('name')
    context = {'employees': employees}
    return render(request, 'weeklyTipsCalculator/employees.html', context)

def employeesSearch(request):
    query_dict = request.GET # is a dictionary
    try: # If input does not match anything, do nothing
        query = query_dict.get('query')
        employee = Employee.objects.get(name=query) # <input type="text" name="query"/>
    except:
        query = None
    employee = None
    if query is not None:
        employee = Employee.objects.get(name=query)
    context = {'employee': employee}
    return render(request, "weeklyTipsCalculator/search.html", context)

def addEmployee(request):
    form = EmployeeForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        # context['form'] = EmployeeForm()
        employeeObject = Employee.objects.create(name=form.cleaned_data.get("name"))
        employeeObject.hours = 0
        employeeObject.save()
        context['employee'] = employeeObject
        context['created'] = True

    return render(request, 'weeklyTipsCalculator/addEmployee.html', context)

def employee(request, name):
    # Display a single employee and their information
    if name is not None:
        employee = Employee.objects.get(id=name)
    context = {'employee': employee}
    return render(request, 'weeklyTipsCalculator/employee.html', context)

def calculateTips(request):
    hoursFormSet = formset_factory(HoursForm, extra=Employee.objects.count())
    formset = hoursFormSet()
    context = {'formset': formset}
    if request.method == 'POST':
        formset = {hoursFormSet(request.POST, request.FILES)}
        if formset.is_valid():
            for form in formset:
                if form.cleaned_date:
                    None
    return render(request, 'weeklyTipsCalculator/calculateTips.html', context)