#!/usr/bin/python
from Data.System import *

def test_loadPlaceholderData():
    sys = System()
    sys.loadPlaceholderData()
    assert sys.patientList[len(sys.patientList) -1].firstName == "first 19"

def test_getPatientList():
    initialize()
    list = getPatientList()
    assert list[0].firstName == "Sophia"

def test_getUser():
    initialize()
    loginSystem.login(System.TheSystem.user, "volunteer", "volunteer")
    user = getUser()
    assert user.getUserType() == 3

def test_getUserType():
    initialize()
    loginSystem.login(System.TheSystem.user, "officestaff", "officestaff")
    userType = getUserType()
    assert userType == 2

def test_logoutUser():
    initialize()
    window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())
    loginSystem.login(System.TheSystem.user, "test", "test")
    logoutUser()
    assert getUserType() == -1