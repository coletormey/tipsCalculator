#!/usr/bin/env python3

from employee import (
    Employee,
    calculateEmployeeTips,
    calculateTipPercentage,
    saveAndDisplay,
)
import sys, os


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


listOfEmployees = []
totalHours = 0

fileName = "tipsInfo.txt"

try:
    with open(resource_path(fileName), "r") as file:
        for line in file:
            if line[0] == "$":
                totalTips = float(line[1:])
            elif line[0] == "~":
                date = line[1:]
            else:
                name, hours = line.split()
                newEmployee = Employee(name, hours)
                listOfEmployees.append(newEmployee)
                totalHours += float(hours)
except FileNotFoundError:
    print(f"\nThe file '{fileName}' could not be located.\n")
    exit()

checkingPercentage = calculateTipPercentage(
    listOfEmployees, totalHours
)  # returns sum of all percentages. Should equal ~100%
calculateEmployeeTips(listOfEmployees, totalTips)
saveAndDisplay(listOfEmployees, date, totalHours, totalTips, checkingPercentage)
