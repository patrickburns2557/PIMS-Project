#!/usr/bin/python
from Data.System import *

def test_searchPatient():
    
    initialize()
    window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())
    loginSystem.login(System.TheSystem.user, "test", "test")
    
    GUI.MainWindow.switchPatientList(getPatientList())
    window.searchPatient("Garcia")