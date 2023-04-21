from django.contrib import admin

# Register your models here.
from .models import Employee, TipsTotal

admin.site.register(Employee)
admin.site.register(TipsTotal)
