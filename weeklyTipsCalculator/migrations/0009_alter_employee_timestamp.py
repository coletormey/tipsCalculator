# Generated by Django 4.2 on 2023-04-27 23:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "weeklyTipsCalculator",
            "0008_alter_employee_timestamp_alter_employee_updated",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="timestamp",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
