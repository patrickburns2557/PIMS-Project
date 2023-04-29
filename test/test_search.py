#!/usr/bin/python
import GUI.MainWindow
from Data.System import *
from GUI.ListView import *


def test_search():
    print(System.TheSystem.PatientList[0].firstName)
    GUI.MainWindow.switchPatientList(System.TheSystem.PatientList)
    result = GUI.MainWindow.MainWindow.window.currentView.searchPatient("Garcia")
    assert result[0].firstName == "Sophia"
