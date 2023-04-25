import math


class Employee:
    def __init__(self, name, hours):
        self.name = name.lower()
        self.hours = hours
        self.percentageOfTips = 0
        self.tips = 0

    def getEmployeeInfo(self):
        return (
            f"{self.name.title()}\n"
            + f" * Hours worked: {self.hours}\n"
            + f" * Percentage of Tips: {self.percentageOfTips}%\n"
            + f" * Tips: ${self.tips}\n"
        )


"""~~~~~~~~~~~~~~~~~~~~~Employee Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


def calculateTipPercentage(listOfEmployees, totalHours):
    totalPercentage = 0
    for employee in listOfEmployees:
        employee.percentageOfTips = 100 * (float(employee.hours) / float(totalHours))
        totalPercentage += float(employee.percentageOfTips)
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
