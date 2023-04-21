from django.shortcuts import render, redirect
from django.forms import formset_factory

from .models import Employee
from .forms import TipsForm

# Create your views here.
def index(request):
    '''The home page for weeklyTipsCalculator'''
    return render(request, 'weeklyTipsCalculator/index.html')

def employees(request):
    # Display all employees
    employees = Employee.objects.order_by('hours')
    context = {'employees': employees}
    return render(request, 'weeklyTipsCalculator/employees.html', context)

def employee(request, name):
    # Display a single employee and their information
    employee = Employee.objects.get(id=name)
    context = {'employee': employee}
    return render(request, 'weeklyTipsCalculator/employee.html', context)

def calculateTips(request):
    # Display the fields to enter hours for each employee, 
    # as well as total tip amount

    listOfEmployees = []
    employees = Employee.objects.order_by('hours')
    for employee in employees:
        listOfEmployees.append(employee)
    employee = listOfEmployees.pop()



    if request.method != 'POST':
        # Create a blank form
            

            form1 = TipsForm(prefix='form1', instance=employee)
            employee = listOfEmployees.pop()
            form2 = TipsForm(prefix='form2', instance=employee)
    else:
        # POST data submitted; process data
        form1 = TipsForm(data=request.POST, prefix='form1', instance=employee)
        employee = listOfEmployees.pop()
        form2 = TipsForm(data=request.POST, prefix='form2', instance=employee)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('weeklyTipsCalculator:index')

    context = {'employees': employees, 'form1': form1, 'form2': form2}
    return render(request, 'weeklyTipsCalculator/calculateTips.html', context)