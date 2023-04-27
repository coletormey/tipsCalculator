from django.db import models
from datetime import datetime

# Create your models here.
class NameField(models.CharField):
    def get_prep_value(self, value):
        return str(value).lower()

class Employee(models.Model):
    name = NameField(max_length=25)
    hours = models.CharField(max_length=6)
    percentageOfTips = 0
    tips = 0

    def __str__(self):
        return (
            f"{self.name.title()}\n"
            + f" * Hours worked: {self.hours}\n"
            + f" * Percentage of Tips: {self.percentageOfTips}%\n"
            + f" * Tips: ${self.tips}\n"
        )

class TipsTotal(models.Model):
    tipsTotal = models.FloatField()
    dateAdded = datetime.now()


    def __str__(self):
        return (f"{self.dateAdded.date()} -- ${self.tipsTotal}")