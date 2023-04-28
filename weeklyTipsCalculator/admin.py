from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hours', 'timestamp', 'updated', 'hoursSet']
    search_fields = ['name']

admin.site.register(Employee, EmployeeAdmin)

