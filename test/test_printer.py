#!/usr/bin/python
import GUI.MainWindow
from Data.Printer import *
from Data.System import *


def test_print():
    LoginSystem.login(System.TheSystem.user, "test", "test")
    GUI.MainWindow.switchPatientList(System.TheSystem.PatientList)
    initPrint(0)
    f = open(REPORT_NAME, 'r')
    lines = f.readlines()

    name = lines[5].split()[1]
    print(name)
    assert name == "Benjamin"
