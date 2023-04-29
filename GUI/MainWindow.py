import customtkinter as ctk

import GUI.EditPatientsView as EditGui
import GUI.ListView as lv
import GUI.NewPatientView as CreateGui
import GUI.PatientDetailedView as pdv
import GUI.TopBarGui as tb
import GUI.LoginView as lgn


class MainWindow(ctk.CTk):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    # print(ctk.get_appearance_mode())
    window = None  # Class variable to hold itself in so that other classes can make calls to the MainWindow class and change the window's views
    viewType = None  # holds the current view (0 for patient list, 1 for detailedView) so other classes know which view the user is on
    currentPatient = None  # the patient the user is currently looking at

    def __init__(self, patientList, user):
        super().__init__()
        MainWindow.window = self  # Store self into class variable upon creation
        MainWindow.viewType = self

        self.geometry("1280x720")
        self.title("Patient Information Management System (PIMS)")
        # Skip loading window icon if it fails since it's not strictly necessary
        try:
            self.iconbitmap('./logo.ico')
        except:
            pass
        self.minsize(1280, 720)

        self.topBar = tb.TopBar(self)
        self.topBar.grid(row=0, column=0, sticky="ew", columnspan=10)

        self.currentView = lgn.LoginView(self, user)  # Default view when starting program
        self.currentView.grid(row=1, column=1, sticky="news", columnspan=10)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)


# Function to allow other classes to change the current view in the window to PatientDetailedView
def switchDetailedView(patient):
    MainWindow.window.currentView.destroy()

    MainWindow.currentPatient = patient
    MainWindow.window.currentView = pdv.PatientDetailedView(MainWindow.window, patient)
    MainWindow.window.currentView.grid(row=1, column=1, sticky="news", columnspan=10)

    MainWindow.viewType = 1


# Function to allow other classes to change the current view in the window to PatientList
def switchPatientList(patientList):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = lv.ListView(MainWindow.window, patientList)
    MainWindow.window.currentView.grid(row=1, column=0, sticky="news", columnspan=10)
    MainWindow.viewType = 0


# view to go to NewPatientCreation window
def switchPatientCreationView(user):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = CreateGui.NewPatientView(MainWindow.window, user)
    MainWindow.window.currentView.grid(row=1, column=0, sticky="news", columnspan=10)
    MainWindow.viewType = 2


# view to go to EditPatientWindow window
def switchEditPatientView(user):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = EditGui.EditPatientView(MainWindow.window, user, getCurrentPatient())
    MainWindow.window.currentView.grid(row=1, column=0, sticky="news", columnspan=10)
    MainWindow.viewType = 3


# Function to allow other classes to change the current view in the window to LoginView
def switchLoginView(user):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = lgn.LoginView(MainWindow.window, user)
    MainWindow.window.currentView.grid(row=1, column=0, sticky="news", columnspan=10)
    MainWindow.viewType = -1


# checks if user is looking at patients list or single patient
def getViewType():
    return MainWindow.viewType


# pull which patient the user is currently looking at
def getCurrentPatient():
    return MainWindow.currentPatient


# Function to allow other classes to update the top bar, such as when a different user type logs in
def updateTopBar():
    MainWindow.window.topBar.destroy()

    MainWindow.window.topBar = tb.TopBar(MainWindow.window)
    MainWindow.window.topBar.grid(row=0, column=0, sticky="ew", columnspan=10)
