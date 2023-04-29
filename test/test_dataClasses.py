#!/usr/bin/python
from Data.DataClasses import *


def test_user():
    newUser = User()
    newUser.setUserType(0)
    type = newUser.getUserType()
    assert type == 0


def test_login():
    newUser = User()
    validLogin = LoginSystem.login(newUser, "test", "test")
    assert validLogin is True
