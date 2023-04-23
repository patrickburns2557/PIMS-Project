#!/usr/bin/python
import GUI.MainWindow
from Data.System import *

def test_switchDetailedView():
    GUI.MainWindow.switchDetailedView(System.TheSystem.patientList[0])
    assert GUI.MainWindow.getViewType() == 1

def test_switchPatientList():
    GUI.MainWindow.switchPatientList(System.TheSystem.patientList)
    assert GUI.MainWindow.getViewType() == 0
    
def test_switchPatientCreationView():
    GUI.MainWindow.switchPatientCreationView(System.TheSystem.user)
    assert GUI.MainWindow.getViewType() == 2

def test_switchEditPatientView():
    GUI.MainWindow.switchEditPatientView(System.TheSystem.user)
    assert GUI.MainWindow.getViewType() == 3

def test_switchLoginView():
    GUI.MainWindow.switchLoginView(System.TheSystem.user)
    assert GUI.MainWindow.getViewType() == -1