#!/usr/bin/python
import GUI.MainWindow
from Data.System import *
from GUI.ListView import *

def test_search():
    GUI.MainWindow.switchPatientList(System.TheSystem.patientList)
    result = GUI.MainWindow.MainWindow.window.currentView.searchPatient("Garcia")
    assert result[0].firstName == "Sophia"