from django.contrib import admin

# Register your models here.
from .models import Employee, TipsTotal

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hours', 'tips', 'percentageOfTips', 'timestamp', 'updated']
    search_fields = ['name']

class TipsTotalAdmin(admin.ModelAdmin):
    list_display = ['tipsTotal', 'dateAdded']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TipsTotal, TipsTotalAdmin)

