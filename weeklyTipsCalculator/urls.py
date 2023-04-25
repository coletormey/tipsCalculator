'''Defines URL patterns for weeklyTipsCalculator'''
from django.urls import path
from . import views

app_name = 'weeklyTipsCalculator'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Displays search results for employees
    path('employees/', views.employeesSearch, name='employeesSearch'),
    # Displays Employees and their info
    path('employees/', views.employees, name='employees'),
    # Displays single employee and their info
    path('employees/<str:name>/', views.employee, name='employee'),
    # Displays fields to enter employee hours and total tip amount
    path('calculateTips/', views.calculateTips, name='calculateTips'),
]