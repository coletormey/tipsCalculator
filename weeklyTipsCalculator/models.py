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

    hours = models.FloatField(max_length=6, default=0)
    percentageOfTips = models.FloatField(max_length=6, default=0)
    tips = models.FloatField(max_length=6, default=0)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.name.title()}\n"
            + f" * Hours worked: {self.hours}\n"
            + f" * Percentage of Tips: {self.percentageOfTips}%\n"
            + f" * Tips: ${self.tips}\n"
        )

    def calculateTipPercentage(employee, totalHours):
        return 100 * (employee.hours / float(totalHours))


    def calculateEmployeeTips(employee, totalTips):
        return math.floor(((employee.percentageOfTips / 100) * totalTips.tipsTotal) * 100) / 100


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
            f"${self.tipsTotal}"
        )