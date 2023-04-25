from django.contrib import admin

# Register your models here.
from .models import Employee, TipsTotal

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TipsTotal)
