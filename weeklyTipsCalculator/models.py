from django.db import models
from django.utils.text import slugify
from datetime import datetime
import math

# Create your models here.
class NameField(models.CharField):
    def get_prep_value(self, value):
        return str(value).lower()

class Employee(models.Model):
    name = NameField(max_length=25)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    hours = models.FloatField(max_length=6)
    percentageOfTips = 0
    tips = 0

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.name.title()}\n"
            + f" * Hours worked: {self.hours}\n"
            + f" * Percentage of Tips: {self.percentageOfTips}%\n"
            + f" * Tips: ${self.tips}\n"
        )
    
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def calculateTipPercentage(listOfEmployees, totalHours):
        totalPercentage = 0
        for employee in Employee.objects.all():
            employee.percentageOfTips = 100 * (float(employee.hours) / float(totalHours))
            totalPercentage += float(employee.percentageOfTips)
            employee.save()
        print(Employee.objects.order_by('name'))
        return totalPercentage


    def calculateEmployeeTips(listOfEmployees, totalTips):
        for employee in listOfEmployees:
            employee.tips = (
                math.floor((employee.percentageOfTips / 100 * totalTips) * 100) / 100
            )


    def saveAndDisplay(listOfEmployees, date, totalHours, totalTips, checkingPercentage):
        with open(f"tips.txt", "w") as file:
            file.write(date)
            print(date)
            finalInfo = (
                f"\nTotal tips for the week: ${totalTips}\n"
                + f"Total number of hours worked: {totalHours}\n"
                + f"Sum of each employee's 'Pecentage of Tips': {checkingPercentage}%\n"
            )

        for employee in listOfEmployees:
            employeeInfo = employee.getEmployeeInfo()
            file.write(employeeInfo + "\n")
            print(employeeInfo)

        file.write(finalInfo)
        print(finalInfo)




class TipsTotal(models.Model):
    tipsTotal = models.FloatField()
    dateAdded = datetime.now()

    def __str__(self):
        return (
            f"{self.tipsTotal}"
        )


#     def __str__(self):
#         return (f"{self.dateAdded.date()} -- ${self.tipsTotal}")