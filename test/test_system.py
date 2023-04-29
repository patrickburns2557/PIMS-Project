#!/usr/bin/python
from Data.System import *


def test_loadPlaceholderData():
    System.TheSystem.loadPlaceholderData()
    assert System.TheSystem.PatientList[len(System.TheSystem.PatientList) - 1].firstName == "first 19"


def test_getPatientList():
    list = getPatientList()
    assert list[0].firstName == "Sophia"


def test_getUser():
    LoginSystem.login(System.TheSystem.user, "volunteer", "volunteer")
    user = getUser()
    assert user.getUserType() == 3


def test_getUserType():
    LoginSystem.login(System.TheSystem.user, "officestaff", "officestaff")
    userType = getUserType()
    assert userType == 2


def test_logoutUser():
    LoginSystem.login(System.TheSystem.user, "test", "test")
    logoutUser()
    assert getUserType() == -1
