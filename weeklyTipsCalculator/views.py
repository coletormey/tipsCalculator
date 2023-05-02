from django.shortcuts import render, redirect
from django.forms.models import modelformset_factory # model form for querysets

from .models import Employee, TipsTotal
from .forms import EmployeeForm, HoursForm, TotalTipsForm

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
    totalTipsForm = TotalTipsForm(request.POST or None)
    form = HoursForm(request.POST or None)
    hoursFormSet = modelformset_factory(Employee, form=HoursForm, extra=0)
    qs = Employee.objects.order_by('hours')
    formset = hoursFormSet(request.POST or None, queryset=qs)

    context = {'formset': formset,
               'form': form,
               'totalTipsForm': totalTipsForm}

    if all([formset.is_valid()]):
        formset.save()
        totalTipsForm.save()
        for form in formset:
            form.save()

        totalHours = calculateTotalHours()
        checkingPercentage = Employee.calculateTipPercentage(
            Employee.objects.all(), totalHours
        )  # returns sum of all percentages. Should equal ~100%
        tipsTotal = totalTipsForm.clean.__get__('tipsTotal')
        print(tipsTotal)


        context['tipsCalculated'] = False


    return render(request, 'weeklyTipsCalculator/calculateTips.html', context)

def calculateTotalHours():
    totalHours = 0
    for employee in Employee.objects.all():
        totalHours += employee.hours
    return totalHours

def calculateTotalTips():
    totalTips = 0
    for employee in Employee.objects.all():
        totalTips += employee.tips
    return totalTips