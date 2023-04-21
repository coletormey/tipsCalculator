from employee import (
    Employee,
    calculateEmployeeTips,
    calculateTipPercentage,
    saveAndDisplay,
)
import sys, os
import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [
    [sg.Text("Tips Calculator")],
    [sg.Button("Add New\nEmployee"), sg.Button("Calculate\nTips")],
]

window = sg.Window("Tips Calculator", layout)

while 1:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if use closes window or clicks cancel
        break
    print("You entered ", values[0])

window.close()
