from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class NameField(models.CharField):
    def get_prep_value(self, value):
        return str(value).lower()

class Employee(models.Model):
    name = NameField(max_length=25)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    hours = models.CharField(max_length=6)
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
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




# class TipsTotal(models.Model):
#     tipsTotal = models.FloatField()
#     dateAdded = datetime.now()


#     def __str__(self):
#         return (f"{self.dateAdded.date()} -- ${self.tipsTotal}")