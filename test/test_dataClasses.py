#!/usr/bin/python
from Data.dataClasses import *

def test_user():
    newUser = User()
    newUser.setUserType(0)
    type = newUser.getUserType()
    assert type == 0

def test_login():
    newUser = User()
    validLogin = loginSystem.login(newUser, "test", "test")
    assert validLogin == True