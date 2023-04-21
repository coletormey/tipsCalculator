from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    hours = models.FloatField()

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